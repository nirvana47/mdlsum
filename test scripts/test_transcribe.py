# test_transcribe.py
from mdlsum.transcribe import transcribe_audio

audio_file = "downloads/output.wav"  # Replace with the actual path to the downloaded WAV file
transcript = transcribe_audio(audio_file)
print(f"Transcript: {transcript}")