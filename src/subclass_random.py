import random
import string

from parent_class import *

class RandomPass(PasswordGenerator):
    def __init__(self, length: int=8, include_number: bool= False, include_symbol: bool= False ):
        self.length = length
        self.include_number = include_number
        self.include_symbol = include_symbol
    def password_generator(self) -> str:
        chars = string.ascii_letters
        if self.include_number:
            chars += string.digits
        if self.include_symbol:
            chars += string.punctuation
        return ''.join(random.choice(chars) for _ in range(self.length))
    
#test= RandomPass()
#print(test.password_generator())
