import requests
import random
import warnings

def detect_language(text):
    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')

        response = requests.post(
            'https://languages.cortical.io/rest/text/detect_language',
            headers=headers,
            verify=False,
            data=text.encode('utf-8')
        )

    return response.json()['iso_tag']


def detect_keywords(text, language=None):
    if language == None:
        language = detect_language(text)

    headers = {
        'User-Agent': ''.join(random.sample('abcdefghijklmnopqrstuvwxyz', 10))
    }

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')

        response = requests.post(
            f'https://languages.cortical.io/rest/text/keywords?retina_name={language}_general',
            headers=headers,
            verify=False,
            data=text.encode('utf-8')
        )

    try:
        return response.json()

    except:
        return []