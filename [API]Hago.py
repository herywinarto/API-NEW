import requests, json

def HagoUserID():
    apiKey = "YOUR_APIKEY_HERE"
    userId = "hery" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/hago?userid="+userId,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

HagoUserID()
