from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import serpapi

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API And get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to set up image for Google Gemini Pro
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        return None

# Function to fetch health updates using SERP API
def get_health_updates():
    params = {
        "q": "health updates",  # Your search query
        "engine": "google",     # Search engine to use (Google in this case)
        "hl": "en",             # Language (English)
        "gl": "in",             # Country to search from (India)
        "api_key": os.getenv("SERP_API_KEY")  # Your SERP API key
    }
    
    search = serpapi.GoogleSearch(params)
    results = search.get_dict()
    
    health_updates = []
    for result in results['organic_results']:
        title = result['title']
        link = result['link']
        health_updates.append((title, link))
    
    return health_updates

# Streamlit app initialization
st.set_page_config(page_title="Gemini Health App")
st.header("Gemini Health App")

# User input for image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    # Button to trigger processing
    submit = st.button("Tell me the total calories")

    # Process input and show response
    if submit:
        try:
            input_prompt_template = """
            You are a nutrition expert analyzing food items from the image and calculating the total calories. Please provide details of each food item with their respective calorie intake in the following format:
            
            1. Food Item 1 - Calories
            2. Food Item 2 - Calories
            3. ...
            """
            image_data = input_image_setup(uploaded_file)
            if image_data is not None:
                response = get_gemini_response("", image_data, input_prompt_template)
                st.subheader("The Response is")
                st.write(response)
            else:
                st.warning("Please upload an image before processing.")
        except Exception as e:
            st.error(f"Error processing image: {e}")

# Display latest health updates fetched from SERP API
st.subheader("Latest Health Updates")
try:
    health_updates = get_health_updates()
    for title, link in health_updates:
        st.write(f"- [{title}]({link})")
except Exception as e:
    st.error(f"Error fetching health updates: {e}")
