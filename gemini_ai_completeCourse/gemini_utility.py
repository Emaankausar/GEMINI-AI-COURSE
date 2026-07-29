import os
import json

import google.generativeai as genai

working_directory = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_directory}/config.json"

with open(config_file_path, "r") as file:
    config_data = json.load(file)

# loading the API key
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

genai.configure(api_key=GOOGLE_API_KEY)

#function to load gemini chatbot
def load_gemini_pro_model():
    gemini_model = genai.GenerativeModel("gemini-2.5-flash")
    return gemini_model

#function for image captioning
def gemini_pro_vision_response(prompt, image):
    gemini_pro_vision_model = genai. GenerativeModel("gemini-2.5-flash")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result

#function to get embeddings for text
# function to get embeddings for text
def embedding_model_response(input_text):
    embedding = genai.embed_content(
        model="models/gemini-embedding-001",
        content=input_text,
        task_type="retrieval_document",
    )
    return embedding["embedding"]

#function to get a response from gemini-pro response
def gemini_pro_response(user_prompt):
    gemini_pro_model = genai.GenerativeModel("gemini-2.5-flash")
    response = gemini_pro_model.generate_content(user_prompt)
    result = response.text
    return result

