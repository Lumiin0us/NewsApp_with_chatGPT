from flask import Flask, render_template
from get_news_api import get_news, URL

class FlaskInstance(Flask):
    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        global news_title
        global news_description
        title, description = get_news(URL)
        news_title = title
        news_description = description
        super().run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)

app = FlaskInstance(__name__)

@app.route('/')
def news():
    return render_template('app_ui.html',title=news_title, description=news_description)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)