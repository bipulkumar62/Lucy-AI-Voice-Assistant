import os
import sys
import webbrowser
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from google import genai

# -------------------------------------------------------------------
# 1. SETUP & CONFIGURATION
# -------------------------------------------------------------------

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def speak(text):
    """Voice output through pyttsx3 engine"""
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 185)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"TTS Error: {e}")

def open_url(url):
    """Guaranteed Web Browser Opener across Windows/Mac/Linux"""
    try:
        # Standard Browser Open
        webbrowser.open_new_tab(url)
    except Exception:
        # Fallback OS system launch if default browser fails
        if sys.platform == "win32":
            os.system(f'start {url}')
        elif sys.platform == "darwin":
            os.system(f'open {url}')
        else:
            os.system(f'xdg-open {url}')

def ask_gemini(prompt):
    """Gemini API call with voice-optimized output limit"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Respond in 1 simple short sentence for voice assistant output: {prompt}",
        )
        return response.text.strip()
    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry boss, I couldn't process that request."

r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = False

# -------------------------------------------------------------------
# 2. MAIN VOICE ASSISTANT LOOP
# -------------------------------------------------------------------

if __name__ == "__main__":
    speak("Initializing Lucy...")
    print("Lucy active hai! Say 'Lucy' followed by your command.")

    while True:
        try:
            with sr.Microphone() as source:
                print("\nListening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            command = r.recognize_google(audio).lower().strip()
            print(f"You said: {command}")

            # Detect wake word
            if "lucy" in command:
                # 🔊 Voice reply
                speak("Yes boss")

                # --- 1. BROWSER COMMANDS (DIRECT KEYWORD CHECK) ---
                if "youtube" in command:
                    print("--> Opening YouTube...")
                    speak("Opening YouTube")
                    open_url("https://www.youtube.com")

                elif "google" in command:
                    print("--> Opening Google...")
                    speak("Opening Google")
                    open_url("https://www.google.com")

                elif "github" in command:
                    print("--> Opening GitHub...")
                    speak("Opening GitHub")
                    open_url("https://github.com")

                # --- 2. GEMINI AI QUESTION ANSWERING ---
                else:
                    clean_prompt = command.replace("lucy", "").strip()
                    if clean_prompt:
                        print(f"Asking Gemini: {clean_prompt}")
                        reply = ask_gemini(clean_prompt)
                        print(f"Lucy: {reply}")
                        speak(reply)

        except (sr.WaitTimeoutError, sr.UnknownValueError):
            pass
        except sr.RequestError as e:
            print(f"Network error: {e}")
        except KeyboardInterrupt:
            print("\nStopping Lucy...")
            break