from Main import FACTS_FILE


import json


def load_generated_facts():
    try:
        with open(FACTS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []