def APIKeyStatus():
    apiKey = input("Your API key: ")
    headers = {"apiKey": apiKey}
    main = json.loads(requests.get("https://api.be-team.me/apikey",headers=headers).text)
    print("Expired: "+main["result"]["expired"])
    print("Usage: "+main["result"]["usage"])
    print("IsActive: "+main["result"]["isActive"])
    print("IsLimit: "+main["result"]["isLimit"])
    print("IsVIP: "+main["result"]["isVIP"])
    print("UsageRestartDate: "+main["result"]["restartTime"])

APIKeyStatus()
