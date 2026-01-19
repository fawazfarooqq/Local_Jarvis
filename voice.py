import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    
    # Configure Voice (Try to find a decent one)
    voices = engine.getProperty('voices')
    # On Windows, index 1 is usually a female voice, 0 is male (David).
    # You can change this index to find the voice you like.
    engine.setProperty('voice', voices[0].id) 
    
    # Speed adjustment
    engine.setProperty('rate', 170) 

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("AURIS systems initialized.")