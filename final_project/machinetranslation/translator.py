""" py code to translate from Watson
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = '93xOaY8xJBISwiPUGQyWJ8X8T5KLwFzUxjjSNXbF5wg3'
url = 'https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/34186b23-6a4e-41b4-9422-810aa52c276a'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')


language = language_translator.identify(
    'Language translator translates text from one language to another').get_result()

def english_to_french(english_text):
    """ translate english to french
    """
    french_translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return french_translation.get("translations")[0].get("translation")

def french_to_english(french_text):
    """ translate french to english
    """
    english_translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_translation.get("translations")[0].get("translation")
