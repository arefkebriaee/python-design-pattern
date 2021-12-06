'''
    Adapter Design Pattern
        type: Structural
            main part => adaptee, adapter, client
'''


class Persian_language:
    _greeting_word = 'Dorood'

# --------------------------------------------------------------
# adapter


class Translator:
    _persian_greeting_word = None
    _translation = "Hello means Dorood"

    def __init__(self, greeting_word):
        self._persian_greeting_word = greeting_word._greeting_word

# --------------------------------------------------------------
# adaptee


class English_language:
    _adapter = None
    _greeting_word = 'Hello'

    def __init__(self, adapter):
        self._adapter = adapter

    def translate(self):
        translated_phrase = self._greeting_word + \
            ' means ' + self._adapter._persian_greeting_word
        if self._adapter._translation == translated_phrase:
            print('Hello translated correctly.')
        else:
            print('sorry, translator could not translate')

# --------------------------------------------------------------
# client


persian_word = Persian_language()
translator = Translator(persian_word)
english_word = English_language(translator)

english_word.translate()
