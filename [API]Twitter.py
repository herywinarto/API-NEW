import requests, json

def twitterProfile():
    apiKey = "YOUR_APIKEY_HERE"
    userId = "@animecentral" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/twitter?userid="+userId,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def twitterPost():
    apiKey = "YOUR_APIKEY_HERE"
    url = "https://twitter.com/jus_v1b1n/status/1323853844187668480" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/twitter?url="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))


twitterPost()
