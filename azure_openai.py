import os
from decouple import config
import openai

# Set up OpenAI API credentials and configuration
def setup_openai():
    openai.api_key = config("AZURE_OPENAI_KEY")
    openai.api_base = config("AZURE_OPENAI_ENDPOINT")  # Your endpoint URL
    openai.api_type = 'azure'
    openai.api_version = '2023-05-15'  # Update as needed

# Create a function to generate a LinkedIn post content
def generate_linkedin_post(text=False):
    deployment_name = 'linked'  # Update with your deployment name

    # Define the starting phrase for the post
    if text:
        start_phrase = text
    else:
        start_phrase = """
    You are a Python professional assistant and expert in social media content. 
    Tell me a fact about Python programming language, which may be a tidbit or a functional fact or some code explanation. 
    Also, explain with an example where necessary. We shall share this post on LinkedIn, therefore use hashtags also. 
    And, keep this fact/tidbit/explanation shorter, no more than 300 words.
    """

    # Send a completion call to generate an answer
    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=[{
            'role': 'system',
            'content': start_phrase
        }],
        max_tokens=400,
        temperature=0.7
    )

    # Extract and return the generated post content
    text = response['choices'][0]['message']['content']
    return start_phrase, text

if __name__ == "__main__":
    setup_openai()
    start_phrase, generated_post = generate_linkedin_post()
    print(start_phrase, ":\n", generated_post)

