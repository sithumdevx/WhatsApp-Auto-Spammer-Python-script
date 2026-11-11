# 🚀 WhatsApp Message Repeater / Desktop Auto-Typer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Library](https://img.shields.io/badge/automation-PyAutoGUI-brightgreen.svg)](https://pyautogui.readthedocs.io/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

A lightweight, automated desktop messaging tool written in Python. It simulates keystrokes using `pyautogui` to repeatedly send custom messages via **WhatsApp Desktop**, **WhatsApp Web**, or any chat interface.

---

## 🌟 Key Features

- **⏱️ Configurable Countdown Timer**: Gives you a 5-second countdown (configurable) to switch to your WhatsApp window and focus on the message box before typing begins.
- **⚙️ Interactive CLI Prompts**: Choose default settings with one keypress (Enter) or dynamically set custom messages, repeat counts, and delays directly in the terminal.
- **😍 Full Emoji & Unicode Support**: Seamlessly sends emojis (😘, ❤️, 🔥, etc.), Sinhala/Tamil fonts, and multi-language characters without dropping or skipping text using clipboard pasting (`pyperclip`).
- **📊 Real-Time Console Progress**: Live feedback displaying `Sent message X of Y` and total execution time summary upon completion.
- **🛡️ Dual Safety Fail-Safes**:
  - **Screen-Corner Fail-Safe**: Move your mouse pointer to any of the 4 screen corners to trigger an instant emergency stop.
  - **Terminal Interruption**: Stop execution anytime cleanly by pressing `Ctrl + C`.

---

## 📋 Prerequisites

- **Python 3.8+** installed on your machine.
- WhatsApp Desktop application or WhatsApp Web open in a browser.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sithumdevx/WhatsApp-Auto-Spammer-Python-script.git
cd WhatsApp-Auto-Spammer-Python-script
```

### 2. Create and Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> **Note:** If you get a script execution policy error in PowerShell, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

**On macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use

### 1. Run the Script
With your virtual environment activated:
```bash
python main.py
```
Or directly using the virtual environment interpreter on Windows:
```powershell
.\.venv\Scripts\python.exe main.py
```

### 2. Configure Your Session
When prompted:
```text
============================================================
      WHATSAPP MESSAGE REPEATER / AUTO-TYPER TOOL
============================================================
Current Configuration:
 - Message       : "The message text to send"
 - Repeat Count  : 500
 - Delay (sec)   : 0.5s
 - Countdown     : 5s
============================================================
Use default settings? [Y/n] (Press Enter for Yes):
```
- **Press Enter** (or type `y`) to accept defaults.
- **Type `n`** to enter a custom message text, repeat count, delay (seconds), and countdown.

### 3. Switch to WhatsApp
1. As soon as the timer begins (`Starting in 5 second(s)...`), click on your WhatsApp chat window.
2. Ensure the cursor is active inside the text input box.
3. Keep hands off the keyboard and mouse while the script is typing.

---

## ⚙️ Configuration Variables

You can also customize the default variables permanently inside [`main.py`](file:///c:/Users/12sit/Documents/MessegeRepater/main.py):

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `DEFAULT_MESSAGE` | `"Mama Oyata adarei ne menike ❤️"` | Default text string to be typed and sent. |
| `DEFAULT_REPEAT_COUNT` | `500` | Number of times the message will be sent. |
| `DEFAULT_DELAY` | `0.5` | Delay in seconds between successive messages. |
| `DEFAULT_COUNTDOWN` | `5` | Buffer countdown in seconds before sending starts. |
| `TYPING_INTERVAL` | `0.01` | Delay between each character typed. |

---

## 🛑 Emergency Stop & Safety

If you need to halt the script immediately at any point:
1. **Mouse Slam (Failsafe)**: Rapidly move your mouse cursor to **any corner of your screen** (`(0, 0)`, etc.). PyAutoGUI will trigger a `FailSafeException` and instantly abort.
2. **Terminal Break**: Focus back into the terminal and press `Ctrl + C`.

---

## ⚠️ Disclaimer & Responsible Use

> **Notice:** This project is intended for educational, testing, and personal productivity purposes only. Please use this tool responsibly and respect WhatsApp's [Terms of Service](https://www.whatsapp.com/legal/terms-of-service). Automated repetitive messaging / spamming can lead to temporary or permanent bans of your WhatsApp account.
