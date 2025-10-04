import random
import string

from parent_class import *

class RandomPass(PasswordGenerator):
    def __init__(self, length: int=8, include_number: bool= False, include_symbol: bool= False ):

        self.length = length
        self.characters: str = string.ascii_letters
        if include_number:
            self.characters += string.digits
        if include_number:
            self.characters += string.punctuation
    
    def password_generator(self) -> str:

        """
        Generate a password from specified characters.
        """
        return ''.join(random.choice(self.characters) for _ in range(self.length))
    
#test= RandomPass()
#print(test.password_generator())
