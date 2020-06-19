import requests, json

### EFECT LIST ONE ###
def PhotoFunia1():
    category_list = ['concrete-jungle', 'at-the-gallery', 'halloween-pumpkins', 'harley-davidson', 'the-frame', 'vintage-scooter', 'card-with-flowers', 'giant-artwork', 'explorer-drawing', 'at-the-beach', 'in-the-woods', 'shopping-arcade', 'art-admirer', 'sketch-practicing', 'passage', 'travellers-sketch', 'mirror', 'ink-portrait', 'truck-advert', 'girl-with-bicycle', 'easter-flowers', 'easter-frame', 'puppy-with-frame', 'city-billboard', 'underground-poster', 'sparklers', 'famous-gallery', 'burning-fire', 'autumn-frame', 'tablet', 'black-and-white-mural', 'vintage-photos', 'art-experts', 'scroll', 'worker-by-the-billboard', 'old-camera', 'tokyo-crossing', 'in-the-cinema', 'spring-flowers', 'latte-art', 'love-letter', 'wall-poster', 'skydiver', 'national-gallery-in-london', 'watercolour-painting', 'summoning-spirits', 'stadium', 'coloured-pencils', 'piccadilly-arcade', 'drawing-photo', 'artistic-filter', 'winter-princess', 'train-station-poster', 'knight-with-sword', 'football-field', 'rainy-night', 'bunnies', 'roses-and-marshmallows', 'playful-cat', 'wall-mural', 'gallery-visitor', 'equestrienne', 'new-year-frames', 'ghostwood', 'frankenstein-monster', 'brass-frame', 'red-and-blue', 'painting-and-sketches', 'new-york-street', 'wedding-day', 'vhs', 'passing-by-the-painting', 'lemon-tree', 'evening-billboard', 'kitty-and-frame', 'pedestrian-crossing', 'press_conference', 'picture_at_the_gallery', 'on_the_mountain', 'building_painters', 'replacing_billboard_advert', 'warrior', 'heart_locket', 'painter_at_work', 'galeries_lafayette', 'mermaid', 'goats', 'golden_valentine', 'london_calling', 'drawing_near_the_sea', 'ornament', 'indian_beauty', 'apples', 'spring_memories', 'brugge', 'medieval_art', 'cappuccino', 'modern_art_exhibition', 'louvre', 'watercolours', 'woman_pilot', 'vintage_table', 'pavement_artist', 'bicycle', 'bunny_ears', 'crooked_gambler', 'frame_and_roses', 'crown', 'oxford', 'midnight_billboard', 'pisa_street', 'pictures_sale', 'citylight', 'film_scan', 'knight', 'picadilly_circus', 'graffiti_billboard', 'romantic_etude', 'broadway', 'yellow_wall', 'the_first_man_on_the_moon', 'large_painting', 'mint_frame', 'night_street', 'boardings', 'portrait_on_the_wall', 'easter', 'impressionists', 'biker', 'snow_in_london', 'vintage_frame', 'family_in_museum', 'museum_kid', 'oil_painting', 'xmas_tree', 'marilyn_autograph', 'graffiti_wall', 'graffiti_artist', 'pumpkins', 'lavander', 'fire', 'truck', 'obama', 'roses', 'late_autumn', 'graffiti', 'riverside_billboard', 'stacco', 'etude', 'surfer', 'ny_taxis', 'chinese_opera', 'sidewalk', 'the_kiss', 'snowboard', 'mysterious_painting', 'prince_of_wales_theatre', 'sphinx', 'swedish_billboard', 'witch', 'nyc', 'art_gallery', 'city', 'dj', 'the_gun', 'tulips', 'flower_frame', 'male_gambler', 'female_gambler', 'artist', 'last_advert', 'lego_portrait', 'bride_in_grass', 'cafe', 'ax', 'artist_in_the_dark', 'hammock', 'goalkeeper', 'billboard_workers', 'huge_billboard', 'ophelia', 'leftfield', 'pavement_art', 'osaka', 'hockey_team', 'street_artist', 'watercolor', 'drawing', 'night_ride', 'frosty_window', 'girls_with_poster', 'watchinng', '100_dollars', 'puzzle', 'pastel', 'library', 'twilight', 'urban_billboard', 'glass', 'singer', 'bodybuilder', 'female_soldier', 'cupid', 'night_walk', 'icecream', 'rainy_day', 'urban', 'odessa_opera_house', 'hockey', 'captivity', 'local_shop', 'tram', 'ethanol', 'taipei', 'jigsaw_puzzle', 'mount_rushmore', 'lego', 'stencil', 'esquire', 'glamour', 'galatea', 'reproduction', 'godfather', 'death_proof', 'coffee_break', 'chris_pirillo', 'old_book', 'shop_poster', 'retail_park', 'purple_sky', 'warhol', 'special_billboard', 'yo', 'reflection', 'wall_painting', 'bride', 'tv_girl', 'mini_cooper', 'lenin', 'reconstruction', 'two_cats', 'superman', 'frame', 'street_exhibition', 'wall', 'night', 'pilot', 'pavement_drawing', 'applying_makeup', 'polaroid_dress', 'torn_billboard', 'kitty', 'portrait', 'eye', 'posters', 'night_city', 'bad_santa', 'christmass_tree_balls', 'good_luck_chuck', 'paris_hilton', 'cinema', 'wall_banner', 'gas_mask_freaks', 'marilyn_monroe', 'two_female_fans', 'wanted_wizard', 'on_the_moon', 'art_exhibition', 'train_station', 'museum', 'madonna', 'mona_lisa', 'vogue', 'dollar', 'art_painting', 'behind_the_fence', 'newspaper', 'castle', 'angry_granny', 'victoria_beckham', 'putin', 'perfume_shop', 'billboard', 'shopping_center']
    apiKey = input("Your API key: ")
    print(category_list)
    category = input("Insert Category: ")
    if category not in category_list:
        raise Exception("Wrong Category")
    url = input("Insert Your Image Link: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/photofunia1?category="+category+"&url="+url,headers=headers).text)
    print("Link Image: "+main["result"]["image"])
    print("Animated: "+str(main["result"]["animated"]))

### EFECT LIST TWO ###
def PhotoFunia2():
    category_list = ['christmas-writing', 'beach-sign', 'yacht', 'water-writing', 'bracelet', 'light-graffiti', 'street-sign', 'cemetery-gates', 'plane-banner', 'love-lock', 'fortune-cookie', 'frosty-window-writing', 'einstein', 'lipstick-writing', 'typewriter', 'soup_letters', 'cookies_writing', 'blood_writing', 'wooden_sign', 'sand_writing']
    apiKey = input("Your API key: ")
    print(category_list)
    category = input("Insert Category: ")
    if category not in category_list:
        raise Exception("Wrong Category")
    text = input("Insert Your Text: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/photofunia2?category="+category+"&text="+text,headers=headers).text)
    print("Link Image: "+main["result"]["image"])


### EFECT LIST THREE ###
def PhotoFunia3():
    category_list = ['broadway-at-night', 'painter', 'festive-days', 'old-tram', 'bronze-frames', 'urban-billboard', 'billboards-at-night', 'shop-posters', 'campaign', 'two-girls', 'antique_shop', 'art_book', 'two_citylights', 'brooches', 'queens_theatre', 'painter_on_the_bridge', 'streets_of_new_york', 'on_the_roof', 'copying_masterpiece', 'taxis_on_times_square', 'summer_love', 'reading', 'photo_exhibition', 'football_players', 'developing_photos', 'night_square', 'couple', 'underground', 'brad_pitt', 'times_square', 'smart_kitty', 'broken_glass', 'brick_wall', 'stamps', 'modern_art']
    apiKey = input("Your API key: ")
    print(category_list)
    category = input("Insert Category: ")
    if category not in category_list:
        raise Exception("Wrong Category")
    url1 = input("Insert Your Image Link: ")
    url2 = input("Insert Your Second Image Link: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/photofunia3?category="+category+"&url1="+url1+"&url2="+url2,headers=headers).text)
    print("Link Image: "+main["result"]["image"])
    print("Animated: "+str(main["result"]["animated"]))

### EFECT LIST FOUR ###
def PhotoFunia4():
    category_list = ['morning-newspaper', 'easter-greetings', 'christmas-diary', 'activists', 'coffee-and-tulips', 'night-street', 'travellers-diary', 'festive-greetings', 'xmas-time', 'vinyl-store', 'easter-nest', 'travelers-suitcase', 'hanging-billboard', 'easter-card', 'santas-parcel-picture', 'double-decker', 'book_lover', 'new_world', 'quill', 'easter_postcard', 'daffodils', 'memories_of_paris', 'making_tattoo', 'instant_camera', 'another_magazine', 'pink_heart', 'new_year_presents', 'miss', 'affiche', 'rounded_billboard', 'hand_lens', 'vintage_photo', 'volunteer', 'valentine', 'coin', 'macho', 'guilty', 'music_shop']
    apiKey = input("Your API key: ")
    print(category_list)
    category = input("Insert Category: ")
    if category not in category_list:
        raise Exception("Wrong Category")
    url = input("Insert Your Image Link: ")
    text = input("Insert Your Text: ")
    headers = {"apiKey": apiKey} ## APIKEY, YOU CAN BUY FROM ME IN WHATSAPP: +6289625658302
    main = json.loads(requests.get("https://api.be-team.me/photofunia4?category="+category+"&text="+text+"&url="+url,headers=headers).text)
    print("Link Image: "+main["result"]["image"])
    print("Animated: "+str(main["result"]["animated"]))
    
PhotoFunia2()
