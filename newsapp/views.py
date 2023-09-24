from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def index(request):
    API_KEY = 'cc58d962a6f249d4a7fbfa421b63d1e0'
    newsapi = NewsApiClient(api_key=API_KEY)
    src = newsapi.get_sources()
    print(src)

    top = newsapi.get_top_headlines(sources='bbc-news')
    my_articles=top['articles']
    news = []
    desc = []
    img = []
    for i in range(len(my_articles)):
        f = my_articles[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        lst = zip(news, desc, img)
    print(lst)

    return render(request, 'index.html', {'lst':lst})