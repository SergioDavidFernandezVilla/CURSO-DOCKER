import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Amin",
        "lastname": "sergio",
        "socialMedia":
        [
            {"facebookUser": "sergio"},
            {"instagramUser": "sergio"},
            {"xUser": "sergio"},
            {"linkedin": "sergio-david"},
            {"githubUser": "sergio"}
        ],
        "blog": "https://sergio.com",
        "author": "sergio"
    }
    return json.dumps(value)