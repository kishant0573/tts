import streamlit as st
import pandas as pd
import os
import speech_recognition as sr

def main():
    st.title("Table Generator")

    # Create a DataFrame to store data
    df = create_empty_dataframe()

    # Get WAV file names from the 'kannad' folder
    wav_files = get_wav_files("kannad")

    if wav_files:
        # Update the DataFrame with WAV file names and convert audio to text
        update_dataframe(df, wav_files)

    # Display the table
    st.table(df)

def create_empty_dataframe():
    columns = [
        "HINDI AUDIO FILE",
        "POSSIBLE HINDI ASR SOLUTIONS",
        "POSSIBLE HINDI ASR SOLUTIONS IN TRANSLITERATION LETTER",
        "TEXT BOX FOR MANUAL CORRECTION",
        "CONVERTED TEXT FROM TRANSLITERATION TO HINDI",
        "BUTTON TO RUN PUNCTUATION MODELS",
        "PUNCTUATION MODELS",
        "TEXT BOX FOR MANUAL CORRECTION POST PUNCTUATION",
        "TRANSLITERATION FROM LEFT BOX",
        "BUTTON FOR RUN TTS",
        "TTS OF MANUAL CORRECTION"
    ]
    return pd.DataFrame(columns=columns, index=range(58))


def get_wav_files(folder_path):
    wav_files = []
    if os.path.exists(folder_path):
        wav_files = [file for file in os.listdir(folder_path) if file.endswith(".wav")]
    return wav_files[:58]  # Limit to 58 WAV files

def update_dataframe(df, wav_files):
    recognizer = sr.Recognizer()
    for i, wav_file in enumerate(wav_files):
        file_path = os.path.join("kannad", wav_file)
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio, language="hi-IN")  # Speech recognition in Hindi
                df.loc[i, "POSSIBLE HINDI ASR SOLUTIONS"] = text
            except sr.UnknownValueError:
                df.loc[i, "POSSIBLE HINDI ASR SOLUTIONS"] = "Could not understand audio"

        df.loc[i, "HINDI AUDIO FILE"] = wav_file

if __name__ == "__main__":
    main()
