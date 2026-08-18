# 🎙️ Lucy - AI Voice Assistant

Lucy is a Python-based virtual voice assistant capable of converting speech to text and providing text-to-speech responses using a custom female voice module.

## 🚀 Features

- **Voice Feedback:** Speaks using Windows text-to-speech engine with a female voice interface (`Microsoft Zira`).
- **Speech Recognition:** Listens to audio inputs via microphone.
- **Web Automation:** Integrates with the `webbrowser` library to open websites dynamically.

---

## 🛠️ Prerequisites

- **Python:** 3.11 or 3.12 (Recommended for PyAudio support on Windows)
- **OS:** Windows 10 / 11

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/lucy-voice-assistant.git](https://github.com/YOUR_USERNAME/lucy-voice-assistant.git)
   cd lucy-voice-assistant
   ```

2. **Create and activate a virtual environment:**
   ```powershell
   py -3.12 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

---

## 💻 Usage

Run the main script to start Lucy:

```powershell
python main.py
```

---

## 📦 Project Structure

```text
├── .venv/               # Virtual environment (ignored by Git)
├── .gitignore           # Git ignore settings
├── main.py              # Main application script
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```
