import glob, json, colorsys
from PIL import Image, ImageDraw

def collate(subdir="img"):
    #Collate.py looks at a culled image folder and the available index jsons and creates a new master json.
    import glob, json, re

    #new dict add {"filename": filename}
    #load all the img names into an array
    dir = subdir+"/*"

    filenames = [g[4:] for g in (glob.glob(dir))]
    index_filenames = [j for j in glob.glob(subdir+'/*.json') if ('errors' , 'culled' not in j)]
    indices_collated = []
    indices_culled = []
    
    for ifilename in index_filenames:
        with open (ifilename) as json_file:
            index_items = json.load(json_file)
            json_file.close()
        [indices_collated.append(i) for i in index_items]

    print "found ", len (indices_collated), " indices in JSON files"
    print "found ", len (filenames), " files in folder (including non-image files)"

    for filename in filenames:
        if ('.json' not in filename):
            namechunks = re.split('_', filename)
            print "chunking filename\t", namechunks
            type = unicode(namechunks[0])
            keyword = unicode(namechunks[1])
            id = unicode(namechunks[2].translate(None, 'jpgifnbmeJPGIFNBME.'))
            #print id
            
            for c in indices_collated:
                if (c['type'] == type and c['keyword'] == keyword and c['id'] == id):
                    c['filename'] = filename
                    indices_culled.append(c) 
                    
                    
    #print indices_collated[0]
    print "collated ", len (indices_culled), " valid image files"
    with open (subdir+'/culled_index.json', 'w') as json_file:
        json_file.write(json.dumps(indices_culled,indent=2))
        json_file.close()
    

# A variety of image processing functions to be applied to the culled Index

def calc_rgb_avg(im):
    pixels = [im.getpixel((x,y)) for x in range(im.size[0]) for y in range(im.size[1])]
    rgba = [(px[0],px[1],px[2],px[3]) for px in pixels ]
    def wght(tup,idx): return tup[idx] * (tup[3]/255.0)
    rgba_avg = [ sum([wght(tup,n) for tup in rgba])/sum([tup[3]/255.0 for tup in rgba]) for n in range(3)]
    return (int(rgba_avg[0]),int(rgba_avg[1]),int(rgba_avg[2]))

def process_for_web(subdir="img",webdir="webimg"):
    THUMB_SIZE = 40, 40
    import os
    if not os.path.exists(subdir): os.makedirs(subdir)
    if not os.path.exists(webdir): os.makedirs(webdir)
    
    Indexfile = subdir+'/culled_index.json'
    with open (Indexfile) as j:
        img_index = json.load(j)
        j.close()

    src_dir  = subdir+'/'
    save_dir = webdir+'/'

    img_index_web = {}
    for pic_num, item in enumerate (img_index):
        pic_str = "%05d" % (pic_num,) # five-digit leading zeros
        print "pic_num\t", pic_str
        filename = src_dir + item['filename']
        IMG = Image.open(filename)
        if IMG.mode != "RGBA":  IMG = IMG.convert("RGBA")
        # calculate some values, add to your index
        item['rgb-avg'] = calc_rgb_avg(IMG)
        print "average RGB\t", item['rgb-avg']
        # do more stuff 
        #websize Image 
        print "image dimensions: \t", IMG.size
        img_wh = IMG.size
        img_w, img_h = float(img_wh[0]), float(img_wh[1])
        sqs = 450
        if (img_w or img_h > sqs):
            if (img_w > img_h) : size = sqs, int(sqs*img_h/img_w)
            else : size = int(sqs*img_w/img_h), sqs
        elif(img_w and img_h <sqs):
            if (img_w > img_h) : size = sqs, int(sqs*img_h/img_w)
            else : size = int(sqs*img_w/img_h), sqs
        print "resize dimensions: \t", size
        IMG = IMG.resize(size, Image.ANTIALIAS)
        #re-name and save
        item['filename'] = pic_str + '.jpg'
        filepath = save_dir + pic_str + '.jpg'
        print "saving file to\t", filepath
        IMG.save(filepath, "JPEG") 
        #close IMG
        #IMG.close()
        
        # MAKE THUMBNAIL
        print "making thumbnail"
        width, height = IMG.size
        
        if width > height:
           delta = width - height
           left = int(delta/2)
           upper = 0
           right = height + left
           lower = height
        else:
           delta = height - width
           left = 0
           upper = int(delta/2)
           right = width
           lower = width + upper

        IMG = IMG.crop((left, upper, right, lower))
        IMG.thumbnail(THUMB_SIZE, Image.ANTIALIAS)
        filepath = save_dir + pic_str + '_th.jpg'
        IMG.save(filepath, "JPEG") 
        item['filename_th'] = filepath
        
        img_index_web[pic_str] = item
        

    new_filename = webdir+'/web_index.json'
    #overwrite file with new information
    with open (new_filename, 'w') as k:
        k.write(json.dumps(img_index_web, indent=2))
        k.close()