from app import app
from flask import render_template, request
from instagram.client import InstagramAPI
import urllib.request, json
import ssl


#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
instaURL = "https://api.instagram.com/v1/"


@app.route('/')
@app.route('/index')
def index():
    with urllib.request.urlopen(instaURL + "users/self/?access_token=300842295.c5a6374.e55f81b372d74c1c83c42ec2df484238", context=ctx) as url:
        data = json.loads(url.read().decode())
        #!print(data)
    return render_template('index.html', data=data)

@app.route('/photos')
def photos():
    with urllib.request.urlopen(instaURL + "users/self/media/recent/?access_token=300842295.c5a6374.e55f81b372d74c1c83c42ec2df484238", context=ctx) as url:
        data = json.loads(url.read().decode())
        photoURLs = []
        #!print(data)
        for u in data['data']:
            photoURLs.append(u['images']['standard_resolution']['url'])
            #!print(u['images']['standard_resolution']['url'])



    return render_template('feed.html', picData=data, photos=photoURLs)
