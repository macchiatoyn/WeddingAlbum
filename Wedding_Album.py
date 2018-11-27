from bs4 import BeautifulSoup
import requests

#sample users:
#  meagan_moffitt

#tags for testing:
#  johnandsuzie2018
#  davidplussue
#  samanddavidsayido
#  vickyandryan
#  timandbeckyswedding
#  tylerandnataliesayido



quince_dict = {
    'dress': 'prep',
    'hair': 'prep',
    'excite': 'prep',
    'makeup': 'prep',
    'make up': 'prep',
    'escort': 'prep',
    'ready': 'prep',
    'florals': 'prep',
    'flower': 'prep',
    'table': 'prep',
    'silverware': 'prep',
    'placesetting': 'prep',
    'decor': 'prep',
    'planning': 'prep',
    'arrange': 'prep',
    'design': 'prep',
    'entrance': 'prep',
    'banquet': 'prep',
    'hall':'prep',
    'venue':'prep',
    'music': 'dance',
    'waltz': 'dance',
    'father daughter': 'dance',
    'fatherdaughter': 'dance',
    'dj': 'dance',
    'dance': 'dance',
    'dancing': 'dance',
    'groov': 'dance',
    'shake': 'dance',
    'disco': 'dance',
    'rock': 'dance',
    'boogie': 'dance',
    'shimmy': 'dance',
    'strut': 'dance',
    'sway': 'dance',
    'baila': 'dance',
    'choreograph': 'dance',
    'cake': 'food',
    'bake': 'food',
    'baked': 'food',
    'dessert': 'food',
    'cut': 'food',
    'tier': 'food',
    'yum': 'food',
    'food': 'food',
    'bar': 'food',
    'chocolate': 'food',
    'fruit': 'food',
    'drink': 'food',
    'cheers': 'food',
    'delicious': 'food',
    'catering': 'food',
    'sugar': 'food',
    'confection': 'food',
    'photograph':'photoshoot',
    'pic': 'photoshoot',
    'shot': 'photoshoot',
    'model': 'photoshoot',
    'headshot': 'photoshoot',
    'photoshoot': 'photoshoot',
    'booth': 'photobooth',
    'friend':'familyandfriends',
    'sister':'familyandfriends',
    'uncle':'familyandfriends',
    'brother':'familyandfriends',
    'mom':'familyandfriends',
    'dad':'familyandfriends',
    'father':'familyandfriends',
    'mother':'familyandfriends',
    'sibling':'familyandfriends',
    'aunt':'familyandfriends',
    'grandm':'familyandfriends',
    'grandp':'familyandfriends',
    'fam':'familyandfriends',
    'squad':'familyandfriends',
    'crew':'familyandfriends',
    'people':'familyandfriends'
}

#result_temp = {"qui_prep":set(qui_prep),"recessional":set(recessional),"dance":set(dance),"cake": set(cake),
#                   "dinner": set(dinner), "what also happened": set(other)}
wedding_dict = {
    'wedding dress': 'wedding prep',
    'gown': 'wedding prep',
    'tuxedo': 'wedding prep',
    'wedding hair': 'wedding prep',
    'excite': 'wedding prep',
    'makeup': 'wedding prep',
    'make up': 'wedding prep',
    'ready': 'wedding prep',
    'florals': 'wedding prep',
    'venue': 'prelude',
    'open air': 'prelude',
    'outdoor': 'prelude',
    'wedding guest': 'prelude',
    'welcome': 'prelude',
    'here comes': 'prelude',
    'comes the bride': 'prelude',
    'bridesmaids': 'prelude',
    'maid of honor': 'prelude',
    'best man': 'prelude',
    'groomsmen': 'prelude',
    'parents': 'prelude',
    'just married': 'prelude',
    'music': 'recessional',
    'march': 'recessional',
    'down the aisle': 'recessional',
    'reception': 'reception',
    'new husband': 'reception',
    'new wife': 'reception',
    'bouquet': 'reception',
    'toss': 'reception',
    'wedding favor': 'reception',
    'dinner': 'reception',
    'champagne': 'reception',
    'garter': 'reception',
    'toast': 'reception',
    'speech': 'reception',
    'twirl': 'first dance',
    'first dance': 'first dance',
    'dancing floor': 'first dance',
    'lights down': 'first dance',
    'dancing': 'first dance',
    'dance': 'first dance',
    'dancing shoes': 'first dance',
    'cake': 'cake',
    'bake': 'cake',
    'baked': 'cake',
    'dessert': 'cake',
    'cut': 'cake',
    'tier': 'cake',
    'i now pronounce you': 'vows',
    'man and wife': 'vows',
    'mr. and mrs.': 'vows',
    'mister and misses': 'vows',
    'manandwife': 'vows',
    'i do': 'vows',
    'vow': 'vows',
    'ring exchange': 'vows',
    'ring': 'vows',
    'diamond': 'vows',
    'true love': 'vows',
    'tie the knot': 'vows',
    'love is patient': 'vows',
    'love is kind': 'vows',
    'you may now kiss': 'kiss',
    'mwah': 'kiss',
    'smooch': 'kiss',
    'kiss': 'kiss',
}


def number_of_post(soup):
    cont = soup.find("meta", {"name": "description"})['content']
    total_post = int(cont.split(' ')[0])

    if total_post < 10:
        maxphoto = total_post * 0.9
    elif total_post < 20:
        maxphoto = total_post * 0.8
    elif total_post < 30:
        maxphoto = total_post * 0.7
    else:
        maxphoto = total_post * 0.6

    return int(maxphoto)

# returns photos prioritizing covering categories and then likes
def return_photos(result_temp,maxphoto):
    count = 0
    wedding_prep = []
    prelude = []
    recessional = []
    reception = []
    first_dance = []
    cake = []
    vows = []
    kiss = []
    other = []
    seen = []
    while count < maxphoto:
        for set_name, photo_set in result_temp.items():
            if photo_set != set([]) and count < maxphoto:
                photo, seen = best_photo(photo_set, seen)

                if len(photo) != 0:
                    count = count + 1
                    if set_name == "cake":
                        cake.append(photo)
                    elif set_name == "kiss":
                        kiss.append(photo)
                    elif set_name == "first dance":
                        first_dance.append(photo)
                    elif set_name == "wedding_prep":
                        wedding_prep.append(photo)
                    elif set_name == "vows":
                        vows.append(photo)
                    elif set_name == "reception":
                        reception.append(photo)
                    elif set_name == "recessional":
                        recessional.append(photo)
                    elif set_name == "prelude":
                        prelude.append(photo)
                    elif set_name == "what also happened":
                        other.append(photo)
                    seen.append(photo)


    result = {"wedding_prep":wedding_prep, "prelude":prelude, "vows":vows, "kiss":kiss,
         "recessional":recessional, "reception":reception, "first dance":first_dance,"cake":cake,
         "what also happened":other}

    return result

# returns photos prioritizing covering categories and then likes
def return_photos_quince(result_temp,maxphoto):
    count = 0
    prep = []
    dance = []
    food = []
    photobooth = []
    photoshoot = []
    familyandfriends = []
    other = []
    seen = []

    while count < maxphoto:
        for set_name, photo_set in result_temp.items():

            if photo_set != set([]) and count < maxphoto:
                photo, seen = best_photo(photo_set, seen)
                if len(photo) != 0:
                    count = count + 1
                    if set_name == "food":
                        food.append(photo)
                    elif set_name == "dance":
                        dance.append(photo)
                    elif set_name == "qui_prep":
                        prep.append(photo)
                    elif set_name == "photobooth":
                        photobooth.append(photo)
                    elif set_name == "photoshoot":
                        photoshoot.append(photo)
                    elif set_name == "familyandfriends":
                        familyandfriends.append(photo)
                    elif set_name == "what also happened":
                        other.append(photo)
                    seen.append(photo)


    result = {"qui_prep":prep, "photoshoot":photoshoot, "dance":dance, "food":food, "photobooth":photobooth,
              "familyandfriends":familyandfriends, "what also happened":other}

    return result


# returns most liked photo from a set of photos
def best_photo(photo_set, seen):
    most_likes = 0
    best_photo = set()

    for photo in photo_set:
        if int(photo[1]) > int(most_likes) and not photo in seen:
            most_likes = photo[1]
            best_photo = photo
    return best_photo, seen


# Extract author of each post
def extract_username(shortcode):
    url = "https://www.instagram.com/p/" + shortcode + "/"
    r = requests.get(url)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')

    cont = soup.find("meta", {"name":"description"})['content']
    username = cont.split('@')[1].split(')')[0]

    return username



# Extract and return images based on keywords
# Input: soup
# Output: a dict of links with subevents
def extract_wedding_images(soup):

    max_post = number_of_post(soup)

    scripts = soup.find_all('script')
    all_info = scripts[3].text.strip()

    wedding_prep = []
    prelude = []
    recessional = []
    reception = []
    first_dance = []
    cake = []
    vows = []
    kiss = []
    other = []

    nodes = all_info.split("\"node\":")
    for x in nodes:
        if "text" in x and "display_url" in x:
            text = x.split('},')[0].lower()
            shortcode = x.split('"shortcode":"')[1].split('",')[0]
            username = "@" + extract_username(shortcode)

            liked_count = x.split('"edge_liked_by":{"count":')[1].split('}')[0]
            jpg_link = x.split('"display_url":"')[1].split('"')[0]
            flag = 0

            # Search for a keyword in "text", and save corresponding url
            for keyword in wedding_dict.keys():
                if keyword in text:
                    if wedding_dict.get(keyword) == "cake":
                        cake.append((jpg_link,liked_count,username))
                        flag = 1
                    elif wedding_dict.get(keyword) == "kiss":
                        kiss.append((jpg_link,liked_count,username))
                        flag = 1
                    elif wedding_dict.get(keyword) == "first dance":
                        first_dance.append((jpg_link,liked_count,username))
                        flag = 1
                    elif wedding_dict.get(keyword) == "wedding prep":
                        wedding_prep.append((jpg_link,liked_count,username))
                        flag = 1
                    elif wedding_dict.get(keyword) == "vows":
                        vows.append((jpg_link,liked_count,username))
                        flag = 1
                    elif wedding_dict.get(keyword) == "reception":
                        reception.append((jpg_link,liked_count,username))
                        flag = 1
                    elif wedding_dict.get(keyword) == "recessional":
                        recessional.append((jpg_link,liked_count,username))
                        flag = 1
                    elif wedding_dict.get(keyword) == "prelude":
                        prelude.append((jpg_link,liked_count,username))
                        flag = 1
            if not flag == 1:
                other.append((jpg_link,liked_count,username))


    result_temp = {"wedding_prep":set(wedding_prep),"prelude":set(prelude),"vows":set(vows),"kiss":set(kiss),
              "recessional":set(recessional), "reception":set(reception),"first dance":set(first_dance), "cake": set(cake),
              "what also happened": set(other)}

    result = return_photos(result_temp,max_post)

    return result


# Extract and return images based on keywords
# Input: soup
# Output: a dict of links with subevents
def extract_quince_images(soup):
    max_post = number_of_post(soup)

    scripts = soup.find_all('script')
    all_info = scripts[3].text.strip()

    prep = []
    photoshoot = []
    dance = []
    food = []
    photobooth = []
    familyandfriends = []
    other = []


    nodes = all_info.split("\"node\":")
    for x in nodes:
        if "text" in x and "display_url" in x:
            text = x.split('},')[0].lower()
            shortcode = x.split('"shortcode":"')[1].split('",')[0]
            username = "@" + extract_username(shortcode)

            liked_count = x.split('"edge_liked_by":{"count":')[1].split('}')[0]
            jpg_link = x.split('"display_url":"')[1].split('"')[0]
            flag = 0

            # Search for a keyword in "text", and save corresponding url
            for keyword in quince_dict.keys():
                if keyword in text:
                    if quince_dict.get(keyword) == "familyandfriends":
                        familyandfriends.append((jpg_link,liked_count,username))
                        flag = 1
                    if quince_dict.get(keyword) == "photobooth":
                        photobooth.append((jpg_link,liked_count,username))
                        flag = 1
                    elif quince_dict.get(keyword) == "dance":
                        dance.append((jpg_link,liked_count,username))
                        flag = 1
                    elif quince_dict.get(keyword) == "prep":
                        prep.append((jpg_link,liked_count,username))
                        flag = 1
                    elif quince_dict.get(keyword) == "photoshoot":
                        photoshoot.append((jpg_link,liked_count,username))
                        flag = 1
                    elif quince_dict.get(keyword) == "food":
                        food.append((jpg_link,liked_count,username))
                        flag = 1

            if not flag == 1:
                other.append((jpg_link,liked_count,username))


    result_temp = {"qui_prep":set(prep),"photoshoot":set(photoshoot),"dance":set(dance),"food": set(food),
                   "photobooth": set(photobooth),"familyandfriends":set(familyandfriends), "what also happened": set(other)}

    result = return_photos_quince(result_temp,max_post)

    return result




if __name__ == '__main__':
    event_type = input("Please enter the type of your event: ")
    #event_type = "quince"

    tag = input("Please enter a hashtag of your event: ")
    #tag = "arianasquinceañera"
    url = "https://www.instagram.com/explore/tags/" + tag + "/"


    r = requests.get(url)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')


    if event_type == "wedding":
        photos = extract_wedding_images(soup)
    elif event_type == "quince":
        photos = extract_quince_images(soup)
    else:
        print("Error! Check your input!")


    print("Links of images: ")
    for k,v in photos.items():
        print(k)
        for x in v:
            print(x)
        print()
