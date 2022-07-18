import random

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

if text == 'Какая погода?':
    print(intens['weather'])

for intent_name in intens:
    for exaple in intens[intent_name]['examples']:
        if text == exaple:
            answer = random.choice(intens[intent_name]['responses'])
            print(answer)

