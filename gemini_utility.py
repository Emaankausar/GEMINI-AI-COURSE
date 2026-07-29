import streamlit as st
import google.generativeai as genai

# Loading the API key from Streamlit Secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)


# Function to load Gemini chatbot
def load_gemini_pro_model():
    gemini_model = genai.GenerativeModel("gemini-2.5-flash")
    return gemini_model


# Function for image captioning
def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-2.5-flash")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result


# Function to get embeddings for text
def embedding_model_response(input_text):
    embedding = genai.embed_content(
        model="models/gemini-embedding-001",
        content=input_text,
        task_type="retrieval_document",
    )
    return embedding["embedding"]


# Function to get a response from Gemini
def gemini_pro_response(user_prompt):
    gemini_pro_model = genai.GenerativeModel("gemini-2.5-flash")
    response = gemini_pro_model.generate_content(user_prompt)
    result = response.text
    return result
