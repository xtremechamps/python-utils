#Python3

from flask import  Flask, render_template, flash, request, url_for, redirect, session , Response
import requests,sys,json
from requests_ntlm import HttpNtlmAuth
app = Flask(__name__)

__author__      = "Devendra Dora"

@app.route("/dora/httpWithNTLM",methods=['POST'])
def invokeHTTPReqWithNTLM():
    url =""
    reqData = json.loads(request.data)        
    reqxml=request.data
    headers = {}
    headers["SOAPAction"] = "";
    headers["Content-Type"] = "text/xml"
    headers["Accept"] = "text/xml"
    print("req headers "+str(request.headers))

    r = requests.Request("POST",url,auth=HttpNtlmAuth('domain\\username','password'), data=reqxml, headers=headers) 

    prepared = r.prepare()
    s = requests.Session()
    resp = s.send(prepared)
    print (resp.status_code)
    return Response(resp.text.replace("&lt;","<").replace("&gt;",">"),resp.status_code)




if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001)
