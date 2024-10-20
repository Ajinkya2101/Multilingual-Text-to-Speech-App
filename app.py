import streamlit as st
from gtts import gTTS
import os
import tempfile
import time

def text_to_speech(text, language):
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the audio file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        return fp.name

def main():
    st.title("Text to Speech Converter")

    # Text input
    text = st.text_area("Enter the text you want to convert to speech:", height=150)

    # Language selection
    languages = {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Italian": "it",
        "Portuguese": "pt",
        "Russian": "ru",
        "Japanese": "ja",
        "Korean": "ko",
        "Chinese": "zh-cn"
    }
    selected_language = st.selectbox("Select the language:", list(languages.keys()))

    if st.button("Convert to Speech"):
        if text.strip() == "":
            st.warning("Please enter some text to convert.")
        else:
            with st.spinner("Converting text to speech..."):
                audio_file = text_to_speech(text, languages[selected_language])
                
                # Display audio player
                st.audio(audio_file, format="audio/mp3")
                
                # Provide download button
                st.download_button(
                    label="Download Audio",
                    data=open(audio_file, "rb"),
                    file_name="text_to_speech.mp3",
                    mime="audio/mp3"
                )
            
            st.success("Text converted to speech successfully!")

    st.markdown("---")
    st.write("Created by Ajinkya")

if __name__ == "__main__":
    main()