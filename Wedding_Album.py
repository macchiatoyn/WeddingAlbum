from bs4 import BeautifulSoup
import requests

#meagan_moffitt
#johnandsuzie2018

tag = input("Please enter a hashtag of your event: ")
url = "https://www.instagram.com/explore/tags/" + tag + "/"
keywords = ["wedding","bridal"]


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
