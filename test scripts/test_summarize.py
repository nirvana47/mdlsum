# test_summarize.py
import os
from mdlsum.summarize import summarize_text

# Path to the long transcription file
file_path = os.path.join("downloads", "output.vtt")

# Read the content of the file
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Summarize the text
summary = summarize_text(text)

# Print the summary
print(summary)

# Path to the short transcription file
print("\nBeginning Short Transcription...\n")
file_path = os.path.join("downloads", "shortTranscription.lrc")

# Read the content of the file
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Summarize the text
summary = summarize_text(text)

# Print the summary
print(summary)