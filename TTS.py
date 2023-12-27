from gtts import gTTS
import pandas as pd
import os
import speech_recognition as sr

def text_to_speech(text, output_file='output.mp3'):
    """
    Convert text to speech using gTTS (Google Text-to-Speech) and save it to an audio file.

    Parameters:
    - text: The text to be converted to speech.
    - output_file: The path of the output audio file.
    """
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(output_file)

def audio_to_text(audio_file):
    """
    Convert audio to text using SpeechRecognition.

    Parameters:
    - audio_file: The path of the input audio file.

    Returns:
    - The recognized text.
    """
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language='en')

    return text

if _name_ == "_main_":
    # Load the Excel file
    excel_file_path = './ASTA_NO_VAD.csv'  # Replace with the path to your Excel file
    df = pd.read_csv(excel_file_path)

    # Output directory for audio files
    output_dir = './ASTA_NO_VAD'
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through the rows and convert text to audio
    for index, row in df.iterrows():
        text = row[0]  # Replace 'TextColumn' with the actual column name in your Excel file
        output_file_path = os.path.join(output_dir, f'audio_{index + 1}.mp3')  # Serial order naming

        text_to_speech(text, output_file=output_file_path)

        print(f"Speech saved to: {output_file_path}")

        # Convert audio to text
        recognized_text = audio_to_text(output_file_path)
        print(f"Recognized Text: {recognized_text}")