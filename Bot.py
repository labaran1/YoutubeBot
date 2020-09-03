import tweepy
import requests
import time
from random import randint
import random
import numpy as np
# flask stuff
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()
# Flask and CORS stuff
app = Flask(__name__)
CORS(app)


# Getting env variables
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
Access_key = os.environ.get('Access_key')
Access_secret = os.environ.get('Access_secret')
YouTube_Api_Key = os.environ.get('YouTube_Api_Key')

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
                "https://towardsdatascience.com/the-self-learning-path-to-becoming-a-data-scientist-ai-or-ml-engineer-9ab3a97ca",
               "https://medium.com/@labaranlabs/is-it-worth-contributing-to-open-source-f1bca2c21828",
               "https://towardsdatascience.com/the-no-code-approach-to-data-science-and-ai-41bf22fea971",
               "https://medium.com/downsample/rules-to-building-an-ai-system-from-a-data-scientist-f39d303d7d79",
               "https://towardsdatascience.com/why-you-should-consider-a-career-in-data-science-5f5468e516b6"


]
toFollow = ["traversymedia", "randallKanna", "kvlly", "lavie_encode", "math_rachel","florinpop1705", "lynnandtonic", "Emmaboiston", "catalinmpit", "techgirl1908", "kentcdodds", "scribblingOn", 'telmo', "samantha_ming"]
followid = []
Assert = ['Data1.jpeg',
'Data2.jpeg',
'Data3.jpeg',
'Data4.jpeg',
'Data5.jpeg'
,
'Data6.jpeg',
'Data7.jpeg',
'Data8.jpeg',
'Data9.jpeg',
'Data10.jpeg',
'Data11.jpeg',
'Data12.jpeg',
'Data13.jpeg',
'Data14.jpeg',
'Data15.jpeg',
'Data16.jpeg',
'Data17.jpeg',
'Data18.jpeg',
'Data19.jpeg',
'Data20.jpeg',
'Data21.jpeg',
'Data22.jpeg',
'Data23.jpeg',



]

# Function to run every 10 hours
def toFollowDetails():
    try:
        mine = random.sample(api.followers_ids(random.choice(toFollow)), 150)
                         #    followid.append(random.sample(api.followers_ids(random.choice(toFollow)), 10))
        for i in mine:
            followid.append(i)
        return { "action": "Get Details of who to follow", "status":"success"}

    except Exception as err:
        exception_type = type(err).__name__
        return { "action": "Get Details of who to follow", "status": "failed", "error_type": exception_type}


 

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
        # me = '/me.jpeg'
        # api.update_status(tweet)
        pic = f'./Asserts/{random.choice(Assert)}'
        
        api.update_with_media(pic, tweet)
        return { "action": " article tweet", "status": "success"}
    except Exception as err:
        exception_type = type(err).__name__
        return { "action": "tweet article", "status":"failed", "error_type":exception_type}





def follow():

    try:
       
        api.create_friendship(random.choice(followid))

        return { "action": "followed", "status":"Success"}

        
    except Exception as err:
        exception_type = type(err).__name__
        
        return { "action": "Unable to follow", "status":"failed", "error_type":exception_type}




@app.route('/follow')
def followInc():
    return follow()

@app.route('/getFollowers')
def getFollow():
    followid.clear()
    return toFollowDetails()

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
