import tweepy
import time
from random import randint
import random
import numpy as np
# flask stuff
from flask import Flask
from flask_cors import CORS
# from datetime import datetime


# Flask and CORS stuff
app = Flask(__name__)
CORS(app)



consumer_key = 'uZGF89lJwOs7JT70wnRb3ZWwM'
consumer_secret = '0KAo0Dk27tEepN7dUEIvKNKRNAEzUPamyvUHVXIm3NYDRpvXaq'
Access_key = '1165369936488927233-6dbf0usveUf0TFMOcuVAD5AFUzWvtE'
Access_secret = 'Gj6BimWT0c4oj55NS3uTh8yzSlx0ygg7uP2Oo5k5vGAjR'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(Access_key, Access_secret)
# Twi Api
api = tweepy.API(auth)


links = [
    'https://www.youtube.com/watch?v=yVmm3FjXbm8&t=243s',
    'https://www.youtube.com/watch?v=fx7pW3kPXMg',
    'https://www.youtube.com/watch?v=PDFlqkm5-LQ&t=22s',
    'https://www.youtube.com/watch?v=hW6t1c46CsY&t=606s',
    'https://www.youtube.com/watch?v=HFHM8eWwjn0',
    'https://www.youtube.com/watch?v=-Fxy5pewRkU',
    'https://www.youtube.com/watch?v=aQXSErOBlqA'
]
hashtags = [
    '#programming',
    "#javascript",
    "#codeNewbies",
    "#frontEnd",
    "#100DaysOfCode",
    "#coding",
    "#reactjs",
    "#CodeNewbies",
    "#css",
    "#linux",
    "#webdev",
    "#python",
    "#nodejs",
    '#Denojs',
    "#techtwitter",
    '#vuejs',
    "#helpmecode",
    "#freecodecamp",
    "#nestjs"
]

search_words = ["#javascript",
                "#webdevelopment", "#angular", "#nestjs"
                "#techtwitter", "#techtwitter", "#100DaysOfCode",
                "#helpmecode", "#freecodecamp", "#CodeNewbies",
                "#linux", "#reactjs", "#nodejs"]
compliment = ["Amazing content", "Nice Video", "Great Learning Resource",
              "Check this Video Out", "Let Learn together", "Great Content",
              "Great Tutorial",
              "Nice Content"]


def retweetRandom():
    try:
        api.retweet(api.search(random.choice(search_words))[0].id_str)
        return { "action": "retweet", "status": "success"}
    except Exception as err:
        exception_type = type(err).__name__
        return { "action": "retweet", "status": "failed", "error_type": exception_type}


def tweetRandom():
    try:
        tweet = random.choice(compliment) + '\n' + random.choice(links) + \
        '\n' + ' '.join(random.sample(hashtags, 7))
        api.update_status(tweet)
        return { "action": "tweet", "status": "success"}
    except Exception as err:
        exception_type = type(err).__name__
        return { "action": "tweet", "status": "failed", "error_type": exception_type}


@app.route("/tweet")
def tweet():
    return tweetRandom()

@app.route("/retweet")
def retweet():
    return retweetRandom()

if __name__ == '__main__':
    app.debug = False
    app.run()
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)