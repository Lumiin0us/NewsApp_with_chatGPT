import requests 

URL = "https://jsonplaceholder.typicode.com/posts"

def get_news(URL):
    news_title = []
    news_body = []
    try:
        response = requests.get(url=URL)
        api_data = response.json()
        for data in api_data:
            news_title.append(data['title'])
            news_body.append(data['body'])

        return news_title, news_body
    
    except Exception as e:
        print(f"[EXCEPTION IN FETCHING API] {e}")
