import requests
__author__      = "Devendra Dora"

def exampleGetRequest(queryParam1):  
  base_url='https://www.google.co.in/search'
  params = {               
               'q': queryParam1,
              # 'queryParam2': "test",                     
            }
  resp = requests.get(base_url, params=params)
  print("url  -> "+resp.url)


if __name__== "__main__":   
      exampleGetRequest("devendra dora")      
      