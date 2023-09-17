import datetime
import logging

import azure.functions as func

from .Main import main as main_post
from .azure_openai import setup_openai

# Path to the JSON file for storing generated facts
FACTS_FILE = 'generated_facts.json'

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    setup_openai()

    main_post()

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
