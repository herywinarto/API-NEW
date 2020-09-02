import requests, json

def TiktokURL():
    apiKey = "YOUR_APIKEY_HERE"
    url = "https://www.tiktok.com/@neymarjr/video/6845350696078904582" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/tiktok?url="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

TiktokURL()
