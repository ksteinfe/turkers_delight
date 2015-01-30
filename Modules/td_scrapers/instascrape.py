


def scrape(searchString, limit):
    
    
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from PIL import Image
    import time, requests, json, urllib, math

    browser = webdriver.Firefox()
    tag = searchString
    url = 'http://iconosquare.com/tag/'+tag
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

    
    carrots = soup.findAll('a', {'class' : 'lienPhotoGrid'})
    
    if (limited) : 
        carrots = carrots[:limit]
    
    results = []
    for ind, carrot in enumerate(carrots):
        link = 'http://iconosquare.com' + carrot['href']
        id = str(ind)
        item = {"type" : "Instagram", "keyword": tag, 'id': id.encode('ascii') , 'link': link.encode('ascii'), "retrieved": time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()) }
        results.append(item)
        meta = { "num_results": len(carrots)}

    for result in results:
        address = result['link']
        #print address
        other_tags = []
        browser.get(address)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #print 'got'
        #file = r.text
        stew = BeautifulSoup(browser.page_source, 'html.parser')
        #print stew
        #idstring = str(address[25:])
        #print idstring
        Instaimage = stew.findAll('img', {'class' : 'photo-mode-liste photo-flux loaded'})
        #print Instaimage
        if (len(Instaimage) > 0):
            imglink = Instaimage[0]['src']
            #print imglink
        filename = "Images/Instagram_" + tag + "_"  + result['id'] + ".jpg"
        #print filename
        urllib.urlretrieve(imglink,filename)
        onions = stew.findAll('a', {'class' : 'unTag'})
        if (len(onions) > 0):
            for onion in onions:
                link = onion['href']
                other_tag = link[5:]
                other_tags.append(other_tag)
        else:
            other_tags = None
        result['other-tags'] = other_tags
        #thing = sou

        try: 
            longitude = stew.findAll('input', {'class' : 'longitude'})
            print longitude
            latitude = stew.findAll('input', {'class' : 'latitude'})
            print latitude
            location = {'latitude':latitude[0]['value'], 'longitude':longitude[0]['value']}
        except:
            location = None
        result['location'] = location
        try :
            postdate = stew.findAll('span', {'class' : 'pic-created'})
            print postdate
            postdate = postdate[0].text
            print postdate
            
            
        except:
            print "err2"
            postdate = None
        result['post-date'] = postdate

        result['visited'] = True
        time.sleep(4)
            #print "error"
            #result['visited'] = False
        #con.close()


        print meta
        print results[0]
        index_filename = 'Imglist_IG_' + tag + '.json'
        with open(index_filename, 'w') as j:
            j.write(json.dumps(results))
            j.close()
        
        
        
if __name__ == "__main__":
    scrape()
