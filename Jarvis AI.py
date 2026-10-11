# JARVIS  AI

# Import Libraries
import speech_recognition as sr
import pyttsx3
import webbrowser

# music section
class MusicLibrary:
    music = {
        "play motivational song": "https://youtu.be/Jv4XQ08V3co?si=ap2kBKs2a2AZ0lzG",
        "play radha krishna song": "https://youtu.be/LYsuFNPYfEA?si=plRKIfEcxyhB2koS",
        "play kung fu panda vibe": "https://youtu.be/jlXIPtjICsk?si=5bb7UuFZIwSPnMfw",
        "play emotional song": "https://youtu.be/TquVlrEqPUQ?si=ke9IVczzCxkzSeTF",
    }


musicLibrary = MusicLibrary()

# Initialize Speech Recognizer
recognizer = sr.Recognizer()

# Speech Recognition Settings
recognizer.pause_threshold = 1.2
recognizer.non_speaking_duration = 0.5
recognizer.phrase_threshold = 0.3

# Text To Speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Personal Details for Jarvis.
def handle_personal_command(command):
    if "good morning" in command:
        print("🌅 Good morning, sir! 😊☀️")
        speak("Good morning, sir. I hope you have a wonderful day.")
        return True

    elif "good evening" in command:
        print("🌆 Good evening, sir! 😊✨")
        speak("Good evening, sir. How can I assist you?")
        return True

    elif "good night" in command:
        print("🌙 Good night, sir! 😴✨")
        speak("Good night, sir. Take care and have a peaceful night.")
        return True

    elif "how are you" in command:
        print("😊 Jarvis is doing great, sir! 🤖✨")
        speak("I am doing well, sir. Thank you for asking.")
        return True

    elif "who are you" in command:
        print("🤖 I am Jarvis, your personal AI assistant! 😊✨")
        speak(
            "Hello sir, I am Jarvis. "
            "I am your personal AI assistant, "
            "designed to help you with your questions and tasks."
        )
        return True

    elif "who made you" in command or "who make you" in command:
        print("👨‍💻 I was created by Abhijit! 🤖✨")
        speak(
            "Sir, I was created and developed by Abhijit. "
            "He built me as his personal AI assistant."
        )
        return True

    elif "what is your name" in command:
        print("🤖 My name is Jarvis! 😊")
        speak("My name is Jarvis, sir.")
        return True

    elif "what can you do" in command:
        print("🤖 I can assist you with many tasks! 😊✨")
        speak(
            "I can answer your questions, open websites, "
            "play music, and assist you with different tasks, sir."
        )
        return True

    elif "are you my friend" in command or "can we be friends" in command:
        print("🤝 Of course, sir! 😊✨")
        speak(
            "Of course, sir. We can be friends. "
            "I am always here to assist you."
        )
        return True

    elif "thank you" in command or "thanks" in command:
        print("😊 You're welcome, sir! 🤝✨")
        speak("You're welcome, sir.")
        return True

    return False

# AI section
from openai import OpenAI

client = OpenAI(api_key="")

def ask_ai(command):
    response = client.responses.create(
        model="gpt-6-luna",
        input=command
    )

    answer = response.output_text

    print("Jarvis...:", answer)
    speak(answer)

# Ai ask Code section.
def ask_question(source):
    speak("What do you want to know, sir?")

    try:
        question_audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=10
        )

        question = recognizer.recognize_google(
            question_audio
        ).lower()

        print(f"Question: {question}")

        ask_ai(question)

    except sr.UnknownValueError:
        print("Sorry sir I am not understand the question...")

    except sr.RequestError as e:
        print(f"Something Went Wrong....; {e}")

    except sr.WaitTimeoutError:
        print("Sorry Sir time out....")

# Open Apps Section
def process_command(command):
    if "open chatgpt" in command:
        speak("Opening ChatGPT sir")
        webbrowser.open("https://chatgpt.com/")

    elif "open cloud" in command:
        speak("Opening Claude sir")
        webbrowser.open(
            "https://claude.ai/project/019f6b1e-34d4-7116-ab99-bed1045a6142"
        )

    elif "open youtube" in command:
        speak("Opening YouTube sir")
        webbrowser.open("https://www.youtube.com/")

    elif "open pin" in command:
        speak("Opening Pinterest sir")
        webbrowser.open("https://www.pinterest.com/")

    elif "open github" in command:
        speak("Opening GitHub sir")
        webbrowser.open("https://github.com/")

    elif "open discord" in command:
        speak("Opening Discord sir")
        webbrowser.open("https://discord.com/channels/@me")

    # music command section
    elif "play kung fu panda song" in command:
        speak("playing kung fu panda vibe song sir")
        webbrowser.open(musicLibrary.music["play kung fu panda vibe"])

    elif "play motivational song" in command:
        speak("Playing motivational song sir")
        webbrowser.open(musicLibrary.music["play motivational song"])

    elif "play radha krishna song" in command:
        speak("Playing Radha Krishna song sir")
        webbrowser.open(musicLibrary.music["play radha krishna song"])

    elif "play emotional song" in command:
        speak("Playing emotional song sir")
        webbrowser.open(musicLibrary.music["play emotional song"])

    else:
        speak("Sorry sir, Try again please....")

# Wake Word Detection
def listen_for_wake_word(source):
    while True:
        try:
            audio = recognizer.listen(
                source,
                timeout=2,
                phrase_time_limit=2
            )

            word = recognizer.recognize_google(audio).lower()

            normalized = " ".join(
                "".join(
                    char if char.isalnum() else " "
                    for char in word
                ).split()
            )

            if "jarvis" in normalized:
                print("Activated.")
                speak("Yes")

                try:
                    command_audio = recognizer.listen(
                        source,
                        timeout=4,
                        phrase_time_limit=8
                    )

                    command = recognizer.recognize_google(
                        command_audio
                    ).lower()

                    print(f"Command: {command}")

                    if handle_personal_command(command):
                        pass

                    elif "i want ask" in command:
                        ask_question(source)

                    else:
                        process_command(command)

                except sr.UnknownValueError:
                    print("Could not understand the command.")

                except sr.RequestError as e:
                    print(f"Could not request results; {e}")

        except sr.UnknownValueError:
            pass

        except sr.RequestError as e:
            print(f"Could not request results; {e}")

        except sr.WaitTimeoutError:
            pass

# Start Jarvis AI
with sr.Microphone() as source:
    print("Loading Jarvis Sir...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Jarvis...")

    speak("Hello Sir")

    listen_for_wake_word(source)