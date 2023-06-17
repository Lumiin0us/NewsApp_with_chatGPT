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

counter = 0
@app.route('/')
def news_loading_page():
    return render_template('app_loading.html')

@app.route('/loaded')
def loading_done():
    global counter 
    if news_title is None or news_description is None:
        return "Data not loaded yet. Please wait or refresh the page."
    else:
        if counter + 8 <= len(news_title):
            return render_template('app_ui.html',title=news_title, description=news_description, index=counter)

        else:
            counter = 0
            return render_template('app_ui.html',title=news_title, description=news_description, index=counter)
    
@app.after_request
def after_request(response):
    global counter 
    counter += 8 
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)