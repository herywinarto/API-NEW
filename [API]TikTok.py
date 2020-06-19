import requests, json

def TiktokUserID():
    apiKey = input("Your API key: ")
    userId = input("Your User ID: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/tiktok?userid="+userId,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def TiktokUserID():
    apiKey = input("Your API key: ")
    url = input("Your TikTok URL: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/tiktok?userid="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

TiktokUserID()
