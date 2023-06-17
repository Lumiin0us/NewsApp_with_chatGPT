import requests 
import openai 

API_KEY = "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"
openai.api_key = API_KEY
try:
    completion_response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role': 'user', 
            'content': 'Write an essay about penguins',
        }]
    )

    print(completion_response.choices[0].message.content)

except Exception as e:
    print(f"[EXCEPTION IN OPENAI-API] {e}")
