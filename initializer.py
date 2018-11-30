from flask import Flask, render_template, request
import Wedding_Album as WA
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

hashtag = ""
event = ""

fakeDictionary = {
    "firstDance" : [("justone", 0, "@nope"), ("secondone", 1, "@wooo")],
    "firstKiss" : [("fakeurl", 15, "@jennikim"), ("Woohoo", 31, "@boyjoshy"), ("no stop", 20, "@boyjoshy")]
}

@app.route('/')
def render_home():
    return render_template('index.html')

@app.route('/collection', methods=['POST'])
def render_album():

    tag = request.form['hashtag']
    event_type = request.form['event']
    url = "https://www.instagram.com/explore/tags/" + tag + "/"

    r = requests.get(url)
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')

    cont = soup.find("meta", {"name": "description"})['content']
    total_post = int(cont.split(' ')[0])
    maxphoto = 5


    if event_type == "Wedding":
        photos = WA.extract_wedding_images(soup)
    elif event_type == "Quince":
        photos = WA.extract_quince_images(soup)
    else:
        print("Error! Check your input!")

    print("hashtag is " + tag)
    print("event is " + event_type)
    for k,v in photos.items():
        print(k)
        for x in v:
            print(x)
        print()
    return render_template('display.html', dictionary = photos.items(), hashtag = tag)
