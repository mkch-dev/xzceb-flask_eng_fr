import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = "2023-04-03"


authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{version}',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.jp-tok.language-translator.watson.cloud.ibm.com')


def english_to_french(english_text):
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    # print(json.dumps(translation, indent=2, ensure_ascii=False))
    # print(type(frenchText["translations"][0]["translation"]))
    return french_text["translations"][0]["translation"]


def french_to_english(french_text):
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    # print(json.dumps(translation, indent=2, ensure_ascii=False))
    # print(type(englishText["translations"][0]["translation"]))
    return english_text["translations"][0]["translation"]


print(english_to_french("Hello, how are you today?"))
print(english_to_french("sun"))
print(french_to_english("Bonjour, comment vous êtes aujourd'hui?"))
