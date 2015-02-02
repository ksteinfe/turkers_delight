
def scrape(searchString, limit,scroll_num=3,brow="firefox",subdir="img"):
    import os
    if not os.path.exists(subdir): os.makedirs(subdir)
        
    if (limit < 800):
        limited = True
    else :
        limited = False
    print "limiting to ", limit, "results"
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from PIL import Image
    import time, requests, json, urllib, cStringIO, ast
    
    
    # CHANGE WEBDRIVER HERE
    browser = None
    if brow.lower()=="firefox": browser = webdriver.Firefox()
    if brow.lower()=="chrome": browser = webdriver.Chrome()
    if browser == None:
        raise Exception("browser should be set to 'Firefox' or to 'Chrome'")
    
    searchterm = searchString #what you would put in the search box as a string
    searchcount = "1000" #the number of results you would like as a string
    url = "https://www.google.com/search?q={0}&num={1}&source=lnms&tbm=isch&sa=X".format(searchterm, searchcount)

    browser.get(url)

    #driver = webdriver.Firefox()
    for n in range(scroll_num):
        time.sleep(5)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        try:
            browser.find_element_by_id("smb").click()
        except:
            break
        

    soup = BeautifulSoup(browser.page_source, 'html.parser')

    carrots = soup.findAll('a', {'class' : 'rg_l'})
    
    if (limited): carrots = carrots[:limit]
    #print len(carrots)


    results = []
    for ind, carrot in enumerate (carrots):
        link = carrot['href']
        start = link.find('imgurl=') + 7
        link = link[start:]
        end = link.find('&')
        link = link[:end]
        id = str(ind)
        item = {"type" : "Google", "keyword" : searchterm, 'id': id.encode('ascii') , 'link': link.encode('ascii'), "retrieved": time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()), "visited": None}
        results.append(item)
        
    meta = {"num_results": len(carrots)}
    print 'meta: \t', meta
    print 'first result \t', results[0]
    error_report = []

    for result in results:
        address = result['link']
        try:
            con = urllib.urlopen(address)
            file = cStringIO.StringIO(con.read())
            img = Image.open(file);
            filename = subdir+"/Google_" + searchterm + "_"  + result['id'] + "." +str(img.format)
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
    index_filename = subdir+'/_imglist_goog_' + searchterm + '.json'

    with open(index_filename, 'w') as j:
        j.write(json.dumps(results, indent = 2))
        j.close()
        
        
    #index_filename = 'Imglist_GI_' + searchterm + '_ErrorReport.json'
    index_filename = subdir+'/_imglist_goog_' + searchterm + '_errors.json'
    with open(index_filename, 'w') as k:
        k.write(json.dumps(error_report, indent = 2))
        k.close()


if __name__ == "__main__":
    scrape()
