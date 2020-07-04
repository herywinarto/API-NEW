import requests, json

def GoogleDriveUpload():
    apiKey = "YOUR_APIKEY_HERE"
    path = "./img.jgp" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    files = {"file": open(path,"rb")}
    main = json.loads(requests.post("https://api.be-team.me/gdrive",headers=headers,files=files).text)
    print("Link: "+ main["result"])

GoogleDriveUpload()
