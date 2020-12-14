import json, requests

class BEApi():
    def __init__(self, apikey):
        self.host = "https://api.be-team.me"
        self.headers = {"Apikey": apikey}
        self.session = requests.Session()

    def pretyPrintJson(self, djson):
        print(json.dumps(djson, indent=4, sort_keys=True))
        
    def sendPost(self, path, headers=None, data=None, files=None, djson=None):
        if headers:
            headers = {**headers, **self.headers}
        else:
            headers = self.headers
        try:
            r = json.loads(self.session.post(self.host+path,headers=headers,data=data,files=files,json=djson).text)
        except:
            raise Exception("Oops... Like api is down :(")
        if r["status"] != 200:
            raise Exception(str(r))
        return r

    
    def sendGet(self, path, headers=None):
        if headers:
            headers = {**headers, **self.headers}
        else:
            headers = self.headers
        try:  
            r = json.loads(self.session.get(self.host+path,headers=headers).text)
        except:
            raise Exception("Oops... Like api is down :(")
        if r["status"] != 200:
            raise Exception(str(r))
        return r


    ### APIKEY STATUS CHECKER ###
    def checkStatusApikey(self):
        return self.sendGet("/apikey")

    ### WALLPAPER HD ###
    def alphaCodersSearch(self, search, page=1):
        return self.sendGet("/alphacoders?search={}&page={}".format(search,page))

    ### ANIME INDO 1 ###
    def animeIndo1List(self):
        return self.sendGet("/animeindo1/list")
    def animeIndo1Ongoing(self):
        return self.sendGet("/animeindo1/ongoing")
    def animeIndo1Fetch(self, url):
        return self.sendGet(url.replace(self.host,""))

    ### ANIME INDO 2 ###
    def animeIndo2List(self):
        return self.sendGet("/animeindo2/list")
    def animeIndo2Ongoing(self):
        return self.sendGet("/animeindo2/ongoing")
    def animeIndo2Fetch(self, url):
        return self.sendGet(url.replace(self.host,""))
    
    ### ANIME ENGLISH 2 ###
    def animenglishSeries(self):
        return self.sendGet("/animenglish/series")
    def animenglishMovie(self):
        return self.sendGet("/animenglish/movie")

    ### ANIMEXIN ###
    def animexinOngoing(self):
        return self.sendGet("/animexin/ongoing")

    ### AUTHKEY TO PRIMARY CONVERT ###
    def authkeytoprimary(self, authkey):
        return self.sendGet("/authkey2primary?authkey="+authkey)

    ### BRANLY SEARCH ###
    def brainlySearch(self, search):
        return self.sendGet("/brainly?search="+search)

    ### COOKPAD SEARCH ###
    def cookpadSearch(self, search, lang="id"): #[en,id]
        return self.sendGet("/cookpad?search={}&lang={}".format(search,lang))

    ### DANBOORU PAGE ###
    def danbooruPage(self, page=1):
        return self.sendGet("/danbooru?page="+str(page))

    ### DATABASE JSON ###
    def saveDatabaseJson(self, dataJson):
        return self.sendPost("/databasejson",djson=dataJson)
    def getDatabaseJson(self, name):
        return self.sendGet("/databasejson/"+name)

    ### PHOTOFUNIA ###
        # ONE PHOTO PATERN #
    def funia1WithPath(self, category, path):
        categoryFunia1 = ['concrete-jungle', 'at-the-gallery', 'halloween-pumpkins', 'harley-davidson', 'the-frame', 'vintage-scooter', 'card-with-flowers', 'giant-artwork', 'explorer-drawing', 'at-the-beach', 'in-the-woods', 'shopping-arcade', 'art-admirer', 'sketch-practicing', 'passage', 'travellers-sketch', 'mirror', 'ink-portrait', 'truck-advert', 'girl-with-bicycle', 'easter-flowers', 'easter-frame', 'puppy-with-frame', 'city-billboard', 'underground-poster', 'sparklers', 'famous-gallery', 'burning-fire', 'autumn-frame', 'tablet', 'black-and-white-mural', 'vintage-photos', 'art-experts', 'scroll', 'worker-by-the-billboard', 'old-camera', 'tokyo-crossing', 'in-the-cinema', 'spring-flowers', 'latte-art', 'love-letter', 'wall-poster', 'skydiver', 'national-gallery-in-london', 'watercolour-painting', 'summoning-spirits', 'stadium', 'coloured-pencils', 'piccadilly-arcade', 'drawing-photo', 'artistic-filter', 'winter-princess', 'train-station-poster', 'knight-with-sword', 'football-field', 'rainy-night', 'bunnies', 'roses-and-marshmallows', 'playful-cat', 'wall-mural', 'gallery-visitor', 'equestrienne', 'new-year-frames', 'ghostwood', 'frankenstein-monster', 'brass-frame', 'red-and-blue', 'painting-and-sketches', 'new-york-street', 'wedding-day', 'vhs', 'passing-by-the-painting', 'lemon-tree', 'evening-billboard', 'kitty-and-frame', 'pedestrian-crossing', 'press_conference', 'picture_at_the_gallery', 'on_the_mountain', 'building_painters', 'replacing_billboard_advert', 'warrior', 'heart_locket', 'painter_at_work', 'galeries_lafayette', 'mermaid', 'goats', 'golden_valentine', 'london_calling', 'drawing_near_the_sea', 'ornament', 'indian_beauty', 'apples', 'spring_memories', 'brugge', 'medieval_art', 'cappuccino', 'modern_art_exhibition', 'louvre', 'watercolours', 'woman_pilot', 'vintage_table', 'pavement_artist', 'bicycle', 'bunny_ears', 'crooked_gambler', 'frame_and_roses', 'crown', 'oxford', 'midnight_billboard', 'pisa_street', 'pictures_sale', 'citylight', 'film_scan', 'knight', 'picadilly_circus', 'graffiti_billboard', 'romantic_etude', 'broadway', 'yellow_wall', 'the_first_man_on_the_moon', 'large_painting', 'mint_frame', 'night_street', 'boardings', 'portrait_on_the_wall', 'easter', 'impressionists', 'biker', 'snow_in_london', 'vintage_frame', 'family_in_museum', 'museum_kid', 'oil_painting', 'xmas_tree', 'marilyn_autograph', 'graffiti_wall', 'graffiti_artist', 'pumpkins', 'lavander', 'fire', 'truck', 'obama', 'roses', 'late_autumn', 'graffiti', 'riverside_billboard', 'stacco', 'etude', 'surfer', 'ny_taxis', 'chinese_opera', 'sidewalk', 'the_kiss', 'snowboard', 'mysterious_painting', 'prince_of_wales_theatre', 'sphinx', 'swedish_billboard', 'witch', 'nyc', 'art_gallery', 'city', 'dj', 'the_gun', 'tulips', 'flower_frame', 'male_gambler', 'female_gambler', 'artist', 'last_advert', 'lego_portrait', 'bride_in_grass', 'cafe', 'ax', 'artist_in_the_dark', 'hammock', 'goalkeeper', 'billboard_workers', 'huge_billboard', 'ophelia', 'leftfield', 'pavement_art', 'osaka', 'hockey_team', 'street_artist', 'watercolor', 'drawing', 'night_ride', 'frosty_window', 'girls_with_poster', 'watchinng', '100_dollars', 'puzzle', 'pastel', 'library', 'twilight', 'urban_billboard', 'glass', 'singer', 'bodybuilder', 'female_soldier', 'cupid', 'night_walk', 'icecream', 'rainy_day', 'urban', 'odessa_opera_house', 'hockey', 'captivity', 'local_shop', 'tram', 'ethanol', 'taipei', 'jigsaw_puzzle', 'mount_rushmore', 'lego', 'stencil', 'esquire', 'glamour', 'galatea', 'reproduction', 'godfather', 'death_proof', 'coffee_break', 'chris_pirillo', 'old_book', 'shop_poster', 'retail_park', 'purple_sky', 'warhol', 'special_billboard', 'yo', 'reflection', 'wall_painting', 'bride', 'tv_girl', 'mini_cooper', 'lenin', 'reconstruction', 'two_cats', 'superman', 'frame', 'street_exhibition', 'wall', 'night', 'pilot', 'pavement_drawing', 'applying_makeup', 'polaroid_dress', 'torn_billboard', 'kitty', 'portrait', 'eye', 'posters', 'night_city', 'bad_santa', 'christmass_tree_balls', 'good_luck_chuck', 'paris_hilton', 'cinema', 'wall_banner', 'gas_mask_freaks', 'marilyn_monroe', 'two_female_fans', 'wanted_wizard', 'on_the_moon', 'art_exhibition', 'train_station', 'museum', 'madonna', 'mona_lisa', 'vogue', 'dollar', 'art_painting', 'behind_the_fence', 'newspaper', 'castle', 'angry_granny', 'victoria_beckham', 'putin', 'perfume_shop', 'billboard', 'shopping_center']
        if category not in categoryFunia1:
            raise Exception("Category funia1 not found...")
        return self.sendPost("/photofunia1?category="+category,files={"file": open(path,"rb")})
    def funia1WithUrl(self, category, url):
        categoryFunia1 = ['concrete-jungle', 'at-the-gallery', 'halloween-pumpkins', 'harley-davidson', 'the-frame', 'vintage-scooter', 'card-with-flowers', 'giant-artwork', 'explorer-drawing', 'at-the-beach', 'in-the-woods', 'shopping-arcade', 'art-admirer', 'sketch-practicing', 'passage', 'travellers-sketch', 'mirror', 'ink-portrait', 'truck-advert', 'girl-with-bicycle', 'easter-flowers', 'easter-frame', 'puppy-with-frame', 'city-billboard', 'underground-poster', 'sparklers', 'famous-gallery', 'burning-fire', 'autumn-frame', 'tablet', 'black-and-white-mural', 'vintage-photos', 'art-experts', 'scroll', 'worker-by-the-billboard', 'old-camera', 'tokyo-crossing', 'in-the-cinema', 'spring-flowers', 'latte-art', 'love-letter', 'wall-poster', 'skydiver', 'national-gallery-in-london', 'watercolour-painting', 'summoning-spirits', 'stadium', 'coloured-pencils', 'piccadilly-arcade', 'drawing-photo', 'artistic-filter', 'winter-princess', 'train-station-poster', 'knight-with-sword', 'football-field', 'rainy-night', 'bunnies', 'roses-and-marshmallows', 'playful-cat', 'wall-mural', 'gallery-visitor', 'equestrienne', 'new-year-frames', 'ghostwood', 'frankenstein-monster', 'brass-frame', 'red-and-blue', 'painting-and-sketches', 'new-york-street', 'wedding-day', 'vhs', 'passing-by-the-painting', 'lemon-tree', 'evening-billboard', 'kitty-and-frame', 'pedestrian-crossing', 'press_conference', 'picture_at_the_gallery', 'on_the_mountain', 'building_painters', 'replacing_billboard_advert', 'warrior', 'heart_locket', 'painter_at_work', 'galeries_lafayette', 'mermaid', 'goats', 'golden_valentine', 'london_calling', 'drawing_near_the_sea', 'ornament', 'indian_beauty', 'apples', 'spring_memories', 'brugge', 'medieval_art', 'cappuccino', 'modern_art_exhibition', 'louvre', 'watercolours', 'woman_pilot', 'vintage_table', 'pavement_artist', 'bicycle', 'bunny_ears', 'crooked_gambler', 'frame_and_roses', 'crown', 'oxford', 'midnight_billboard', 'pisa_street', 'pictures_sale', 'citylight', 'film_scan', 'knight', 'picadilly_circus', 'graffiti_billboard', 'romantic_etude', 'broadway', 'yellow_wall', 'the_first_man_on_the_moon', 'large_painting', 'mint_frame', 'night_street', 'boardings', 'portrait_on_the_wall', 'easter', 'impressionists', 'biker', 'snow_in_london', 'vintage_frame', 'family_in_museum', 'museum_kid', 'oil_painting', 'xmas_tree', 'marilyn_autograph', 'graffiti_wall', 'graffiti_artist', 'pumpkins', 'lavander', 'fire', 'truck', 'obama', 'roses', 'late_autumn', 'graffiti', 'riverside_billboard', 'stacco', 'etude', 'surfer', 'ny_taxis', 'chinese_opera', 'sidewalk', 'the_kiss', 'snowboard', 'mysterious_painting', 'prince_of_wales_theatre', 'sphinx', 'swedish_billboard', 'witch', 'nyc', 'art_gallery', 'city', 'dj', 'the_gun', 'tulips', 'flower_frame', 'male_gambler', 'female_gambler', 'artist', 'last_advert', 'lego_portrait', 'bride_in_grass', 'cafe', 'ax', 'artist_in_the_dark', 'hammock', 'goalkeeper', 'billboard_workers', 'huge_billboard', 'ophelia', 'leftfield', 'pavement_art', 'osaka', 'hockey_team', 'street_artist', 'watercolor', 'drawing', 'night_ride', 'frosty_window', 'girls_with_poster', 'watchinng', '100_dollars', 'puzzle', 'pastel', 'library', 'twilight', 'urban_billboard', 'glass', 'singer', 'bodybuilder', 'female_soldier', 'cupid', 'night_walk', 'icecream', 'rainy_day', 'urban', 'odessa_opera_house', 'hockey', 'captivity', 'local_shop', 'tram', 'ethanol', 'taipei', 'jigsaw_puzzle', 'mount_rushmore', 'lego', 'stencil', 'esquire', 'glamour', 'galatea', 'reproduction', 'godfather', 'death_proof', 'coffee_break', 'chris_pirillo', 'old_book', 'shop_poster', 'retail_park', 'purple_sky', 'warhol', 'special_billboard', 'yo', 'reflection', 'wall_painting', 'bride', 'tv_girl', 'mini_cooper', 'lenin', 'reconstruction', 'two_cats', 'superman', 'frame', 'street_exhibition', 'wall', 'night', 'pilot', 'pavement_drawing', 'applying_makeup', 'polaroid_dress', 'torn_billboard', 'kitty', 'portrait', 'eye', 'posters', 'night_city', 'bad_santa', 'christmass_tree_balls', 'good_luck_chuck', 'paris_hilton', 'cinema', 'wall_banner', 'gas_mask_freaks', 'marilyn_monroe', 'two_female_fans', 'wanted_wizard', 'on_the_moon', 'art_exhibition', 'train_station', 'museum', 'madonna', 'mona_lisa', 'vogue', 'dollar', 'art_painting', 'behind_the_fence', 'newspaper', 'castle', 'angry_granny', 'victoria_beckham', 'putin', 'perfume_shop', 'billboard', 'shopping_center']
        if category not in categoryFunia1:
            raise Exception("Category funia1 not found...")
        return self.sendGet("/photofunia1?category={}&url={}".format(category,url))
        # TEXT PATERN #
    def funia2Text(self, category, text):   
        categoryFunia2 = ['christmas-writing', 'beach-sign', 'yacht', 'water-writing', 'bracelet', 'light-graffiti', 'street-sign', 'cemetery-gates', 'plane-banner', 'love-lock', 'fortune-cookie', 'frosty-window-writing', 'einstein', 'lipstick-writing', 'typewriter', 'soup_letters', 'cookies_writing', 'blood_writing', 'wooden_sign', 'sand_writing']
        if category not in categoryFunia2:
            raise Exception("Category funia2 not found...")
        return self.sendGet("/photofunia2?category={}&text={}".format(category,text))
        # TWO PHOTO PATERN #
    def funia3WithPath(self, category, path1, path2):
        categoryFunia3 = ['broadway-at-night', 'painter', 'festive-days', 'old-tram', 'bronze-frames', 'urban-billboard', 'billboards-at-night', 'shop-posters', 'campaign', 'two-girls', 'antique_shop', 'art_book', 'two_citylights', 'brooches', 'queens_theatre', 'painter_on_the_bridge', 'streets_of_new_york', 'on_the_roof', 'copying_masterpiece', 'taxis_on_times_square', 'summer_love', 'reading', 'photo_exhibition', 'football_players', 'developing_photos', 'night_square', 'couple', 'underground', 'brad_pitt', 'times_square', 'smart_kitty', 'broken_glass', 'brick_wall', 'stamps', 'modern_art']
        if category not in categoryFunia3:
            raise Exception("Category funia3 not found...")
        return self.sendPost("/photofunia3?category="+category,files={"file1": open(path1,"rb"),"file2": open(path2,"rb")})
    def funia3WithUrl(self, category, url1, url2):
        categoryFunia3 = ['broadway-at-night', 'painter', 'festive-days', 'old-tram', 'bronze-frames', 'urban-billboard', 'billboards-at-night', 'shop-posters', 'campaign', 'two-girls', 'antique_shop', 'art_book', 'two_citylights', 'brooches', 'queens_theatre', 'painter_on_the_bridge', 'streets_of_new_york', 'on_the_roof', 'copying_masterpiece', 'taxis_on_times_square', 'summer_love', 'reading', 'photo_exhibition', 'football_players', 'developing_photos', 'night_square', 'couple', 'underground', 'brad_pitt', 'times_square', 'smart_kitty', 'broken_glass', 'brick_wall', 'stamps', 'modern_art']
        if category not in categoryFunia3:
            raise Exception("Category funia3 not found...")
        return self.sendGet("/photofunia3?category={}&url1={}&url2=".format(category,url1,url2))
        # ONE PHOTO WITH TEXT PATERN #
    def funia4WithPath(self, category, text, path):   
        categoryFunia4 = ['morning-newspaper', 'easter-greetings', 'christmas-diary', 'activists', 'coffee-and-tulips', 'night-street', 'travellers-diary', 'festive-greetings', 'xmas-time', 'vinyl-store', 'easter-nest', 'travelers-suitcase', 'hanging-billboard', 'easter-card', 'santas-parcel-picture', 'double-decker', 'book_lover', 'new_world', 'quill', 'easter_postcard', 'daffodils', 'memories_of_paris', 'making_tattoo', 'instant_camera', 'another_magazine', 'pink_heart', 'new_year_presents', 'miss', 'affiche', 'rounded_billboard', 'hand_lens', 'vintage_photo', 'volunteer', 'valentine', 'coin', 'macho', 'guilty', 'music_shop']
        if category not in categoryFunia4:
            raise Exception("Category funia4 not found...")
        return self.sendPost("/photofunia4?category={}&text={}".format(category,text),files={"file": open(path,"rb")})
    def funia4WithUrl(self, category, text, url):   
        categoryFunia4 = ['morning-newspaper', 'easter-greetings', 'christmas-diary', 'activists', 'coffee-and-tulips', 'night-street', 'travellers-diary', 'festive-greetings', 'xmas-time', 'vinyl-store', 'easter-nest', 'travelers-suitcase', 'hanging-billboard', 'easter-card', 'santas-parcel-picture', 'double-decker', 'book_lover', 'new_world', 'quill', 'easter_postcard', 'daffodils', 'memories_of_paris', 'making_tattoo', 'instant_camera', 'another_magazine', 'pink_heart', 'new_year_presents', 'miss', 'affiche', 'rounded_billboard', 'hand_lens', 'vintage_photo', 'volunteer', 'valentine', 'coin', 'macho', 'guilty', 'music_shop']
        if category not in categoryFunia4:
            raise Exception("Category funia4 not found...")
        return self.sendGet("/photofunia4?category={}&text={}&url={}".format(category,text,url))

    ### GIF SEARCH ###
    def gifSearch(self, search):
        return self.sendGet("/gif_search?search="+search)

    ### GOOGLE IMAGE ###
    def googleImage(self, search, page=1):
        return self.sendGet("/googleimg?search="+search)

    ### GOOGLE SEARCH ###
    def googleSearch(self, search, page=1):
        return self.sendGet("/googlesearch?search={}&page={}".format(search,page))

    ### HAGO PROFILE SEARCH ###
    def hagoProfileSearch(self, userid): 
        return self.sendGet("/hago?userid="+userid)

    ### IMAGEREVERSE ###
    def imageReverseWithUrl(self, url): 
        return self.sendGet("/imgreverse?url="+url)
    def imageReverseWithPath(self, path): 
        return self.sendPost("/imgreverse",files={"file": open(path,"rb")})

    ### INSTAGRAM ###
        # POST #
    def instaPost(self, url): 
        return self.sendGet("/instapost?url="+url)
        # PROFILE #
    def instaProfile(self, userid): 
        return self.sendGet("/instaprofile?userid="+userid)
        # STORY #
    def instaStory(self, userid): 
        return self.sendGet("/instastory?userid="+userid)
        # TV #
    def instaTv(self, url): 
        return self.sendGet("/instapost?url="+url)
        # HIGHLIGHT #
    def instaHighlight(self, userid): 
        return self.sendGet("/instahighlight?userid="+userid)

    ### JOOX DOWNLOAD ###
    def jooxSearch(self, search):
        return self.sendGet("/joox?search="+search)
    def jooxDownloadWithId(self, id_song):
        return self.sendGet("/joox?id="+id_song)

    ### NINE GAG ###
    def nineGagFresh(self, category):
        categoryList = ['funny', 'among-us', 'animals', 'anime-manga', 'animewaifu', 'animewallpaper', 'apexlegends', 'ask9gag', 'awesome', 'car', 'comic-webtoon', 'coronavirus', 'cosplay', 'countryballs', 'home-living', 'crappydesign', 'cyberpunk2077', 'drawing-diy-crafts', 'rate-my-outfit', 'food-drinks', 'football', 'fortnite', 'got', 'gaming', 'gif', 'girl', 'girlcelebrity', 'guy', 'history', 'horror', 'kpop', 'timely', 'leagueoflegends', 'lego', 'superhero', 'meme', 'movie-tv', 'music', 'basketball', 'nsfw', 'overwatch', 'pcmr', 'pokemon', 'politics', 'pubg', 'random', 'relationship', 'savage', 'satisfying', 'science-tech', 'sport', 'starwars', 'school', 'travel-photography', 'video', 'wallpaper', 'warhammer', 'wholesome', 'wtf', 'darkhumor', 'funny', 'nsfw', 'girl', 'wtf', 'anime-manga', 'random', 'animals', 'animewaifu', 'awesome', 'car', 'comic-webtoon', 'cosplay', 'cyberpunk2077', 'gaming', 'gif', 'girlcelebrity', 'leagueoflegends', 'meme', 'politics', 'relationship', 'savage', 'video', 'algeria', 'argentina', 'australia', 'austria', 'bosniaherzegovina', 'bahrain', 'belgium', 'bolivia', 'brazil', 'bulgaria', 'canada', 'chile', 'colombia', 'costarica', 'croatia', 'cyprus', 'czechia', 'denmark', 'dominicanrepublic', 'ecuador', 'egypt', 'estonia', 'finland', 'france', 'georgia', 'germany', 'ghana', 'greece', 'guatemala', 'hongkong', 'hungary', 'iceland', 'india', 'indonesia', 'iraq', 'ireland', 'israel', 'italy', 'japan', 'jordan', 'kenya', 'kuwait', 'latvia', 'lebanon', 'lithuania', 'luxembourg', 'malaysia', 'mexico', 'montenegro', 'morocco', 'nepal', 'netherlands', 'newzealand', 'nigeria', 'norway', 'oman', 'pakistan', 'peru', 'philippines', 'poland', 'portugal', 'puertorico', 'qatar', 'romania', 'russia', 'saudiarabia', 'senegal', 'serbia', 'singapore', 'slovakia', 'slovenia', 'southafrica', 'southkorea', 'spain', 'srilanka', 'sweden', 'switzerland', 'taiwan', 'tanzania', 'thailand', 'tunisia', 'turkey', 'uae', 'usa', 'ukraine', 'uk', 'uruguay', 'vietnam', 'yemen', 'zimbabwe']
        if category not in categoryList:
            raise Exception("Category 9gag not found...")
        return self.sendGet("/9gag/hot?category="+category)
    def nineGagHot(self, category):
        categoryList = ['funny', 'among-us', 'animals', 'anime-manga', 'animewaifu', 'animewallpaper', 'apexlegends', 'ask9gag', 'awesome', 'car', 'comic-webtoon', 'coronavirus', 'cosplay', 'countryballs', 'home-living', 'crappydesign', 'cyberpunk2077', 'drawing-diy-crafts', 'rate-my-outfit', 'food-drinks', 'football', 'fortnite', 'got', 'gaming', 'gif', 'girl', 'girlcelebrity', 'guy', 'history', 'horror', 'kpop', 'timely', 'leagueoflegends', 'lego', 'superhero', 'meme', 'movie-tv', 'music', 'basketball', 'nsfw', 'overwatch', 'pcmr', 'pokemon', 'politics', 'pubg', 'random', 'relationship', 'savage', 'satisfying', 'science-tech', 'sport', 'starwars', 'school', 'travel-photography', 'video', 'wallpaper', 'warhammer', 'wholesome', 'wtf', 'darkhumor', 'funny', 'nsfw', 'girl', 'wtf', 'anime-manga', 'random', 'animals', 'animewaifu', 'awesome', 'car', 'comic-webtoon', 'cosplay', 'cyberpunk2077', 'gaming', 'gif', 'girlcelebrity', 'leagueoflegends', 'meme', 'politics', 'relationship', 'savage', 'video', 'algeria', 'argentina', 'australia', 'austria', 'bosniaherzegovina', 'bahrain', 'belgium', 'bolivia', 'brazil', 'bulgaria', 'canada', 'chile', 'colombia', 'costarica', 'croatia', 'cyprus', 'czechia', 'denmark', 'dominicanrepublic', 'ecuador', 'egypt', 'estonia', 'finland', 'france', 'georgia', 'germany', 'ghana', 'greece', 'guatemala', 'hongkong', 'hungary', 'iceland', 'india', 'indonesia', 'iraq', 'ireland', 'israel', 'italy', 'japan', 'jordan', 'kenya', 'kuwait', 'latvia', 'lebanon', 'lithuania', 'luxembourg', 'malaysia', 'mexico', 'montenegro', 'morocco', 'nepal', 'netherlands', 'newzealand', 'nigeria', 'norway', 'oman', 'pakistan', 'peru', 'philippines', 'poland', 'portugal', 'puertorico', 'qatar', 'romania', 'russia', 'saudiarabia', 'senegal', 'serbia', 'singapore', 'slovakia', 'slovenia', 'southafrica', 'southkorea', 'spain', 'srilanka', 'sweden', 'switzerland', 'taiwan', 'tanzania', 'thailand', 'tunisia', 'turkey', 'uae', 'usa', 'ukraine', 'uk', 'uruguay', 'vietnam', 'yemen', 'zimbabwe']
        if category not in categoryList:
            raise Exception("Category 9gag not found...")
        return self.sendGet("/9gag/fresh?category="+category)

    ### ONE CAK RANDOM ###
    def oneCakRandom(self):
        return self.sendGet("/1cak")

    ### ROTATE PRIMARY TO SECONDARY CONVERT ###
    def primarytosecondary(self, authToken, sysname="BE-Team", appName="IOSIPAD\t10.5.2\tiPhone 8\t11.2.5"):
        headers = {"appName": appName, "sysname": sysname, "authToken": authToken}
        main = self.sendGet("/primary2secondary",headers=headers)
        print("Your Token: " + main["result"]["token"])
        return main["result"]["token"]

    ### PRIMBON ###
    def primbonNama(self, nama):
        return self.sendGet("/primbon/nama?nama="+nama)
    def primbonZodiac(self, zodiac):
        return self.sendGet("/primbon/bintang?zodiac="+zodiac)
    def primbonKecocokan(self, nama1, nama2):
        return self.sendGet("/primbon/kecocokan?nama1={}&nama2={}".format(nama1,nama2))

    ### SMULE ###
        # POST #
    def smulePost(self, url):
        return self.sendGet("/smule?url="+url)
        # PROFILE #
    def smuleProfile(self, userid):
        return self.sendGet("/smule?userid="+userid)
        # PERFORMANCE #
    def smulePerformance(self, userid):
        return self.sendGet("/smule?performance="+userid)

    ### SIMISIMI ###
    def simiTalk(self, text, lang="id"): #['af', 'al*', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'cx*', 'ch*', 'hr', 'cs', 'da', 'nl', 'en', 'et', 'ph*', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'he', 'hi', 'hu', 'is', 'id', 'it', 'ja', 'kn', 'kk', 'kh*', 'ko', 'ku', 'lv', 'lt', 'mk', 'ms', 'ml', 'mr', 'mn', 'my', 'ne', 'nb', 'as', 'br', 'gn', 'jv', 'or', 'rw', 'zh*', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'rs*', 'si', 'sk', 'sl', 'es', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'vn*', 'cy']
        return self.sendGet("/simisimi?text={}&lang={}".format(text,lang))

    ### SHORT LINK GENERATOR ###
    def shortLink(self, url):
        return self.sendPost("/short_link",data={"url": url})

    ### RORATE SECONDARY QR ###
    def secondaryQR(self, sysname="BE-Team", cert=None, appName="IOSIPAD\t10.5.2\tiPhone 8\t11.2.5"):
        headers = {"appName": appName, "cert" : cert, "sysname": sysname}
        main = self.sendGet("/qrv2",headers=headers)
        print("QR Link: " + main["result"]["qr_link"])
        if not headers["cert"]:
            print("Callback Pincode: " + main["result"]["cb_pincode"])
            result = self.sendGet(main["result"]["cb_pincode"].replace(self.host,""))
            print("Your Pincode: " + result["result"])
        result = self.sendGet(main["result"]["cb_token"].replace(self.host,""))
        print("Your Cert: " + result["result"]["cert"])
        print("Your Token: " + result["result"]["token"])
        return result["result"]["cert"], result["result"]["token"]

    ### SWAPFACE ###
        # IMAGE TEMPLATE #
    def swapfaceImageWithUrl(self, url, templateId):
        return self.sendGet("/swapface/image?url={}&id={}".format(url,templateId))
    def swapfaceImageWithPath(self, path, templateId):
        return self.sendPost("/swapface/image?id="+templateId,files={"file": open(path,"rb")})
    def swapfaceImageListTemplate(self):
        return self.sendGet("/swapface/image/list")
        # GIF TEMPLATE #
    def swapfaceGifWithUrl(self, url, templateId):
        return self.sendGet("/swapface/gif?url={}&id={}".format(url,templateId))
    def swapfaceGifWithPath(self, path, templateId):
        return self.sendPost("/swapface/gif?id="+templateId,files={"file": open(path,"rb")})
    def swapfaceGifListTemplate(self):
        return self.sendGet("/swapface/gif/list")
        # VIDEO TEMPLATE #
    def swapfaceVideoWithUrl(self, url, templateId):
        return self.sendGet("/swapface/video?url={}&id={}".format(url,templateId))
    def swapfaceVideoWithPath(self, path, templateId):
        return self.sendPost("/swapface/video?id="+templateId,files={"file": open(path,"rb")})
    def swapfaceVideoListTemplate(self):
        return self.sendGet("/swapface/video/list")
    
    ### TIKTOK VIDEO DOWNLOAD NOWM #
    def tiktokDownload1(self, url): 
        return self.sendGet("/musicallydown?url="+url)
    def tiktokDownload2(self, url): 
        return self.sendGet("/snaptik?url="+url)

    ### TRACK RESI ###
    def trackResi(self, resi, courier):
        listCourier = ['pos', 'wahana', 'jnt', 'sap', 'sicepat', 'jet', 'dse', 'first', 'ninja', 'lion', 'idl', 'rex', 'ide', 'sentral']
        if courier not in listCourier:
            raise Exception("courier trackresi not found...")
        return self.sendGet("/trackresi?resi={}&courier={}".format(resi,courier))

    ### TWITTER ###
        # POST #
    def twitterPost(self, url): 
        return self.sendGet("/twitter?url="+url)
        # PROFILE #
    def twitterProfile(self, userid): 
        return self.sendGet("/twitter?userid="+userid)

    ### FILE TO URL ( STORAGE ) ###
    def uploadStorage(self, path):
        return self.sendPost("/storage",files={"file": open(path,"rb")})

    ### SCREENSHOT WEBSITE ###
    def webScreenshot(self, url):
        return self.sendGet("/webss?url="+url)

    ### YOUTUBE DOWNLOAD ###
    def youtubeDownloadUrl(self, url):
        return self.sendGet("/ytdl?url="+url)
    def youtubeDownloadSearch(self, search):
        return self.sendGet("/ytdl?search="+search)

    ### YOUTUBE MP3 ###
    def youtubeMp3Url(self, url):
        return self.sendGet("/ytmp3?url="+url)
    def youtubeMp3Search(self, search):
        return self.sendGet("/ytmp3?search="+search)

    ### YOUTUBE MP4 ###
    def youtubeMp4Url(self, url):
        return self.sendGet("/ytmp4?url="+url)
    def youtubeMp4Search(self, search):
        return self.sendGet("/ytmp4?search="+search)

# APPNAME LIST FOR QR (EXAMPLE) :
# "IOSIPAD\t10.10.0\tiPhone 8\t11.2.5"
# "CHROMEOS\t2.3.8\tChrome OS\t1"
# "DESKTOPWIN\t6.0.3\tWindows\t10"
# "DESKTOPMAC\t6.0.3\tMAC\t10.15"

