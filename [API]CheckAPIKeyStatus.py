import requests, json

def APIKeyStatus():
    apiKey = "YOUR_APIKEY_HERE"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/apikey",headers=headers).text)
    print("Expired: "+main["result"]["expired"])
    print("Usage: "+main["result"]["usage"])
    print("IsActive: "+str(main["result"]["isActive"]))
    print("IsLimit: "+str(main["result"]["isLimit"]))
    print("IsVIP: "+str(main["result"]["isVIP"]))
    print("UsageRestartDate: "+main["result"]["restartTime"])

APIKeyStatus()
