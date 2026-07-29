import os.path

import os

from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

from gemini_utility import (load_gemini_pro_model,
                            gemini_pro_vision_response,
                            embedding_model_response,
                            gemini_pro_response)

st.set_page_config(
    page_title="Gemini AI",
    page_icon="🧠",
    layout="centered"
)

with st.sidebar:
    selected = option_menu(
        "Gemini AI",
        ["ChatBot", "Image Captioning", "Embed text", "Ask me anything"],
        menu_icon="robot",
        default_index=0
    )


def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    return user_role


if selected == "ChatBot":

    model = load_gemini_pro_model()

    # Initialize chat session
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # Streamlit page title
    st.title("🤖 ChatBot")

    # Display chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # User input
    user_prompt = st.chat_input("Ask Gemini Pro...")

    if user_prompt:
        with st.chat_message("user"):
            st.markdown(user_prompt)

        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)


# Image Captioning Page
if selected == "Image Captioning":

    #streamlit page title
    st.title("📷 Snap Narrate")

    uploaded_image = st.file_uploader("upload an image...", type=["jpg, jpeg", "png"])

    if st.button("Generate Caption"):

        image = Image.open(uploaded_image)

        col1,col2 = st.columns(2)

        with col1:
            resized_image = image.resize((800, 500))
            st.image(resized_image)

        default_prompt = "write a short caption for this image"

        #getting the response from gemini-pro-vision model
        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)

#text embedding page
if selected == "Embed text":

    st.title("🔤Embed text")

    #input text box
    input_text = st.text_area(label='', placeholder="Enter the text to get the embeddings")

    if st.button("get embeddings"):
        response = embedding_model_response(input_text)
        st.markdown(response)


#question answering page
if selected == "Ask me anything":

    st.title("❓Ask me a question")

    #text box to enter prompt
    user_prompt = st.text_area(label="", placeholder="ask Gemini-Pro...")

    if st.button("Get an answer"):
        response = gemini_pro_response(user_prompt)
        st.markdown(response)

