# Text-to-Speech Converter

This Streamlit app allows users to convert text to speech in multiple languages. Users can input text, select a language, and generate an audio file of the spoken text.

## Features

- Convert text to speech in 10 different languages
- Play audio directly in the browser
- Download the generated audio as an MP3 file

## Demo

App Link: https://text-to-speech-io.streamlit.app/

## Installation

To run this app locally, follow these steps:

1. Clone this repository:
   git clone https://github.com/Ajinkya2101/Multilingual-Text-to-Speech-App


3. Install the required packages:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py


## Usage

1. Enter the text you want to convert to speech in the text area.
2. Select the desired language from the dropdown menu.
3. Click the "Convert to Speech" button.
4. Use the audio player to listen to the generated speech.
5. Click the "Download Audio" button to save the MP3 file.

## Supported Languages

- English
- Spanish
- French
- German
- Italian
- Portuguese
- Russian
- Japanese
- Korean
- Chinese (Simplified)

## Dependencies

- streamlit
- gTTS (Google Text-to-Speech)

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web app framework
- [gTTS](https://github.com/pndurette/gTTS) for the text-to-speech conversion
