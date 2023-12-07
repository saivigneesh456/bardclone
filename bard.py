from bardapi import Bard
import streamlit as st
from streamlit_chat import message
import os

os.environ['_BARD_API_KEY'] = "dwgK4FeK3ArqMEnVzsVehzCpKcZbqfP8FkStLwx5X5d99xCEbye9nlsxKGj5patkbtm35A."

def response_api(prompt):
    response_message = Bard().get_answer(str(prompt))['content']
    return response_message

def user_input():
    input_text = st.text_input("Enter your question?")
    return input_text


if 'conversation' not in st.session_state:
    st.session_state.conversation = []

user_text = user_input()

if user_text:
   
    if any(keyword in user_text.lower() for keyword in ["last question", "previous question"]):
        if st.session_state.conversation:
            most_recent_question = st.session_state.conversation[-1]['user']
            st.session_state.conversation.append({'system': f"Your last question was: {most_recent_question}"})
        else:
            st.session_state.conversation.append({'system': "You haven't asked any questions yet."})
    else:
        
        response = response_api(user_text)
        st.session_state.conversation.append({'user': user_text, 'bard': response})


if st.session_state.conversation:
    for i, entry in enumerate(st.session_state.conversation):
        if 'user' in entry:
            message(entry['user'], is_user=True, key=str(i) + '_user')
        if 'system' in entry:
            message(entry['system'], key=str(i) + '_system')
        if 'bard' in entry:
            message(entry['bard'], key=str(i) + '_bard')
