import tweepy
import time
from random import randint
import random
import schedule
# from datetime import datetime

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
    "#coding"
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
    "#freecodecamp"
]

search_words = ["#javascript", "#100DaysOfCode",
                "#helpmecode", "#freecodecamp"
                "#linux", "#reactjs", "#nodejs"]
compliment = ["Amazing content", "Nice Video", "Great Learning Resource",
              "Check this Video Out", "Let Learn together", "Great Content",
              "Great Tutorial",
              "Nice Content"]


def retweetRandom():
    api.retweet(api.search(random.choice(search_words))[0].id_str)
    print("Retweeted Succefully")


def tweetRandom():
    tweet = random.choice(compliment) + '\n' + random.choice(links) + \
        '\n' + str(random.sample(hashtags, 7))
    api.update_status(tweet)
    print("Posted Succesfully")


schedule.every(5).hours.do(tweetRandom)
schedule.every(30).minutes.do(retweetRandom)

print("Just Got Started")
while True:
    schedule.run_pending()
    time.sleep(1)
