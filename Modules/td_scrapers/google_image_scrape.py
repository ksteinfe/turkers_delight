def scrape(searchString, limit):
    
    if (limit < 800):
        limited = True
    else :
        limited = False
    print limit
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from PIL import Image
    import time, requests, json, urllib, cStringIO, ast
    browser = webdriver.Firefox()
    searchterm = searchString #what you would put in the search box as a string
    searchcount = "1000" #the number of results you would like as a string
    url = "https://www.google.com/search?q={0}&num={1}&source=lnms&tbm=isch&sa=X".format(searchterm, searchcount)

    browser.get(url)

    #driver = webdriver.Firefox()
    scroll_num = 3
    for n in range(scroll_num):
        time.sleep(10)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        try:
            browser.find_element_by_id("smb").click()
        except:
            break
        

    soup = BeautifulSoup(browser.page_source, 'html.parser')

    carrots = soup.findAll('a', {'class' : 'rg_l'})
    
    if (limited): carrots = carrots[:limit]
    print len(carrots)


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
    print meta
    print results[0]
    error_report = []

    for result in results:
        address = result['link']
        try:
            con = urllib.urlopen(address)
            file = cStringIO.StringIO(con.read())
            img = Image.open(file);
            filename = "Images/Google_" + searchterm + "_"  + result['id'] + "." +str(img.format)
            print filename
            urllib.urlretrieve(address,filename)
        except:
            print "error"
            result["visited"] = False
            error_report.append(result)
        else:
            file = None
            con.close()
            result["visited"] = True
            

    print error_report
    index_filename = 'Imglist_GI_' + searchterm + '.json'

    with open(index_filename, 'w') as j:
        j.write(json.dumps(results))
        j.close()
        
        
    index_filename = 'Imglist_GI_' + searchterm + '_ErrorReport.json'
    with open(index_filename, 'w') as k:
        k.write(json.dumps(error_report))
        k.close()


if __name__ == "__main__":
    scrape()
