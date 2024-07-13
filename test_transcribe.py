# test_transcribe.py
from transcribe import transcribe_audio

audio_file = "downloads/Bidens High-Stakes NATO News Conference Analyzed  WSJ_16bit.wav"  # Replace with the actual path to the downloaded WAV file
transcript = transcribe_audio(audio_file)
print(f"Transcript: {transcript}")