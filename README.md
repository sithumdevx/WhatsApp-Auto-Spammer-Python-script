# WhatsApp Message Repeater / Desktop Auto-Typer

A lightweight, Python-based desktop automation tool built using `pyautogui` and `time` to automatically type and send repetitive messages to WhatsApp (desktop app or WhatsApp Web).

---

## Features

- **Countdown Timer**: Gives you 5 seconds (configurable) to switch to WhatsApp and focus on the message input box.
- **Easy Configuration**:
  - Direct modification via variables at the top of [`main.py`](file:///c:/Users/12sit/Documents/MessegeRepater/main.py)
  - Interactive terminal prompt on startup (press Enter for defaults or customize on the fly).
- **Keystroke Simulation**: Types each message via `pyautogui.write()` and sends it with `pyautogui.press('enter')`.
- **Progress Tracking**: Real-time console status (`Sent message X of Y`) and overall time summary.
- **Safety Fail-Safes**:
  - **Screen-corner failsafe**: Move your mouse cursor immediately to any corner of the screen to abort.
  - **Ctrl+C**: Gracefully stops the script from the terminal.

---

## Quick Start

### 1. Activate the Virtual Environment (Optional if running via `.venv\Scripts\python`)
In PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Run the Script
Using the project's virtual environment:
```powershell
.\.venv\Scripts\python.exe main.py
```
Or directly if the environment is activated:
```powershell
python main.py
```

### 3. Usage Steps
1. Run the script.
2. Select whether to use default settings or input custom text/count/delay.
3. During the countdown, quickly switch to your WhatsApp window and click inside the chat message box.
4. Let the tool type and send messages automatically.

---

## Safety & Emergency Stop

If you ever need to stop sending immediately:
- **Mouse Failsafe**: Quickly slam your mouse cursor into any corner of the screen.
- **Terminal Failsafe**: Return to the terminal and press `Ctrl + C`.
