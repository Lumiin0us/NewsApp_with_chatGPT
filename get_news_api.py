import requests 

URL = "https://jsonplaceholder.typicode.com/posts"

def get_news(URL):
    news_description = []
    try:
        response = requests.get(url=URL)
        api_data = response.json()
        for data in api_data:
            news_description.append(data['title'])
        return news_description
    
    except Exception as e:
        print(f"[EXCEPTION IN FETCHING API] {e}")
