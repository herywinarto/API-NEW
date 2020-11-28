import requests, json

def swapfaceImage():
    apiKey = "YOUR_APIKEY_HERE"
    url = "https://file.be-team.me/test.jpg" ## EXAMPLE SELFIE
    templateId = "7a07cd2d-2032-49a4-9c42-29004a7a3ff6" ## GETFROM TEMPLATE LIST
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/swapface/image?url="+url+"&id="+templateId,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def swapfaceImagePost():
    apiKey = "YOUR_APIKEY_HERE"
    path = "./img.jpg" ## EXAMPLE
    files = {"file": open(path,"rb")}
    templateId = "7a07cd2d-2032-49a4-9c42-29004a7a3ff6" ## GETFROM TEMPLATE LIST
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.post("https://api.be-team.me/swapface/image?id="+templateId,headers=headers,files=files).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def swapfaceImageListTemplate():
    apiKey = "YOUR_APIKEY_HERE"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/swapface/image/list",headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def swapfaceGif():
    apiKey = "YOUR_APIKEY_HERE"
    url = "https://file.be-team.me/test.jpg" ## EXAMPLE SELFIE
    templateId = "bb44c753-61e1-4674-aaa1-c3081257094f" ## GETFROM TEMPLATE LIST
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/swapface/gif?url="+url+"&id="+templateId,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def swapfaceGifPost():
    apiKey = "YOUR_APIKEY_HERE"
    path = "./img.jpg" ## EXAMPLE
    files = {"file": open(path,"rb")}
    templateId = "bb44c753-61e1-4674-aaa1-c3081257094f" ## GETFROM TEMPLATE LIST
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.post("https://api.be-team.me/swapface/gif?id="+templateId,headers=headers,files=files).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def swapfaceGifListTemplate():
    apiKey = "YOUR_APIKEY_HERE"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/swapface/gif/list",headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def swapfaceVideo():
    apiKey = "YOUR_APIKEY_HERE"
    url = "https://file.be-team.me/test.jpg" ## EXAMPLE SELFIE
    templateId = "5812bb60-7f25-446a-8174-7ab6ae7814b6" ## GETFROM TEMPLATE LIST
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/swapface/video?url="+url+"&id="+templateId,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def swapfaceVideoPost():
    apiKey = "YOUR_APIKEY_HERE"
    path = "./img.jpg" ## EXAMPLE
    files = {"file": open(path,"rb")}
    templateId = "5812bb60-7f25-446a-8174-7ab6ae7814b6" ## GETFROM TEMPLATE LIST
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.post("https://api.be-team.me/swapface/video?&id="+templateId,headers=headers,files=files).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def swapfaceVideoListTemplate():
    apiKey = "YOUR_APIKEY_HERE"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/swapface/video/list",headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

swapfaceImage()
