import glob, json, colorsys
from PIL import Image, ImageDraw

def collate():
    #Collate.py looks at a culled image folder and the available index jsons and creates a new master json.
    import glob, json, re

    #new dict add {"filename": filename}
    #load all the img names into an array
    dir = "Images/*"

    Filenames = [g[7:] for g in (glob.glob(dir))]
    IndexFilenames = [j for j in glob.glob('*.json') if ('ErrorReport' , 'Collated' not in j)]
    Indices_Collated = []
    Indices_Culled = []

    for ifilename in IndexFilenames:
        with open (ifilename) as json_file:
            index_items = json.load(json_file)
            json_file.close()
        [Indices_Collated.append(i) for i in index_items]

    print len (Indices_Collated)
    print len (Filenames)

    for filename in Filenames:
        #print filename
        namechunks = re.split('_', filename)
        #print namechunks
        type = unicode(namechunks[0])
        keyword = unicode(namechunks[1])
        id = unicode(namechunks[2].translate(None, 'jpgifnbmeJPGIFNBME.'))
        #print id
        
        for c in Indices_Collated:
            if (c['type'] == type and c['keyword'] == keyword and c['id'] == id):
                Indices_Culled.append(c) 
                c['filename'] = filename
    print Indices_Collated[0]
    print len (Indices_Culled)
    with open ('Culled_Index.json', 'w') as json_file:
        json_file.write(json.dumps(Indices_Culled))
        json_file.close()
    

# A variety of image processing functions to be applied to the culled Index

def calc_rgb_avg(im):
    pixels = [im.getpixel((x,y)) for x in range(im.size[0]) for y in range(im.size[1])]
    rgba = [(px[0],px[1],px[2],px[3]) for px in pixels ]
    def wght(tup,idx): return tup[idx] * (tup[3]/255.0)
    rgba_avg = [ sum([wght(tup,n) for tup in rgba])/sum([tup[3]/255.0 for tup in rgba]) for n in range(3)]
    return (int(rgba_avg[0]),int(rgba_avg[1]),int(rgba_avg[2]))

def process_for_web():
    Indexfile = 'Culled_Index.json'
    with open (Indexfile) as j:
        img_index = json.load(j)
        j.close()

    src_dir  = 'Images/'
    save_dir = 'webImages/'

    for pic_num, item in enumerate (img_index):
        print pic_num
        filename = src_dir + item['filename']
        IMG = Image.open(filename)
        if IMG.mode != "RGBA":  IMG = IMG.convert("RGBA")
        # calculate some values, add to your index
        item['rgb-avg'] = calc_rgb_avg(IMG)
        print item['rgb-avg']
        # do more stuff 
        #websize Image 
        print IMG.size
        img_wh = IMG.size
        img_w, img_h = float(img_wh[0]), float(img_wh[1])
        print img_w, ", ", img_h
        sqs = 450
        if (img_w or img_h > sqs):
            if (img_w > img_h) : size = sqs, int(sqs*img_h/img_w)
            else : size = int(sqs*img_w/img_h), sqs
        elif(img_w and img_h <sqs):
            if (img_w > img_h) : size = sqs, int(sqs*img_h/img_w)
            else : size = int(sqs*img_w/img_h), sqs
        print size
        IMG = IMG.resize(size, Image.ANTIALIAS)
        #re-name and save
        pic_str = str(pic_num)
        while (len(pic_str)<4) : pic_str  = '0' + pic_str
        item['filename'] = pic_str + '.jpg'
        filepath = save_dir + pic_str + '.jpg'
        IMG.save(filepath, "JPEG") 
        #close IMG
        IMG.close()


    new_filename = 'Web_Index.json'
    #overwrite file with new information
    with open (new_filename, 'w') as k:
        k.write(json.dumps(img_index))
        k.close()