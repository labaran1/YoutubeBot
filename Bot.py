import tweepy
import requests
import time
from random import randint
import random
import numpy as np
# flask stuff
from flask import Flask
from flask_cors import CORS
import os
# from datetime import datetime


# Flask and CORS stuff
app = Flask(__name__)
CORS(app)


# Todo:Move to Env variables
consumer_key = 'uZGF89lJwOs7JT70wnRb3ZWwM'
consumer_secret = '0KAo0Dk27tEepN7dUEIvKNKRNAEzUPamyvUHVXIm3NYDRpvXaq'
Access_key = '1165369936488927233-6dbf0usveUf0TFMOcuVAD5AFUzWvtE'
Access_secret = 'Gj6BimWT0c4oj55NS3uTh8yzSlx0ygg7uP2Oo5k5vGAjR'
YouTube_Api_Key = "AIzaSyCbr1OKUXT0ecjiMsS-trRYKvqHxIOtXdw"
# Variables
channel_id = "UCLINuI_UuQ3KMY-QQYGO1Lw"
uploads_id = "UULINuI_UuQ3KMY-QQYGO1Lw"
youtubeShort_video_Url = "https://www.youtube.com/watch?v="
playlist = f"https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={uploads_id}&key={YouTube_Api_Key}&maxResults=50"



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(Access_key, Access_secret)
# Twi Api
api = tweepy.API(auth)

  # 'https://www.youtube.com/watch?v=qzMYrt5GqAo&list=PLHz0I0UMGTSwo61WYAvRHre0QcIU4f1ip&index=2',
    # 'https://www.youtube.com/watch?v=yVmm3FjXbm8&t=243s',
    # 'https://www.youtube.com/watch?v=fx7pW3kPXMg',
    # 'https://www.youtube.com/watch?v=PDFlqkm5-LQ&t=22s',
    # 'https://www.youtube.com/watch?v=hW6t1c46CsY&t=606s',
    # 'https://www.youtube.com/watch?v=HFHM8eWwjn0',
    # 'https://www.youtube.com/watch?v=-Fxy5pewRkU',
    # 'https://www.youtube.com/watch?v=aQXSErOBlqA',
    # "https://www.youtube.com/watch?v=WOdndBthyPU&list=PLHz0I0UMGTSwo61WYAvRHre0QcIU4f1ip&index=3"


links = []
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
   "#Datascience",
   "#ML",
   
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

articleCompliment =["Great Article",
                    "Nice Work", 
                    "Amazing Content", 
                     "Worth a share",
                     "Check out this article", 
                    "Nice Article", "Worth a Retweet",
                    "Check this content out",
                     "Amazing Content"]
articleLinks =['https://medium.com/@labaranlabs/object-oriented-programming-concept-978a7cbaf33b',
                'https://medium.com/@labaranlabs/understand-data-types-in-javascript-2f4cee026ed3',
                "https://medium.com/@labaranlabs/data-analysis-with-pandas-39d4516f56a6",
                "https://towardsdatascience.com/the-fastml-guide-9ada1bb761cf",
                "https://towardsdatascience.com/developing-a-good-attitude-towards-data-science-be4b7d0e1e49",
                "https://medium.com/@adlabaran/ultimate-guide-to-numpy-for-machine-learning-a6d3dd5abdad",
                "https://towardsdatascience.com/the-self-learning-path-to-becoming-a-data-scientist-ai-or-ml-engineer-9ab3a97ca"


]

def getVids(playlist):
    try:
         data = requests.get(playlist).json()
         for ids in data["items"]:
             links.append(youtubeShort_video_Url + ids["snippet"]["resourceId"]["videoId"])
         return { "action": "Get Videos", "status":"success"}

    except Exception as err:
        exception_type = type(err).__name__
        return { "action": "Get Videos", "status": "failed", "error_type": exception_type}



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
        return { "action": " article tweet", "status": "success"}
    except Exception as err:
        exception_type = type(err).__name__
        return { "action": "tweet", "status": "failed", "error_type": exception_type}

def tweetArticle():
    try:
        tweet = random.choice(articleCompliment) + '\n' + random.choice(articleLinks) + \
          '\n' + ' '.join(random.sample(hashtags, 7))
        api.update_status(tweet)
        return { "action": " article tweet", "status": "success"}
    except Exception as err:
        exception_type = type(err).__name__
        return { "action": "tweet article", "status":"failed", "error_type":exception_type}



@app.route("/tweet")
def tweet():
    return tweetRandom()

@app.route("/retweet")
def retweet():
    return retweetRandom()


@app.route("/getVideos")
def getPersonalVids():
    links.clear()
    return getVids(playlist)

@app.route("/articletweet")
def article():
    return tweetArticle()
    

if __name__ == '__main__':
    app.debug = False
    app.run()
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
