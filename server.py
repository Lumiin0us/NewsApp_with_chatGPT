from flask import Flask, render_template
from get_global_news import get_global_news
import random 

class FlaskInstance(Flask):
    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        global news_title
        global news_description
        global world_news
        global all_articles
        world_news, all_articles = get_global_news()
        super().run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)

app = FlaskInstance(__name__)

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)