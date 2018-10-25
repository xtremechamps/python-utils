#Python3
import requests
from bs4 import BeautifulSoup
import json
from multiprocessing import Pool
import sys

__author__      = "Devendra Dora"

def downloadImage(args):
    searchq, imgname = args
    
    payload = {'q': searchq,
               'source':'lnms','tbm':'isch'}
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/59.0.3071.86 Safari/537.36'}
    s = requests.get('http://www.google.com/search',headers=headers,params=payload).text
    soup = BeautifulSoup(s, 'html.parser')
    #print(soup.find_all('img')[0].link.get('data-src'))

    try:
        link = json.loads(soup.find('div', {"id": "rg_s"}).find("div", {"class": "rg_meta notranslate"}).text)["tu"]
        print(searchq, link)        
        r=requests.get(link, headers=headers)
        print("status_code "+str(r.status_code)+" ")
        print("download image "+searchq+"   ->  "+imgname)
        with open("/home/devendradora/Downloads/"+imgname.split("\n")[0]+".jpg",'wb') as f:            
            f.write(r.content)
    except Exception as e:
        print(str(e))
    sys.stdout.flush()

    

if __name__ == '__main__':
   #file = open("data.csv","r")
   #lines = file.readlines()
   # searchname , imageName
   lines=["devendra dora,img1","dileep dora,img2"]
   args = [line.split(",") for line in lines]
   p = Pool(20)
   print(p.map(downloadImage, args))

          
        
    
    
