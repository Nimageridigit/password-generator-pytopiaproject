import random
import string

from parent_class import *

class PinPass(PasswordGenerator):

    def __init__(self, length: int=8):

        self.length=length
        self.chars: str = string.digits
        
    def password_generator(self):
        
        return ''.join(random.choice(self.chars) for _ in range(self.length))   

#test=PinPass()
#print(f"Pin password is: {test.password_generator()}")