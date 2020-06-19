import requests, json

def ImageReverse():
    apiKey = input("Your API key: ")
    path = input("Your Image Path: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    files = {"file": open(path,"rb")}
    main = json.loads(requests.post("https://api.be-team.me/imgreverse",headers=headers,files=files).text)
    print("Link: "+ main["result"])
    
ImageReverse()
