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