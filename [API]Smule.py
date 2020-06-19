import requests, json

def SmuleUserID():
    apiKey = input("Your API key: ")
    userId = input("Your User ID: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/smule?userid="+userId,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def SmuleURL():
    apiKey = input("Your API key: ")
    url = input("Your Smule URL: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/smule?url="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))


SmuleURL()
