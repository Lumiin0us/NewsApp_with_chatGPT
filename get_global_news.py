import json 

def get_global_news():
    COUNTRIES = ['africa', 'americas', 'asia', 'australia', 'canada', 'europe', 'middleeast']
    with open("files/all_region_news.json", "r") as json_file:
        json_data = json.load(json_file)
        world = []
        all_articles = []
        for index, region in enumerate(COUNTRIES):
            articles = json_data[index][region]
            country = []
            for i in range(len(articles)):
                country.append(articles[i]['choices'][0]['message']['content'])
                all_articles.append(articles[i]['choices'][0]['message']['content'])
            world.append(country)
    return world, all_articles
    
