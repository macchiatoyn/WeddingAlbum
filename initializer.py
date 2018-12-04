from flask import Flask, render_template, request
import Wedding_Album as WA
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

hashtag = ""
event = ""

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



    if event_type == "Wedding":
        photos = WA.extract_wedding_images(soup)
    elif event_type == "Quincenera":
        photos = WA.extract_quince_images(soup)
    else:
        return render_template('display.html', invalid = True)


    print("hashtag is " + tag)
    print("event is " + event_type)
    counter = 0
    for k,v in photos.items():
        print(k)
        for x in v:
            print(x)
            counter += 1


    print(counter)
    return render_template('display.html', dictionary = photos.items(), hashtag = tag, count = counter, invalid = False)
