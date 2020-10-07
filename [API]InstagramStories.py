import requests, json

def InstaStories():
    apiKey = "YOUR_APIKEY_HERE"
    userid = "instagram" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/instastories?userid="+userid,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))


InstaStories()
