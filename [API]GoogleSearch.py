import requests, json

def GoogleSearch():
    apiKey = "YOUR_APIKEY_HERE"
    search = "naruto" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/googlesearch?search="+search,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

GoogleSearch()
