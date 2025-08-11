import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Try to find a female voice
female_voice = None
for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():
        female_voice = voice.id
        break

# If no female found, default to the first available
if female_voice:
    engine.setProperty('voice', female_voice)
else:
    print("No female voice found, using default voice.")

# Set speaking rate
engine.setProperty('rate', 150)

# Text to speak
text = "Hello! I am speaking with a female voice."

# Speak the text
engine.say(text)
engine.runAndWait()
