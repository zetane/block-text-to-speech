import torch
from TTS.api import TTS
import builtins

def compute(prompt, audio_file_path):
    """A textual description of the compute function.

    Inputs:
        prompt (str): Textual description of audio
        audio_file_path (str): path for audio file

    Outputs:
        result (dict of str): List of Output file

    Requirements:
    """

    # Backup the original input function
    original_input = builtins.input

    # Define a new function that always returns 'y'
    def mock_input(prompt):
        print(prompt + "y")  # Optionally print the prompt and response
        return 'y'
    
    # Replace the input function with the mock_input function
    builtins.input = mock_input

    # Initialize TTS
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cpu")
    
    # Run TTS to convert text to speech
    wav = tts.tts(text=prompt, speaker_wav=audio_file_path, language="en")
    
    # Convert text to speech and save to a file
    tts.tts_to_file(text=prompt, speaker_wav=audio_file_path, language="en", file_path="output.wav")

    # Append output file to results
    result = ["output.wav"]

    # Restore the original input function after operations
    builtins.input = original_input

    return {"result": result}
