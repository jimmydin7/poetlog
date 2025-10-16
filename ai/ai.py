import os

open_ai_api_key = os.environ.get('OPENAI_API_KEY')
alternative_api = os.environ.get('ALTERNATIVE_FREE_API')

def generate_poem()