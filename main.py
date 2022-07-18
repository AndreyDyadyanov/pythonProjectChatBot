import random
import re
import nltk

def get_intent(text):
    for intent_name in intens:
        for exaple in intens[intent_name]['examples']:
            if text_math(text, exaple):
                return intent_name

def get_response(intent):
    return random.choice(intens[intent]['responses'])

def clean_up(text):
    text = text.lower()

    re_not_word = r'[^\w\w]'
    text = re.sub(re_not_word, '', text)

    return text

def text_math(user_text, example):
    user_text = clean_up(user_text)
    example = clean_up(example)

    if user_text.find(example) != -1:
        return True

    if example.find(user_text) != -1:
        return True

    exaple_len = len(example)
    differens = nltk.edit_distance(user_text, example)

    return (differens / exaple_len) < 0.4

intens = {
    'hello': {
        'examples': ['Хелло', 'Привет', 'Здравствуйте'],
        'responses': ['Добрый день', 'Как дела?', 'Как настроение?']
    },
    'weather': {
        'examples': ['Какая погода?', 'Что за окном?', 'Во что одеваться?'],
        'responses': ['Погода отличная!', 'У природы нет плохой погоды!'],
    }
}

text = input('Введите: ')
intent = get_intent(text)
answer = get_response(intent)
print(answer)