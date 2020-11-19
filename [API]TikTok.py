import requests, json

def TiktokURL():
    apiKey = "YOUR_APIKEY_HERE"
    url = "https://www.tiktok.com/@edowardoginting/video/6896459475486526721" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/tiktok?url="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

TiktokURL()
