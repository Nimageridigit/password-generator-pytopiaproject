from subclass_random import RandomPass
from subclass_pin import PinPass
from subclass_memorable import MemorablePass   

def main():
    random_pass = RandomPass(length=12, include_number=True, include_symbol=True)
    pin_pass = PinPass(length=6)
    memorable_pass = MemorablePass(num_words=4, separator='-', capitalization=True)

    print(f"Random Password: {random_pass.password_generator()}")
    print(f"PIN Password: {pin_pass.password_generator()}")
    print(f"Memorable Password: {memorable_pass.password_generator()}")

if __name__ == "__main__":
    main()