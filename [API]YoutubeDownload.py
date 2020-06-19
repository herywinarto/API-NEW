import requests, json

def YoutubeSearch():
    apiKey = input("Your API key: ")
    search = input("Your Search Query: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/ytdl?search="+search,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def YoutubeURL():
    apiKey = input("Your API key: ")
    url = input("Your TikTok URL: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/ytdl?url="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))


YoutubeSearch()
