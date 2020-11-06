import requests, json

def SmuleUserID():
    apiKey = "YOUR_APIKEY_HERE"
    userId = "JeffKraad" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/smule?userid="+userId,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def SmuleURL():
    apiKey = "YOUR_APIKEY_HERE"
    url = "https://www.smule.com/c/1112691877_3200708124" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/smule?url="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def SmulePerformance():
    apiKey = "YOUR_APIKEY_HERE"
    userId = "JeffKraad" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/smule?performance="+userId,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))


SmuleURL()
