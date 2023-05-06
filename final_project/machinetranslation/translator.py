"""
This module contains functions that translate English to French, French to English
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator   
)

language_translator.set_service_url('')

def english_to_french(english_text):
    """
    This function translates english text to french text
    """
    if english_text=="":
        return "No input"

    fr_translation = language_translator.translate(
        text = english_text,
        model_id='en-fr').get_result()
    
    french_text = fr_translation.get('translations')[0].get('translation')

    return french_text

def french_to_english(french_text):
    """
    This function translates french text to english text
    """
    if french_text=="":
        return "No input"

    en_translation = language_translator.translate(
        text = french_text,
        model_id='fr-en').get_result()
    
    english_text = en_translation.get('translations')[0].get('translation')
    return english_text
