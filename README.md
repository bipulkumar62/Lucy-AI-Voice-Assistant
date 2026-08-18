# 🎙️ Lucy – AI Voice Assistant

Lucy is a lightweight, low-latency Python voice assistant powered by Google's **Gemini 2.5 Flash** model. It features custom wake-word recognition, fast system navigation, automated web integration, and secure environment variable handling for safe deployment.

---

## 🏗️ System Architecture

                  +-------------------+
                  |   Microphone Input|
                  +---------+---------+
                            |
                            v
               +------------+------------+
               |  Speech Recognition     |
               |  (Google Speech API)    |
               +------------+------------+
                            |
                            v
               +------------+------------+
               |    Command Parser       |
               |    "Lucy" Wake Word     |
               +-----+-------------+-----+
                     |             |
       +-------------+             +-------------+
       |                                         |
       v                                         v
+----------+----------+                   +----------+----------+|  Local Automations  |                   |   Gemini 2.5 Flash  ||  (Web & Channels)   |                   |    LLM Engine       |+----------+----------+                   +----------+----------+|                                         |+-------------+             +-------------+|             |v             v+-----+-------------+-----+|   pyttsx3 Speech Engine ||   ("Yes boss" / Reply)  |+-------------------------+
---

## ⚡ Execution Flow

[ User Speaks ] ──> [ Audio Capture ] ──> [ Threshold Check ]│▼[ Output Response ] <── [ pyttsx3 Engine ] <── [ Process Command ]│┌─────────────────────┴─────────────────────┐│                                           │[ Local Browser Action ]                  [ Gemini API Request ](e.g. YouTube, GitHub, Google)             (General Knowledge Queries)
---

## ✨ Features

- **Wake Word Detection:** Responds to `"Lucy"` with *"Yes boss"*.
- **Low-Latency Audio Processing:** Optimized listening threshold (`phrase_time_limit`) for fast recognition.
- **Gemini 2.5 Flash Integration:** Powered by the `google-genai` SDK for quick intelligence queries.
- **Automated Web Navigation:** Instant voice access to GitHub, LinkedIn, YouTube, and supercar media shorts.
- **Secure Configuration:** Zero exposure of API credentials using `.env` environment files and `.gitignore` rules.

---

## 🛠️ Project Structure

project-3-lucy/│├── main.py              # Main application entry point├── mychannels.py        # Channel/media routing module├── requirements.txt     # Dependency specifications├── .env                 # API Keys (Excluded from Git)├── .gitignore           # Git tracking exclusions└── README.md            # Project documentation
---

## 🚀 Getting Started

### Prerequisites

* Python 3.9 or higher
* Active Internet Connection
* Working Microphone & Speakers

### 1. Clone the Repository

```bash
git clone [https://github.com/bipulkumar62/Lucy---AI-Voice-Assistant.git](https://github.com/bipulkumar62/Lucy---AI-Voice-Assistant.git)
cd Lucy---AI-Voice-Assistant
2. Set Up Virtual EnvironmentBash# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
4. Configure API KeyCreate a .env file in the root folder of the project:Bash# Windows (PowerShell)
New-Item -ItemType File -Name .env
Add your Gemini API Key inside .env:Code snippetGEMINI_API_KEY=your_actual_gemini_api_key_here
Note: Never commit the .env file to version control. The included .gitignore file automatically excludes it.🏃 UsageRun the assistant from your terminal:Bashpython main.py
Example CommandsCommand PromptAction Executed"Lucy, open google"Launches Google in your default browser"Lucy, open github"Opens your GitHub profile"Lucy, open youtube"Opens your target YouTube channel"Lucy, open bugatti"Launches specified media link"Lucy, what is Quantum Computing?"Queries Gemini 2.5 Flash and speaks the response🔒 Security PolicyThis repository adheres to standard security practices for handling API credentials:Secrets are injected at runtime via python-dotenv.Virtual environments (.venv/) and .env files are explicitly ignored in .gitignore.Explicit API calls use dynamic variable resolution via os.getenv("GEMINI_API_KEY").📜 LicenseDistributed under the MIT License. See LICENSE for more information.
