import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools


username = input('Enter a username: ')
topic = input('Enter a topic you want to scrape: ')

user_tweet = sntwitter.TwitterUserScraper(username).get_items()
topic_tweet = sntwitter.TwitterSearchScraper(topic).get_items()


count_username = itertools.islice(user_tweet, 500)
count_topic = itertools.islice(topic_tweet, 500)

df = pd.DataFrame(count_username)[['url', 'date', 'content', 'id', 'username', 'outlinks']]
dfs = pd.DataFrame(count_topic)[['url', 'date', 'content', 'id', 'username', 'outlinks']]

df.to_csv('nameofcsvfile.csv')
dfs.to_csv('nameof.csv')