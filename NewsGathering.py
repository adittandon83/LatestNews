from newsapi import NewsApiClient

if __name__ == '__main__':
    newsapi = NewsApiClient(api_key='<yourAPIKEY>')
    topic= input("Enter your topic of interest:")
    everything = newsapi.get_everything(qintitle=topic, language='en')
    num =1
    for article in everything['articles']:
        print(num, article['source']['name'], "-", article['title'])
        num+=1
