from bardapi import Bard
import streamlit as st
from streamlit_chat import message
import os
import time

os.environ['_BARD_API_KEY'] = "dwgK4FeK3ArqMEnVzsVehzCpKcZbqfP8FkStLwx5X5d99xCEbye9nlsxKGj5patkbtm35A."

# Bard = BardCookies(cookie_dict=cookie_dict)

def response_api(prompt):
    response_message = Bard().get_answer(str(prompt))['content']
    return response_message

def user_input():
    input_text = st.text_input("Enter your question?")
    return input_text

# Initialize session state variables
if 'generate' not in st.session_state:
    st.session_state.generate = []

if 'past' not in st.session_state:
    st.session_state.past = []

user_text = user_input()

if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)

# Check if 'generate' is not empty
if hasattr(st.session_state, 'generate') and st.session_state.generate:
    for i in range(len(st.session_state.generate) - 1, -1, -1):
        message(st.session_state.past[i], is_user=True, key=str(i) + '_user')
        message(st.session_state.generate[i], key=str(i))
