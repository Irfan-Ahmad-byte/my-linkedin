import os
import time
import json

from .azure_openai import setup_openai, generate_linkedin_post
from .auto_linkedin import main as post_to_linkedin
from .load_generated_facts import load_generated_facts

# Path to the JSON file for storing generated facts
FACTS_FILE = 'generated_facts.json'

def save_generated_facts(facts):
    with open(FACTS_FILE, 'w') as f:
        json.dump(facts, f, indent=4)


def main():
    
    # Set up OpenAI
    setup_openai()
    generated_facts = load_generated_facts()

    # Generate a LinkedIn post fact
    start_phrase, generated_post = generate_linkedin_post()

    # Check if the fact is not already generated
    if generated_post not in generated_facts:
        # Post the fact to LinkedIn
        post_to_linkedin(generated_post)

        # Add the fact to the list of generated facts
        generated_facts.append(generated_post)
        save_generated_facts(generated_facts)
        print(f'Fact posted on LinkedIn:\n{start_phrase}\n{generated_post}')
    else:
        print('Fact already generated and posted.')
        main()

if __name__ == "__main__":
    # Run the script every 24 hours
    # Load existing generated facts
    generated_facts = load_generated_facts()

    # Set up OpenAI
    setup_openai()
    main()
    


