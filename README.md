Lucy — AI Voice Assistant

Lucy is a lightweight Python voice assistant for hands-free web navigation, local command execution, and AI-powered questions. Say “Lucy”, speak a command, and receive a spoken response.




Features

Wake-word activation with “Lucy”

Speech-to-text command capture

Text-to-speech responses

Web and browser automation

Local command handling

AI-powered answers for general questions

Environment-based configuration for sensitive values

How It Works

flowchart TD
    A[Microphone input] --> B[Speech recognition]
    B --> C{Wake word detected?}
    C -- No --> A
    C -- Yes --> D[Extract spoken command]
    D --> E{Classify intent}
    E -- Local command --> F[Run local action]
    E -- Web command --> G[Open web resource]
    E -- AI question --> H[Request AI response]
    F --> I[Build response]
    G --> I
    H --> I
    I --> J[Text-to-speech]
    J --> K[Voice output]

Project Structure

Lucy---AI-Voice-Assistant/
├── main.py           # Application entry point
├── mychannels.py     # Web and channel actions
├── requirements.txt  # Python dependencies
├── .gitignore        # Git exclusion rules
├── LICENSE           # MIT license
└── README.md          # Project documentation

Prerequisites

Python 3.9 or later

A working microphone

Speakers or headphones

An internet connection for web and AI features

Installation

Clone the repository:

git clone https://github.com/bipulkumar62/Lucy---AI-Voice-Assistant.git
cd Lucy---AI-Voice-Assistant

Create and activate a virtual environment:

Windows (PowerShell)

python -m venv .venv
.\.venv\Scripts\Activate.ps1

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

Install the dependencies:

python -m pip install -r requirements.txt

Create a .env file in the project root and add the configuration values required by your implementation:

# Add required API keys and configuration here.

Never commit .env or expose credentials in source code.

Usage

Start Lucy:

python main.py

Say “Lucy”, followed by a command. For example:

Lucy, open Google
Lucy, open GitHub
Lucy, open YouTube
Lucy, open Bugatti
Lucy, what is quantum computing?

The available commands depend on the actions and services configured in the project.

Troubleshooting

Lucy cannot hear you: Confirm that the correct microphone is selected and that terminal microphone permission is enabled.

No voice response: Check the system volume and verify that a text-to-speech voice is available.

A web or AI command fails: Confirm the internet connection and check the values in .env.

A module is missing: Reactivate the virtual environment and rerun python -m pip install -r requirements.txt.

Security

Keep API keys, tokens, passwords, and other secrets in .env. At minimum, ensure .gitignore contains:

.env
.venv/
__pycache__/
*.py[cod]
