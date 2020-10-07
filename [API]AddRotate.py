import requests, json


def addRotate():
    apiKey = "YOUR_APIKEY_HERE"
    authToken = "" ## EXAMPLE
    target = "" ## TARGET ADD
    headers = {
        "apiKey": apiKey, ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
        "appName": "IOS\t10.5.2\tiPhone 8\t11.2.5", ## APPNAME, YOU CAN CUSTOMIZE IT (PRIMARY ONLY)
        "authToken": authToken, ## YOUR PRIMARY TOKEN
        "mid": target ## TARGET ADD
        }
    main = json.loads(requests.get("https://api.be-team.me/line_client?act=findAndAddContactsByMid",headers=headers).text)
    if main["status"] != 200:
        print("[ Error ] " + main["reason"])
    else:
        print(main["result"])
    
    
addRotate()
