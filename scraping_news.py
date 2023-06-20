import json
from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import random
import os
import time

URL = "https://www.nytimes.com/international/section/world"
COUNTRIES = ["europe"]

user_agents_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.68 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.92 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.17 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SM-G988U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.79 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.21 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.23 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.46 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.37 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.55 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.60 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.13 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.66 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.80 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/88.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/88.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
]

os.chdir("/Users/abdurrehman/Desktop/NewsApp_with_chatGPT/NewsApp_with_chatGPT/files")

session = requests.Session()
retry = Retry(connect=5, backoff_factor=2)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

for region in COUNTRIES:
    try:
        response = session.get(f"{URL}/{region}")
        soup = BeautifulSoup(response.content, 'html.parser')
        anchor_tags = soup.select('.css-1l4spti a')

        all_articles = []  # Initialize list to store all articles
        
        for index, anchor_tag in enumerate(anchor_tags):
            para_list = []  # Initialize para_list for each article
            print(f"ARTICLE_{region}_{index}")
            href = anchor_tag['href']
            html = session.get(f"https://www.nytimes.com{str(href)}", headers={'User-Agent': random.choice(user_agents_list)})
            detail_soup = BeautifulSoup(html.content, "html.parser")
            section = detail_soup.find("section", class_="meteredContent css-1r7ky0e")
            
            if section is not None:
                try:
                    p_tags = section.find_all("p")
                    print(len(p_tags))
                    print(p_tags[8].getText())
                    for index_, p_tag in enumerate(p_tags):
                        if p_tag is not None:
                            print(f"ARTICLE_{region}_Para_{index_}")
                            para_list.append(p_tag.getText())
                except Exception as e: 
                    print("[EXCEPTION] ", e)

            
            article_data = {
                f"{region}_{index + 1}": para_list
            }
            all_articles.append(article_data)
        
        if all_articles:
            print("\n[CREATING FILE]\n")
            if not os.path.exists(f"{region}.json"):
                with open(f"{region}.json", "w") as json_file:
                    json.dump(all_articles, json_file)
            else:
                with open(f"{region}.json", "r") as json_file:
                    data = json.load(json_file)
                    data.extend(all_articles)
                
                with open(f"{region}.json", "w") as json_file:
                    json.dump(data, json_file)
    
    except:
        time.sleep(5)