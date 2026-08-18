import os
import webbrowser
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

# Initialize TTS Engine
engine = pyttsx3.init()
engine.setProperty('rate', 190)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ask_gemini(prompt):
    """Sends prompt to Gemini and returns clean short text response"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry boss, I couldn't process that request."

# Initialize Recognizer
r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = False

if __name__ == "__main__":
    speak("Initializing Lucy...")
    print("Lucy is active. Say 'Lucy' followed by your command or question!")

    while True:
        try:
            with sr.Microphone() as source:
                print("\nListening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            command = r.recognize_google(audio).lower()
            print(f"You said: {command}")

            if "lucy" in command:
                speak("Yes boss")

                # Web Browser Commands
                if "open google" in command:
                    webbrowser.open("https://www.google.com")
                elif "open github" in command:
                    webbrowser.open("https://github.com/bipulkumar62")
                elif "open youtube" in command:
                    webbrowser.open("https://www.youtube.com/@Carszilla_ccxmn")
                
                # Ask Gemini if it's a general question
                elif "ask gemini" in command or "what is" in command or "who is" in command:
                    clean_prompt = command.replace("lucy", "").strip()
                    print(f"Asking Gemini: {clean_prompt}")
                    reply = ask_gemini(clean_prompt)
                    print(f"Lucy: {reply}")
                    speak(reply)

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Network error: {e}")
        except KeyboardInterrupt:
            print("\nStopping Lucy...")
            break