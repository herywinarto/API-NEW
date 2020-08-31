import requests, json

def cekResi():
    apiKey = "YOUR_APIKEY_HERE"
    listCourier = ['pos', 'wahana', 'jnt', 'sap', 'sicepat', 'jet', 'dse', 'first', 'ninja', 'lion', 'idl', 'rex', 'ide', 'sentral']
    print(listCourier)
    Courier = input("Select Courier: ")
    resiCode = input("Resi Code: ") ## EXAMPLE
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/cekresi?courier={}&resi={}".format(Courier,resiCode),headers=headers).text)
    print(json.dumps(main, indent=4, sort_keys=True))

cekResi()
