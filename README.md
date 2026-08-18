🎙️ Lucy — AI Voice Assistant
<p align="center"> <strong>A lightweight, low-latency AI voice assistant powered by Google Gemini 2.5 Flash.</strong> </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Gemini-2.5%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemini"> <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License"> </p> <p align="center"> <img src="https://img.shields.io/badge/Voice%20Assistant-AI-8A2BE2?style=flat-square" alt="AI Voice Assistant"> <img src="https://img.shields.io/badge/Text--to--Speech-pyttsx3-orange?style=flat-square" alt="Text to Speech"> <img src="https://img.shields.io/badge/Speech%20Recognition-Google-red?style=flat-square" alt="Speech Recognition"> </p>
📖 Overview

Lucy is a Python-based AI voice assistant designed for fast, natural voice interaction.

Lucy listens for the custom wake word "Lucy", responds with "Yes boss", processes the user's command, and either performs a predefined local action or sends the request to Google Gemini 2.5 Flash for an intelligent response.

The project focuses on keeping the architecture simple, lightweight, responsive, and easy to extend.

✨ Features
Feature	Description
🎙️ Wake Word Detection	Activates when the user says Lucy.
⚡ Low-Latency Interaction	Optimized speech recognition for responsive commands.
🤖 Gemini Integration	Uses Gemini 2.5 Flash for general-purpose AI queries.
🔊 Text-to-Speech	Converts responses into speech using pyttsx3.
🌐 Web Automation	Opens configured websites and media destinations using voice commands.
🧠 Command Routing	Separates local automation commands from AI-powered requests.
🔐 Secure Configuration	API credentials are loaded from environment variables.
🪶 Lightweight Design	Minimal architecture that is easy to customize and extend.
🏗️ System Architecture
flowchart TD
    A["🎙️ Microphone"] --> B["🗣️ Speech Recognition"]
    B --> C["🧠 Command Parser"]
    C --> D{"Wake Word / Command"}

    D -->|Local Command| E["⚙️ Local Automation"]
    D -->|AI Query| F["🤖 Gemini 2.5 Flash"]

    E --> G["🌐 Browser / Web Actions"]
    F --> H["💬 AI Response"]

    G --> I["🔊 pyttsx3"]
    H --> I

    I --> J["👤 User Hears Response"]

    style A fill:#1f2937,color:#fff
    style B fill:#2563eb,color:#fff
    style C fill:#7c3aed,color:#fff
    style E fill:#059669,color:#fff
    style F fill:#4285f4,color:#fff
    style I fill:#ea580c,color:#fff
    style J fill:#374151,color:#fff

🔄 Execution Flow
sequenceDiagram
    participant U as 👤 User
    participant M as 🎙️ Microphone
    participant S as 🗣️ Speech Recognition
    participant L as 🧠 Lucy
    participant G as 🤖 Gemini
    participant W as 🌐 Web Browser
    participant T as 🔊 TTS

    U->>M: Speak command
    M->>S: Capture audio
    S->>L: Convert speech to text

    L->>L: Check wake word

    alt Local command
        L->>W: Execute browser/web action
        W-->>L: Action completed
    else AI query
        L->>G: Send user request
        G-->>L: Generate response
    end

    L->>T: Send response
    T-->>U: Speak response

🗣️ How Lucy Works

The interaction follows a simple pipeline:

1. Listen → Lucy captures audio from the microphone.

2. Recognize → Speech recognition converts the audio into text.

3. Activate → Lucy checks for the wake word Lucy.

4. Understand → The command parser determines what the user wants.

5. Execute → Lucy either performs a local action or sends the request to Gemini.

6. Respond → The result is converted to speech using pyttsx3.

📁 Project Structure
Lucy---AI-Voice-Assistant/
│
├── main.py
├── mychannels.py
├── requirements.txt
├── .env
├── .gitignore
├── LICENSE
└── README.md

File Description
File	Purpose
main.py	Main application entry point and voice-assistant logic
mychannels.py	Web, channel, and media routing configuration
requirements.txt	Python package dependencies
.env	Local environment variables and API credentials
.gitignore	Prevents secrets and generated files from being committed
LICENSE	MIT License
README.md	Project documentation
🛠️ Technology Stack
Core
Python 3.9+
Google Gemini 2.5 Flash
Google Speech Recognition
pyttsx3
python-dotenv
What Each Technology Does
Python
  └── Application logic

Google Speech Recognition
  └── Converts voice → text

Gemini 2.5 Flash
  └── Handles intelligent AI queries

pyttsx3
  └── Converts text → voice

python-dotenv
  └── Loads environment variables securely

🚀 Getting Started
Prerequisites

Before installing Lucy, make sure you have:

Python 3.9 or newer
An active internet connection
A working microphone
Speakers or headphones
A valid Gemini API key
1. Clone the Repository
git clone https://github.com/bipulkumar62/Lucy---AI-Voice-Assistant.git
cd Lucy---AI-Voice-Assistant

2. Create a Virtual Environment
Windows
python -m venv .venv
.venv\Scripts\Activate.ps1

macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Your Gemini API Key

Create a file named .env in the root directory:

GEMINI_API_KEY=your_actual_gemini_api_key_here


Lucy loads the API key at runtime instead of storing it directly in the source code.

⚠️ Never commit your .env file to GitHub.

▶️ Running Lucy

Start the assistant with:

python main.py


Lucy will begin listening for the wake word.

Say:

Lucy


Lucy responds:

Yes boss


You can then give your command.

💬 Example Commands
Command	Expected Action
Lucy, open Google	Opens Google in the default browser
Lucy, open GitHub	Opens the configured GitHub destination
Lucy, open YouTube	Opens the configured YouTube destination
Lucy, open Bugatti	Opens the configured automotive/media destination
Lucy, what is quantum computing?	Sends the question to Gemini
Lucy, explain artificial intelligence	Generates an AI-powered explanation

The exact available commands depend on the logic implemented in main.py and mychannels.py.

🔐 Security

Lucy uses environment variables to keep API credentials outside the source code.

Credential Handling
import os

api_key = os.getenv("GEMINI_API_KEY")


The API key should be stored only in .env.

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

# IDE configuration
.vscode/
.idea/

# Operating system files
.DS_Store
Thumbs.db

⚠️ Important

Never write your API key directly inside Python code:

# ❌ Do NOT do this
api_key = "YOUR_SECRET_API_KEY"


Instead:

# ✅ Use environment variables
api_key = os.getenv("GEMINI_API_KEY")

🧩 Customization

Lucy is designed to be easy to customize.

You can extend the assistant by adding:

New voice commands
New websites
New media channels
Custom browser actions
Additional Gemini functionality
Desktop automation
Custom responses
Additional AI tools

Most command and channel customization can be handled through:

main.py
    ↓
Command processing
    ↓
mychannels.py
    ↓
Custom actions / destinations

🛠️ Troubleshooting
<details> <summary><strong>🎙️ Microphone is not working</strong></summary>

Make sure:

Your microphone is connected.
Your operating system recognizes the microphone.
Python has permission to access it.
The correct input device is selected.
Required audio dependencies are installed.
</details> <details> <summary><strong>🤖 Gemini requests are failing</strong></summary>

Check that your .env contains:

GEMINI_API_KEY=your_actual_gemini_api_key_here


Also verify that the API key is valid and that your internet connection is working.

</details> <details> <summary><strong>🗣️ Lucy does not recognize the wake word</strong></summary>

Speech recognition accuracy can be affected by:

Background noise
Microphone quality
Distance from the microphone
Incorrect audio input device
Network connectivity

Try speaking clearly and reducing background noise.

</details> <details> <summary><strong>🔊 No voice response</strong></summary>

Check your:

Speaker/headphone connection
System volume
pyttsx3 installation
Operating-system speech engine configuration
</details>
🔮 Future Improvements

The project can be expanded with:

 🧠 Conversation memory
 🎧 Continuous background listening
 🖥️ Desktop GUI
 🔌 Plugin-based command system
 🏠 Smart-home integration
 📂 File and application automation
 🌍 Multi-language support
 🗣️ More natural conversational responses
 🔒 Advanced permission and security controls
 📊 Usage and command analytics
🤝 Contributing

Contributions are welcome.

Create a feature branch
git checkout -b feature/your-feature

Make your changes

Implement and test your feature locally.

Commit your changes
git add .
git commit -m "Add: your feature"

Push the branch
git push origin feature/your-feature


Then open a Pull Request on GitHub.

📜 License

This project is licensed under the MIT License.

See the LICENSE file for more information.

👨‍💻 Author

Bipul Kumar

Python developer and creator of Lucy — AI Voice Assistant.

⭐ Support

If you find this project useful:

⭐ Star the repository
🍴 Fork the project
🐛 Report bugs
💡 Suggest improvements
🤝 Contribute to the project
<p align="center"> <strong>🎙️ Lucy — Listen. Understand. Automate.</strong> </p> <p align="center"> Built with ❤️ using Python and Google Gemini. </p>
