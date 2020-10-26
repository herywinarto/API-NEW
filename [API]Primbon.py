import requests, json

def primbonNama():
    apiKey = "YOUR_APIKEY_HERE"
    nama = "uzumaki naruto"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/primbon/nama?nama="+nama,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def primbonBintang():
    apiKey = "YOUR_APIKEY_HERE"
    zodiac = "aries"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/primbon/bintang?zodiac="+zodiac,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

def primbonKecocokan():
    apiKey = "YOUR_APIKEY_HERE"
    namaAnda = "sasuke"
    namaPasangan = "sakura"
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/primbon/kecocokan?nama1="+namaAnda+"&nama2="+namaPasangan,headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

primbonKecocokan()
