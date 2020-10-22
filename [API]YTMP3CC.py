import requests, json


def YtMp3():
    apiKey = "YOUR_APIKEY_HERE"
    url = "https://www.youtube.com/watch?v=TkV5709EG5M" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/ytmp3?url="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))
    
def YtMp4():
    apiKey = "YOUR_APIKEY_HERE"
    url = "https://www.youtube.com/watch?v=TkV5709EG5M" ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/ytmp4?url="+url,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))


YtMp3()
