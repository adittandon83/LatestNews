from newsapi import NewsApiClient
import json

if __name__ == '__main__':
    newsapi = NewsApiClient(api_key='cd7b50071b924884bc40e45b9eb5422b')
    # top_headlines = newsapi.get_top_headlines(q='bitcoin', language='en')
    topic= input("Enter your topic of interest:")
    everything = newsapi.get_everything(qintitle=topic, language='en')
    num =1
    for article in everything['articles']:
        print(num, article['source']['name'], "-", article['title'])
        num+=1
