import twitter
from textblob import TextBlob
from datetime import date, timedelta
import math

api = twitter.Api(consumer_key='TErus3u1UOUgdR6AKhIaaE9Wg',
                  consumer_secret='UI8yW0epbpuX9CxNl91eSVCGtmDh9IBkUvopH2TvPIaLjVgOCy',
                  access_token_key='1234781863597760512-SAmWryVIvcqjHM44kTbHhTS0SFExu6',
                  access_token_secret='QPigS2G8RF6wtxiVROnwTAzduh16CuewaBtgOgQdAa5Zv',
                  sleep_on_rate_limit=True,
                  tweet_mode='extended')

dates = []
avg_polarities = []
big_opinions = []

topic = 'coronavirus'

for i in range(7):
  polarities = []
  max_score = 0
  max_opinion = ''

  today = (date.today() + timedelta(days=-i)).strftime("%Y-%m-%d")
  yesterday = (date.today() + timedelta(days=-i-1)).strftime("%Y-%m-%d")
  results = api.GetSearch(term=topic, lang='en', since=yesterday, until=today, count=100) + api.GetSearch(term='#'+topic, since=yesterday, until=today, lang='en', count=100)

  for result in results:
    text = result.full_text.replace('&amp;', '&')
    polarity = TextBlob(text).sentiment.polarity * math.log(1 + result.favorite_count)
    polarities.append(polarity)

    if abs(polarity) > max_score:
      max_score = abs(polarity)
      max_opinion = text

  dates.append(today)
  if len(polarities) > 0:
    avg_polarities.append((sum(polarities) / len(polarities)))
  else:
    avg_polarities.append(0)

  big_opinions.append(max_opinion)

avg_polarities = [x for x in avg_polarities if x != 0][::-1]
dates = dates[:len(avg_polarities)][::-1]
big_opinions = big_opinions[:len(avg_polarities)][::-1]

for bo in big_opinions:
  print(bo, "\n")
  
  import matplotlib.pyplot as plt
from datetime import datetime

#Examples
#x = ['2020-02-24', '2020-02-25', '2020-02-26', '2020-02-27', '2020-02-28', '2020-02-29', '2020-03-01', '2020-03-02', '2020-03-03', '2020-03-04']
#y = [-10.532258804716355, 302.33430923829405, 46.625526925121406, 795.4368023574394, 432.7554295235555, 1480.4161395262813, -161.16961558096256, 194.4875581435194, 165.01653453626625, -22.052069277284346]

x = dates
y = avg_polarities

xtick_labels = [d[-5:] for d in x]

for i in range(len(x)):
  x[i] = datetime.strptime(x[i], "%Y-%m-%d")

#ax = plt.subplot(111)
#ax.bar(x, y, width=0.3)
#ax.xaxis_date()
#ax.set_xticklabels(xtick_labels)
plt.plot(xtick_labels, y)
plt.axhline(0, color='gray', dashes=(3, 3))
plt.show()
