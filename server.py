from flask import Flask, render_template
from get_news_api import get_news, URL
from get_global_news import get_global_news
import random 

class FlaskInstance(Flask):
    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        global news_title
        global news_description
        global world_news
        global all_articles
        title, description = get_news(URL)
        world_news, all_articles = get_global_news()
        news_title = title
        news_description = description
        super().run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)

app = FlaskInstance(__name__)

counter = 0
@app.route('/')
def news_loading_page():
    return render_template('app_loading.html')

# @app.route('/loaded')
# def loading_done():
#     global counter 
#     if news_title is None or news_description is None:
#         return "Data not loaded yet. Please wait or refresh the page."
#     else:
#         if counter + 8 <= len(news_title):
#             return render_template('app_ui.html',title=news_title, description=news_description, index=counter)

#         else:
#             counter = 0
#             return render_template('app_ui.html',title=news_title, description=news_description, index=counter)

@app.route('/world')
def global_news():
    random_num = random.randint(0, len(all_articles) - 1)

    return render_template('app_ui.html', world_news=all_articles[random_num])

@app.route('/africa')
def african_news():
    random_num = random.randint(0, len(world_news[0]) - 1)
    return render_template('app_ui.html', world_news=world_news[0][random_num])

@app.route('/america')
def american_news():
    random_num = random.randint(0, len(world_news[1]) - 1)
    return render_template('app_ui.html', world_news=world_news[1][random_num])

@app.route('/asia')
def asian_news():
    random_num = random.randint(0, len(world_news[2]) - 1)
    return render_template('app_ui.html', world_news=world_news[2][random_num])

@app.route('/australia')
def australian_news():
    random_num = random.randint(0, len(world_news[3]) - 1)
    return render_template('app_ui.html', world_news=world_news[3][random_num])

@app.route('/canada')
def canadian_news():
    random_num = random.randint(0, len(world_news[4]) - 1)
    return render_template('app_ui.html', world_news=world_news[4][random_num])

@app.route('/europe')
def european_news():
    random_num = random.randint(0, len(world_news[5]) - 1)
    return render_template('app_ui.html', world_news=world_news[5][random_num])

@app.route('/middleeast')
def middleeastern_news():
    random_num = random.randint(0, len(world_news[6]) - 1)
    return render_template('app_ui.html', world_news=world_news[6][random_num])



# @app.after_request
# def after_request(response):
#     global counter 
#     counter += 8 
#     return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)