Lucy — AI Voice Assistant

Lucy is a lightweight Python voice assistant that provides voice-controlled commands, web automation, and AI-powered responses.

Features
Wake-word detection using Lucy
Voice command processing
Speech recognition
Text-to-speech responses
Web and browser automation
AI-powered responses
Environment-based configuration
Architecture
Local Command
AI Query
Microphone
Speech Recognition
Command Processing
Command Type
Web / System Action
AI Response
Text-to-Speech
Voice Output
Project Structure
Lucy---AI-Voice-Assistant/
│
├── main.py
├── mychannels.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md

File	Description
main.py	Main application
mychannels.py	Web and channel actions
requirements.txt	Project dependencies
.gitignore	Files excluded from Git
LICENSE	Project license
Requirements
Python 3.9+
Working microphone
Speakers or headphones
Internet connection
Installation
1. Clone the repository
git clone https://github.com/bipulkumar62/Lucy---AI-Voice-Assistant.git
cd Lucy---AI-Voice-Assistant

2. Create a virtual environment

Windows

python -m venv .venv
.venv\Scripts\Activate.ps1


macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure the application

Create a local .env file and add the required configuration values used by the application.

Do not commit .env or any credentials to the repository.

Usage

Run the application:

python main.py


Say:

Lucy


After activation, speak a supported command.

Examples
Lucy, open Google
Lucy, open GitHub
Lucy, open YouTube
Lucy, open Bugatti
Lucy, what is quantum computing?


Available commands depend on the configuration and implementation of the project.

Security

Keep sensitive configuration outside the source code.

The following files should remain local and should not be committed:

.env
.venv/


A suitable .gitignore should include:

.env
.venv/
__pycache__/
*.py[cod]


Never store API keys, passwords, tokens, or other credentials directly in the source code or README.

License

This project is licensed under the MIT License.

See the LICENSE file for details.
