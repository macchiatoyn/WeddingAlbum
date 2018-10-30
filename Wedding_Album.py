from bs4 import BeautifulSoup
import requests

#meagan_moffitt
#johnandsuzie2018

tag = input("Please enter a hashtag of your event: ")
url = "https://www.instagram.com/explore/tags/" + tag + "/"
keywords = ["wedding","bridal"]

wedding_dict = {
'wedding dress': 'wedding prep',
'gown':'wedding prep',
'tuxedo':'wedding prep',
'wedding hair':'wedding prep',
'ready':'wedding prep',
'florals':'wedding prep',
'wedding': 'prelude',
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
'bouquet': 'reception',
'toss': 'reception',
'wedding favor': 'reception',
'dinner': 'reception',
'champagne': 'reception',
'garter': 'reception',
'toast':'reception',
'speech':'reception',
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

# Extract and return images based on keywords
# Input: soup
# Output: a list of links
def extract_images(soup):
    scripts = soup.find_all('script')
    all_info = scripts[3].text.strip()

    images = []

    nodes = all_info.split("\"node\":")
    for x in nodes:
        if "text" in x and "display_url" in x:
            text = x.split('},')[0].lower()

            # Search for a keyword in "text", and save corresponding url
            if keywords[0] in text:
                jpg_link = x.split('"display_url":"')[1].split('"')[0]
                images.append(jpg_link)

    return images

if __name__ == '__main__':
    r = requests.get(url)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')

    images = extract_images(soup)
    print("\nLinks of wedding images: ")
    print(images)
