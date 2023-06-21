import openai 
import time
import json
import os 

def fetch_data():
    os.chdir("/Users/abdurrehman/Desktop/NewsApp_with_chatGPT/NewsApp_with_chatGPT/files")
    dir = os.getcwd()

    COUNTRIES = ['africa', 'americas', 'asia', 'australia', 'canada', 'europe', 'middleeast']
    data_list = []

    for region in COUNTRIES:
        with open(f"{dir}/{region}.json") as json_object:
            json_file = json.load(json_object)        
        region_news = [list(items.values())[0] for items in json_file]
        data_list.append({region : region_news})
    return data_list, COUNTRIES

def wait_for_rate_limit():
    time.sleep(70)

def open_ai():
    region_list, COUNTRIES = fetch_data()
    API_KEY = "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"
    MAX_WORDS = 300
    openai.api_key = API_KEY
    response = []
    try:
        for region_index, regions in enumerate(region_list):
            region_dict = {}
            if COUNTRIES[region_index] == "canada":
                for news_index, news in enumerate(regions[COUNTRIES[region_index]]):
                    summarized_news_responses = []
                    if len(news) > 0:
                        for article in news:
                            truncated_article = " ".join(article.split()[:MAX_WORDS])
                            completion_response = openai.ChatCompletion.create(
                                model='gpt-3.5-turbo',
                                messages=[{
                                    'role': 'user', 
                                    'content': f'Could you please understand, create a logical frame, assign a topic heading and summarize this article in a formal and concise manner: {truncated_article}',
                                }]
                            )
                            summarized_news_responses.append(completion_response)
                            if len(summarized_news_responses) % 3 == 0:
                                wait_for_rate_limit()
                        break
                region_dict[COUNTRIES[region_index]] = summarized_news_responses
                response.append(region_dict)
                with open("chatGPT_response.json", "w") as gpt_json:
                    json.dump(response, gpt_json)
                break
        print(response)
    except Exception as e:
        print(f"[EXCEPTION IN OPENAI-API] {e}")

open_ai()
