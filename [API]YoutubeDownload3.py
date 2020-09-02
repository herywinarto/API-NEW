import requests, json

def YoutubeSearch():
    apiKey = "YOUR_APIKEY_HERE"
    search = "Nanairo Symphony" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/ytdl3?search="+search,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def YoutubeURL():
    apiKey = "YOUR_APIKEY_HERE"
    url = "https://www.youtube.com/watch?v=TkV5709EG5M" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/ytdl3?url="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))


YoutubeSearch()
