import streamlit as st

from subclass_memorable import *
from subclass_pin import *
from subclass_random import *

st.image("./images/password-generator.jpg", width=1000)
st.title("Password Generator")
st.divider()
st.write("What kind of password do you need to generate?")
user_choice=st.radio("Choose:",["Random Password","Memorable Password","Pin Code"])

if user_choice == "Pin Code":
    length=st.slider("select the length of pin you want to create:",4,32)
    generator=PinPass(length)
    password=generator.password_generator()
    st.write(f"Your pic code is: `{password}`")
elif user_choice == "Random Password":
    length=st.slider("select the length of random password you want to create:",8,50)
    include_symbol=st.checkbox("Include special characters?")
    include_numbers=st.checkbox("Include numbers?")
    generator=RandomPass(length,include_numbers,include_symbol)
    password=generator.password_generator()
    st.write(f"Your random password is: ````{password}````")
elif user_choice == "Memorable Password":
    num_words=st.slider("select the number of words you want to create:",1,10)
    seperator=st.text_input("Select a separator:","_")
    capitalization=st.checkbox("Capitalize the first letter of each word?")
    generator=MemorablePass(num_words,seperator,capitalization)
    password=generator.password_generator()
    st.write(f"Your memorable password is: `{password}`")