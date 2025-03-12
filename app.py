import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file (for local development)
load_dotenv()

# Set API key using Streamlit secrets or environment variables
openai.api_key = st.secrets.get("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", os.getenv("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"))


st.title("Adaptive AI Workspaces – MVP Prototype with TTS")

# Sidebar: Domain selection
st.sidebar.header("Settings")
domain = st.sidebar.selectbox("Select Domain", [
    "Personalized Learning", 
    "AI for Developers", 
    "Business Intelligence", 
    "Creative AI"
])

# Main area: Module-specific input
if domain == "Personalized Learning":
    st.header("Personalized Learning Module")
    st.write("Features: AI Tutor, Exam Prep, Text-to-Audio Summarization")
    query = st.text_input("Enter your academic query or topic:")
    option = st.radio("Choose a feature:", (
        "AI Tutor", 
        "Exam Prep", 
        "Text-to-Audio Summarization (Demo)"
    ))
    
elif domain == "AI for Developers":
    st.header("AI for Developers Module")
    st.write("Features: Code Completion, Bug Detection, Documentation Generation")
    query = st.text_input("Enter your coding question or issue:")
    option = st.radio("Choose a feature:", (
        "Code Completion", 
        "Bug Detection", 
        "Documentation Generation"
    ))
    
elif domain == "Business Intelligence":
    st.header("Business Intelligence Module")
    st.write("Features: Financial Insights, Predictive Analytics, Smart Automation")
    query = st.text_input("Enter your business or financial query:")
    option = st.radio("Choose a feature:", (
        "Financial Insights", 
        "Predictive Analytics", 
        "Smart Automation"
    ))
    
elif domain == "Creative AI":
    st.header("Creative AI Module")
    st.write("Features: AI-Generated Music, Video Editing Assistant, Storytelling/Meme Generation")
    query = st.text_input("Enter your creative prompt or idea:")
    option = st.radio("Choose a feature:", (
        "AI-Generated Music", 
        "Video Editing Assistant", 
        "Storytelling/Meme Generation"
    ))

if st.button("Get Adaptive Response"):
    if query:
        # Construct a domain- and feature-specific prompt
        prompt = ""
        if domain == "Personalized Learning":
            if option == "AI Tutor":
                prompt = f"Act as an experienced tutor. Provide a detailed explanation on: {query}"
            elif option == "Exam Prep":
                prompt = f"Act as an exam preparation assistant. Generate practice questions and key summary points for: {query}"
            elif option == "Text-to-Audio Summarization (Demo)":
                prompt = f"Summarize the following text in a concise manner suitable for audio narration: {query}"
                
        elif domain == "AI for Developers":
            if option == "Code Completion":
                prompt = f"Provide an enhanced code snippet or completion suggestion for the following coding problem: {query}"
            elif option == "Bug Detection":
                prompt = f"Act as an expert debugger. Identify potential bugs and suggest fixes for this code issue: {query}"
            elif option == "Documentation Generation":
                prompt = f"Generate clear and concise documentation for the following code snippet or function: {query}"
                
        elif domain == "Business Intelligence":
            if option == "Financial Insights":
                prompt = f"Act as a financial analyst. Provide detailed insights and recommendations for: {query}"
            elif option == "Predictive Analytics":
                prompt = f"Predict future trends and suggest strategies based on the following business data: {query}"
            elif option == "Smart Automation":
                prompt = f"Act as an automation consultant. Provide suggestions on automating business processes for: {query}"
                
        elif domain == "Creative AI":
            if option == "AI-Generated Music":
                prompt = f"Act as a music composer. Create a concept for an original piece of music inspired by: {query}"
            elif option == "Video Editing Assistant":
                prompt = f"Act as a video editing expert. Suggest creative edits or a storyline for a video based on: {query}"
            elif option == "Storytelling/Meme Generation":
                prompt = f"Generate a creative story or meme concept based on: {query}"
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7,
            )
            adaptive_response = response.choices[0].message['content'].strip()
            st.subheader("Adaptive Response:")
            st.write(adaptive_response)
            
            # Text-to-Speech Conversion using gTTS
            tts = gTTS(text=adaptive_response, lang='en')
            tts.save("response.mp3")
            audio_file = open("response.mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please enter a query.")
