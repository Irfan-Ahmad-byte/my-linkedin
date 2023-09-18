import datetime
import logging

import azure.functions as func

from TimerTrigger2.sub_modules.Main import main as main_post
from TimerTrigger2.sub_modules.azure_openai import setup_openai


def main(mytimer: func.TimerRequest) -> None:
    setup_openai()
    main_post()