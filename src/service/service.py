import openai


from src.config import config
from src.utils.utils import preprocess_text


# Set your OpenAI API key
openai.api_key = config.settings.OPENAI_API_KEY

class OpenAIService():

    # Function to classify the article using OpenAI API
    def classify_article(article_text):
        # Preprocess the text
        cleaned_text = preprocess_text(article_text)
        
        prompt = f"Determine if the following news article is real or fake:\n{cleaned_text}\n\nAnswer with 'Fake' or 'Real'."
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
        result = response.choices[0].message['content'].strip()
        return result

