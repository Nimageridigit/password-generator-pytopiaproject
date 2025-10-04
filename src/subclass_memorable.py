import random
import nltk
from nltk.corpus import words
from parent_class import *

nltk.download('words') # type: ignore

class MemorablePass(PasswordGenerator):
    def __init__(self, num_words: int=6,separator: str="_", capitalization: bool=False):
        self.num_words=num_words
        self.separator = separator
        self.capitalization=capitalization


    def password_generator(self) -> str:
        word_list = words.words() # type: ignore
        selected_words = random.sample(word_list, self.num_words) # type: ignore

        if self.capitalization == True:
            selected_words = [word.capitalize() for word in selected_words] # type: ignore

        password = self.separator.join(selected_words) # type: ignore
        return password

test = MemorablePass(num_words=5, separator='_', capitalization=True)
print(f'Memorable password is: {test.password_generator()}')
