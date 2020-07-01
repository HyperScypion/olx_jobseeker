import re


def clean_data(text):
    text = re.sub('<[^>]*>', '', text)
    text = re.sub('[0-9]*', '', text)
    text = re.sub(' +', ' ', text)
    text = text.strip()
    text = re.sub('[ ]$', '', text)
    text = re.sub('(\n|\r)+', '', text)
    return text
