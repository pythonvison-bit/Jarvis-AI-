# Jarvis AI 🤖

A Python-based personal voice assistant that can answer AI-powered questions, open websites, play music, and respond to personal commands using voice recognition and text-to-speech.

## Features

- Voice activation using the wake word "Jarvis"
- AI-powered question answering through the OpenAI API
- Speech recognition using your microphone
- Text-to-speech responses
- Website opening commands
- Music playback through YouTube links
- Personal commands and greetings
- Customizable music links and website commands

## Libraries Used

| Library | Purpose |
|---|---|
| `speech_recognition` | Recognizes spoken commands through the microphone |
| `pyttsx3` | Converts text responses into speech |
| `webbrowser` | Opens websites in the default browser |
| `openai` | Sends questions to the OpenAI API and receives AI responses |
| `os` | Reads the API key from an environment variable when configured securely |

**Note:** `os` is needed only if you configure the API key using an environment variable.

### Install the Required Libraries

```bash
pip install SpeechRecognition pyttsx3 openai pyaudio
```

## How to Use Jarvis AI

### 1. Start Jarvis AI

Run the Python file:

```bash
python main.py
```

Make sure your microphone is connected and working.

### 2. Activate Jarvis

Say:

**You:** "Jarvis"

**Jarvis:** "Yes"

Jarvis listens for your command after activation.

### 3. Ask AI Questions

Say:

**You:** "Jarvis"

**Jarvis:** "Yes"

**You:** "I want ask"

**Jarvis:** "What do you want to know, sir?"

**You:** "Explain Python functions."

Jarvis sends your question to the OpenAI API, displays the answer in the terminal, and speaks the response aloud.

**Important:** To use AI question answering, you must configure your own valid OpenAI API key. Make sure the model specified in the code is available to your API account.

### 4. Open Websites

Activate Jarvis and use commands such as:

- `open ChatGPT`
- `open cloud` — opens Claude
- `open YouTube`
- `open pin` — opens Pinterest
- `open GitHub`
- `open Discord`

Jarvis opens the selected website in your default browser.

### 5. Play Music

Activate Jarvis and say one of the supported commands:

- `play motivational song`
- `play radha krishna song`
- `play kung fu panda song`
- `play emotional song`

Jarvis opens the corresponding YouTube link.

### 6. Personal Commands

Jarvis also responds to commands such as:

- `good morning`
- `good evening`
- `good night`
- `how are you`
- `who are you`
- `who made you`
- `what is your name`
- `what can you do`
- `are you my friend`
- `thank you`

## Customize Your Music and Websites

Jarvis comes with a few default music links and website commands. You can easily customize them according to your preferences.

### Change the Music

Find the `MusicLibrary` class in the Python code:

```python
class MusicLibrary:
    music = {
        "play motivational song": "YOUR_YOUTUBE_LINK",
        "play radha krishna song": "YOUR_YOUTUBE_LINK",
        "play kung fu panda vibe": "YOUR_YOUTUBE_LINK",
        "play emotional song": "YOUR_YOUTUBE_LINK",
    }
```

Replace the existing YouTube URLs with your preferred music links.

**Tip:** Keep the command keys consistent with the corresponding music commands in `process_command()`. If you add a new song, add its command handling as well.

### Change the Websites

The website commands are defined inside the `process_command()` function.

You can replace the default URLs with your preferred websites or add new website commands.

For example:

```python
elif "open my website" in command:
    speak("Opening your website, sir")
    webbrowser.open("YOUR_WEBSITE_URL")
```

Replace `YOUR_WEBSITE_URL` with the website you want to open.

## OpenAI API Setup

Jarvis requires an OpenAI API key for AI-powered question answering.

1. Create an API key at https://platform.openai.com/api-keys
2. Configure the key securely using an environment variable.
3. Update the Python client to read that environment variable.
4. Ensure the selected model is available to your API account.

Never upload your real API key to GitHub.

**Windows PowerShell:**

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

Use the following Python configuration:

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

API usage may require billing or available credits. A ChatGPT subscription does not automatically include API usage.

## How Jarvis AI Works

1. Jarvis starts and initializes the microphone.
2. It listens for the wake word "Jarvis".
3. After activation, it listens for your command.
4. It checks whether the command is a personal command, an AI question, a website command, or a music command.
5. For AI questions, it sends the recognized question to the OpenAI API.
6. The AI response is printed in the terminal and spoken through text-to-speech.

## Troubleshooting

**Jarvis cannot recognize my voice**
- Check your microphone and internet connection.
- Speak clearly and reduce background noise.

**AI questions are not working**
- Check that your API key is configured correctly.
- Verify that your API account has access to the selected model.
- Check your API usage limits and billing status.

**Jarvis does not recognize a command**
- Say "Jarvis" first.
- Wait for the activation response.
- Use one of the supported commands.

**PyAudio installation fails**
- Check the installation requirements for your Python version and operating system.

## Author

**Abhijeet**

Built as a personal Python project to explore voice assistants, AI integration, and automation.

## License

Add a `LICENSE` file to specify how others may use, modify, and distribute this project.
