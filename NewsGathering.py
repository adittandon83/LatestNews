from newsapi import NewsApiClient

if __name__ == '__main__':
    newsapi = NewsApiClient(api_key='<yourAPIKEY>')
    # top_headlines = newsapi.get_top_headlines(q='bitcoin', language='en')
    topic= input("Enter your topic of interest:")
    everything = newsapi.get_everything(qintitle=topic, language='en')
    num =1
    for article in everything['articles']:
        print(num, article['source']['name'], "-", article['title'])
        num+=1
