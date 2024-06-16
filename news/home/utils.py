import requests
from .models import Articles

def get_news_form_api(url):
    try:
        data = requests.get(url)
        data = data.json()
        if data.get('articles'):
            for article in data.get("articles"):
                # print(article)
                source=article.get('source').get('name')
                author=article.get('author')
                title=article.get('title')
                description=article.get('description')
                url=article.get('url')
                urlToImage=article.get('urlToImage')
                publishedAt=article.get('publishedAt')
                content=article.get('content')
                Articles.objects.create(source=source,
                author=author,
                title=title,
                description=description,
                url=url,
                urlToImage=urlToImage,
                publishedAt=publishedAt,
                content=content)
        print(data) 
    except Exception as e :
        print(e)    