import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the speed and volume of the voice
engine.setProperty('rate', 100)  # 150 words per minute
engine.setProperty('volume', 0.8)  # 80% volume

# Get the text to voice from the user
text = input("Enter the text to voice: ")

# Convert the text to speech
engine.say(text)
engine.runAndWait()