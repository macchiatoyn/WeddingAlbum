from bs4 import BeautifulSoup
import requests

#sample users:
#  meagan_moffitt

#tags for testing:
#  johnandsuzie2018
#  davidplussue

wedding_dict = {
'wedding dress': 'wedding prep',
'gown':'wedding prep',
'tuxedo':'wedding prep',
'wedding hair':'wedding prep',
'excite': 'wedding prep',
'makeup' :'wedding prep',
'make up':'wedding prep',
'ready':'wedding prep',
'florals':'wedding prep',
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
'toast':'reception',
'speech':'reception',
'twirl': 'first dance',
'first dance': 'first dance',
'dancing floor': 'first dance',
'lights down': 'first dance',
'dancing': 'first dance',
'dance': 'first dance',
'dancing shoes': 'first dance',
'cake':'cake',
'bake':'cake',
'baked': 'cake',
'dessert':'cake',
'cut':'cake',
'tier':'cake',
'i now pronounce you': 'vows',
'man and wife': 'vows',
'mr. and mrs.': 'vows',
'mister and misses': 'vows',
'manandwife': 'vows',
'i do': 'vows',
'vow': 'vows',
'ring exchange' : 'vows',
'ring' : 'vows',
'diamond' : 'vows',
'true love' : 'vows',
'tie the knot' : 'vows',
'love is patient' : 'vows',
'love is kind' : 'vows',
'you may now kiss' : 'kiss',
'mwah' : 'kiss',
'smooch' : 'kiss',
'kiss' : 'kiss',
}

#returns photos prioritizing covering categories and then likes
def return_photos(result):
    count = 0
    result_list = []
    wedding_prep = ['wedding_prep']
    prelude = ['prelude']
    recessional = ['recessional']
    reception = ['reception']
    first_dance = ['first_dance']
    cake = ['cake']
    vows = ['vows']
    kiss = ['kiss']
    seen = []
    while count < 12:
        for set_name,photo_set in result.items():
            if photo_set != set([]) and count < 12:
                count = count + 1
                photo, seen = best_photo(photo_set, seen)
                if set_name == "cake":
                    cake.append(photo)
                elif set_name == "kiss":
                    kiss.append(photo)
                elif set_name == "first dance":
                    first_dance.append(photo)
                elif set_name == "wedding_prep":
                    wedding_prep.append(photo)
                elif set_name == "vows" :
                    vows.append(photo)
                elif set_name == "reception":
                    reception.append(photo)
                elif set_name == "recessional":
                    recessional.append(photo)
                elif set_name == "prelude":
    return wedding_prep, prelude, recessional, reception, first_dance, cake, vows, kiss, len(wedding_prep), len(prelude), len(recessional), len(reception), len(first_dance), len(cake), len(vows), len(kiss)


#returns most liked photo from a set of photos
def best_photo(photo_set, seen):
    most_likes = 0
    best_photo = set()

    for photo in photo_set:
        if int(photo[1]) > int(most_likes) and not photo in seen:
            most_likes = photo[1]
            best_photo = photo
            seen.append(photo)
    return best_photo, seen



# Extract and return images based on keywords
# Input: soup
# Output: a dict of links with subevents
def extract_wedding_images(soup):
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

    nodes = all_info.split("\"node\":")
    for x in nodes:
        if "text" in x and "display_url" in x:
            text = x.split('},')[0].lower()

            # Search for a keyword in "text", and save corresponding url
            for keyword in wedding_dict.keys():
                if keyword in text:
                    liked_count = x.split('"edge_liked_by":{"count":')[1].split('}')[0]
                    jpg_link = x.split('"display_url":"')[1].split('"')[0]

                    if wedding_dict.get(keyword) == "cake":
                        cake.append((jpg_link,liked_count))
                    elif wedding_dict.get(keyword) == "kiss":
                        kiss.append((jpg_link,liked_count))
                    elif wedding_dict.get(keyword) == "first dance":
                        first_dance.append((jpg_link,liked_count))
                    elif wedding_dict.get(keyword) == "wedding prep":
                        wedding_prep.append((jpg_link,liked_count))
                    elif wedding_dict.get(keyword) == "vows":
                        vows.append((jpg_link,liked_count))
                    elif wedding_dict.get(keyword) == "reception":
                        reception.append((jpg_link,liked_count))
                    elif wedding_dict.get(keyword) == "recessional":
                        recessional.append((jpg_link,liked_count))
                    elif wedding_dict.get(keyword) == "prelude":
                        prelude.append((jpg_link,liked_count))


    result = {"wedding_prep":set(wedding_prep),"prelude":set(prelude),"vows":set(vows),"kiss":set(kiss),
              "recessional":set(recessional), "reception":set(reception),"first dance":set(first_dance), "cake": set(cake)}
    print(return_photos(result))
    return result



if __name__ == '__main__':
    tag = input("Please enter a hashtag of your event: ")
    url = "https://www.instagram.com/explore/tags/" + tag + "/"
    
    r = requests.get(url)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')

    photos = extract_wedding_images(soup)
    print("\nLinks of wedding images: ")
    for k,v in photos.items():
        print(k)
        print(v)
        print()
    #print(photos)
