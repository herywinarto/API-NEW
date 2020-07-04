import requests, json

def InstaPost():
    apiKey = "YOUR_APIKEY_HERE"
    url = "https://www.instagram.com/p/CCOdaxxhcA6/" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/instapost?url="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))


InstaPost()
