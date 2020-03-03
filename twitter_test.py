import tweepy
import csv

consumer_key = 'TErus3u1UOUgdR6AKhIaaE9Wg'
consumer_secret = 'UI8yW0epbpuX9CxNl91eSVCGtmDh9IBkUvopH2TvPIaLjVgOCy'
access_token = '1234781863597760512-SAmWryVIvcqjHM44kTbHhTS0SFExu6'
access_token_secret = 'QPigS2G8RF6wtxiVROnwTAzduh16CuewaBtgOgQdAa5Zv'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

hashtag = 'coronavirus'
csvFile = open(f'{hashtag}.csv', 'w', encoding='utf-8')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q=f"#{hashtag}",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
