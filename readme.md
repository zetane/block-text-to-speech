# Text-to-Speech Conversion with TTS

This repository contains a script to convert textual descriptions into audio files using a text-to-speech (TTS) model. The script is designed to work with a specific TTS model from the `TTS` library.

## Requirements

- Python 3.x
- PyTorch
- TTS Library

## Installation

1. Clone the repository:

```bash
pip install torch TTS
Usage
The script provides a compute function to convert text to speech and save it as an audio file.

Function Definition
python
Copy code
def compute(prompt, audio_file_path):
    """Convert text to speech and save it as an audio file.

    Inputs:
        prompt (str): Textual description to be converted to audio.
        audio_file_path (str): Path to an existing audio file for speaker adaptation.

    Outputs:
        result (dict of str): Dictionary containing the path to the output audio file.
    """
Inputs
prompt (str): The text that you want to convert into speech.
audio_file_path (str): The path to an existing audio file used for speaker adaptation.
Outputs
result (dict of str): A dictionary containing the path to the output audio file.
Example
Here's an example of how to use the compute function:

python
Copy code
import torch
from TTS.api import TTS
import builtins

def compute(prompt, audio_file_path):
    """Convert text to speech and save it as an audio file.

    Inputs:
        prompt (str): Textual description of audio.
        audio_file_path (str): Path for audio file.

    Outputs:
        result (dict of str): List of Output file.
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

# Example usage
prompt = "Hello, this is a test."
audio_file_path = "path/to/existing/audio.wav"
output = compute(prompt, audio_file_path)
print(output)
This script uses the TTS library to perform the text-to-speech conversion. It adapts to the speaker's voice using an existing audio file.
