import openai 

def open_ai(news_list):
    API_KEY = "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"
    openai.api_key = API_KEY
    summarized_news_responses = []
    try:
        for news in news_list:
            completion_response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[{
                    'role': 'user', 
                    'content': f'Could you please look at this news, its not complete, could you make sense out of it by yourself and return a sumarrized response? Here: {news}',
                }]
            )
            summarized_news_responses.append(completion_response)

        print(completion_response.choices[0].message.content)

    except Exception as e:
        print(f"[EXCEPTION IN OPENAI-API] {e}")
