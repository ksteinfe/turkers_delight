"""
@Wenzhe PENG
pwz@berkeley.edu
"""

def scrape(searchString, limit,brow="firefox",subdir="img"):
    import os
    if not os.path.exists(subdir): os.makedirs(subdir)
    
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from PIL import Image
    import time, requests, json, urllib, math,cStringIO, ast

    # CHANGE WEBDRIVER HERE
    browser = None
    if brow.lower()=="firefox": browser = webdriver.Firefox()
    if brow.lower()=="chrome": browser = webdriver.Chrome()
    if browser == None:
        raise Exception("browser should be set to 'Firefox' or to 'Chrome'")
    
    
    tag = searchString
    url = 'https://www.pinterest.com/search/pins/?rs=ac&len=2&q='+tag
    browser.get(url)
    
    
    scroll_num = math.ceil(limit/30)
    scroll_num = int(scroll_num)
    if (scroll_num > 35): 
        scroll_num = 35
        limited = False
    else:
        limited = True
    
    for n in range(scroll_num):
        time.sleep(3)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    
    carrots = soup.findAll('img', {'class' : 'pinImg'})
    if (limited) : 
        carrots = carrots[:limit]
    
    results = []
    for ind, carrot in enumerate(carrots):
        
        link = "http://"+carrot['src'][8:]
        print link
        id = str(ind)
        item = {"type" : "Pinterest", "keyword": tag, 'id': id.encode('ascii') , 'link': link.encode('ascii'), "retrieved": time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()) }
        results.append(item)
        meta = { "num_results": len(carrots)}
    
    error_report = []

    for result in results:
        address = result['link']
        try:
            print address
            con = urllib.urlopen(address)
            file = cStringIO.StringIO(con.read())
            img = Image.open(file);
            filename = subdir+"/Pinterest_" + tag + "_"  + result['id'] + "." +str(img.format)
            print 'urlretrieve', filename
            urllib.urlretrieve(address,filename)
        except:
            print "error"
            result["visited"] = False
            error_report.append(result)
        else:
            file = None
            con.close()
            result["visited"] = True
    
    if len(error_report)>0:
        print 'ENCOUNTERED ERRORS'
        print error_report
        
    #index_filename = 'Imglist_GI_' + searchterm + '.json'
    index_filename = subdir+'/_imglist_pinterest_' + tag + '.json'

    with open(index_filename, 'w') as j:
        j.write(json.dumps(results, indent = 2))
        j.close()
        
        
    #index_filename = 'Imglist_GI_' + searchterm + '_ErrorReport.json'
    index_filename = subdir+'/_imglist_pinterest_' + tag + '_errors.json'
    with open(index_filename, 'w') as k:
        k.write(json.dumps(error_report, indent = 2))
        k.close()

        
        
if __name__ == "__main__":
    scrape()
