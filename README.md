🎙️ Lucy — AI Voice Assistant

Lucy is a lightweight, low-latency Python voice assistant powered by Google Gemini 2.5 Flash. It combines voice recognition, custom wake-word detection, web automation, local system actions, text-to-speech responses, and secure environment-variable configuration into a simple and extensible assistant.

Wake Word: Lucy
Response: "Yes boss"
Core Language: Python
AI Engine: Google Gemini 2.5 Flash

✨ Features
🎙️ Custom Wake-Word Detection — Activates when the user says Lucy.
⚡ Low-Latency Voice Interaction — Optimized speech recognition for responsive commands.
🤖 Gemini 2.5 Flash Integration — Uses Google's Gemini model for general-purpose AI queries.
🔊 Text-to-Speech Responses — Provides spoken responses using pyttsx3.
🌐 Voice-Controlled Web Navigation — Opens services such as Google, GitHub, YouTube, and other configured media links.
🧠 Command Routing — Separates predefined local actions from general AI requests.
🔐 Secure API Configuration — API credentials are loaded through environment variables and excluded from Git.
🪶 Lightweight Architecture — Designed to remain simple, fast, and easy to extend.
🏗️ System Architecture
                        ┌──────────────────────┐
                        │   🎙️ Microphone      │
                        │       Input          │
                        └──────────┬───────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │  Speech Recognition  │
                        │   Google Speech API  │
                        └──────────┬───────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │    Command Parser    │
                        │    "Lucy" Wake Word  │
                        └──────────┬───────────┘
                                   │
                     ┌─────────────┴─────────────┐
                     │                           │
                     ▼                           ▼
          ┌─────────────────────┐      ┌─────────────────────┐
          │ Local Automation    │      │  Gemini 2.5 Flash   │
          │                     │      │     AI Engine       │
          │ • Browser Actions   │      │                     │
          │ • Web Navigation    │      │ • Questions         │
          │ • Custom Channels   │      │ • General Knowledge │
          └──────────┬──────────┘      └──────────┬──────────┘
                     │                            │
                     └─────────────┬──────────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │   pyttsx3 TTS Engine │
                        │    Spoken Response   │
                        └──────────────────────┘

🔄 Execution Flow
┌────────────────┐
│  User Speaks   │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│ Audio Capture  │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│ Speech-to-Text │
└───────┬────────┘
        │
        ▼
┌────────────────┐
│ Wake Word /    │
│ Command Parser │
└───────┬────────┘
        │
        ├───────────────────────┐
        │                       │
        ▼                       ▼
┌────────────────┐      ┌─────────────────┐
│ Local Command  │      │ Gemini API      │
│ / Web Action   │      │ Request         │
└───────┬────────┘      └────────┬────────┘
        │                        │
        └────────────┬───────────┘
                     │
                     ▼
              ┌──────────────┐
              │ TTS Response │
              │   pyttsx3    │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │ User Hears   │
              │   Response   │
              └──────────────┘

📁 Project Structure
Lucy---AI-Voice-Assistant/
│
├── main.py              # Main application entry point
├── mychannels.py        # Web/channel routing and media actions
├── requirements.txt     # Python dependencies
├── .env                 # Local API credentials (not committed)
├── .gitignore           # Git exclusion rules
├── LICENSE              # MIT License
└── README.md            # Project documentation

🚀 Getting Started
Prerequisites

Before running Lucy, make sure you have:

Python 3.9 or newer
An active internet connection
A working microphone
Working speakers or headphones
A Gemini API key
1. Clone the Repository

Using GitHub CLI:

gh repo clone bipulkumar62/Lucy---AI-Voice-Assistant
cd Lucy---AI-Voice-Assistant


Or clone the repository using your preferred Git client.

2. Create a Virtual Environment
Windows — PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1

macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the project root:

GEMINI_API_KEY=your_actual_gemini_api_key_here


Lucy reads the API key at runtime rather than storing credentials directly in the source code.

⚠️ Never commit your .env file to Git.

▶️ Usage

Start Lucy from the project directory:

python main.py


Once Lucy is running, speak the wake word:

Lucy


Lucy responds:

Yes boss


You can then issue a supported command.

🗣️ Example Commands
Voice Command	Action
Lucy, open Google	Opens Google in the default browser
Lucy, open GitHub	Opens the configured GitHub destination
Lucy, open YouTube	Opens the configured YouTube destination
Lucy, open Bugatti	Opens the configured automotive/media link
Lucy, what is quantum computing?	Sends the question to Gemini and speaks the response

Available commands depend on the actions configured in main.py and mychannels.py.

🔐 Security

Lucy is designed to keep sensitive configuration outside the source code.

Security practices
API credentials are stored in .env.
.env is excluded from version control through .gitignore.
Python virtual environments are excluded from Git.
API credentials are accessed dynamically through environment variables.
Secrets should never be hard-coded into Python files or committed to the repository.

Example:

import os

api_key = os.getenv("GEMINI_API_KEY")

Recommended .gitignore
# Environment variables
.env
.env.*

# Virtual environments
.venv/
venv/

# Python cache
__pycache__/
*.py[cod]

# IDE files
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

🧩 Technology Stack
Technology	Purpose
Python	Core application language
Google Gemini 2.5 Flash	AI-powered responses
Google Speech API	Speech recognition
pyttsx3	Text-to-speech
python-dotenv	Environment variable management
Web Browser Automation	Voice-controlled web navigation
⚙️ Configuration

Lucy can be extended by modifying the command-routing logic and channel configuration.

Typical customization areas include:

main.py
├── Wake-word handling
├── Speech recognition
├── Command processing
├── Gemini requests
└── Text-to-speech responses

mychannels.py
├── Website shortcuts
├── Media channels
├── Custom URLs
└── Voice-triggered actions


This makes it straightforward to add new voice commands and automation workflows.

🛠️ Troubleshooting
Microphone is not detected

Check that:

Your microphone is connected.
Python has permission to access the microphone.
Your operating system has the correct input device selected.
Required audio dependencies are installed correctly.
Gemini requests fail

Verify that:

GEMINI_API_KEY=your_actual_gemini_api_key_here


is present in .env and that the API key is valid.

Lucy does not respond to the wake word

Make sure the microphone is working and that the speech-recognition component is receiving audio clearly. Background noise can also affect recognition accuracy.

🔮 Future Improvements

Potential improvements for Lucy include:

🎧 Continuous background listening
🧠 Conversation memory
🖥️ Desktop application interface
🔌 Plugin-based command system
🏠 Smart-home integrations
📂 File and application automation
🗣️ More natural conversational interaction
🌍 Multi-language voice support
🔒 Additional security and permission controls
🤝 Contributing

Contributions, ideas, and improvements are welcome.

A typical contribution workflow is:

git checkout -b feature/your-feature


Make your changes, test them locally, and submit a pull request with a clear description of the improvement.

📜 License

This project is distributed under the MIT License.

See the LICENSE file for the complete license text.

👨‍💻 Author

Bipul Kumar

Built with Python, voice recognition, automation, and Gemini AI.

⭐ Support the Project

If you find Lucy useful or interesting, consider giving the repository a ⭐ on GitHub and sharing it with other developers interested in AI voice assistants.

Lucy — Listen. Understand. Automate.
