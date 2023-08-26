# 🧮 SneakMath

A Python-based automation tool that captures specific math problems from the bottom left corner of the primary monitor, solves them, and inputs the answers into a game chat.

## 🌟 Features

- 📖 Uses local Tesseract OCR installation from the repository to detect and extract math problems.
- 🔢 Real-time problem solving.
- 🎮 Automates keyboard input for in-game chats.
- 🔍 Continuous scanning with adjustable delays.

## 📋 Requirements

- Python 3.8+
- `pyautogui`
- `pynput`
- `pytesseract`
- `Pillow`

## 🐍 Installing Python 3.8

SneakMath requires Python 3.8 to run. If you haven't already installed it, follow the instructions below:

### Windows OS

1. **Download the Installer**

   Visit the [official Python downloads page](https://www.python.org/downloads/release/python-386/) and download the installer for Python 3.8.6

2. **Run the Installer**

   Launch the installer. Ensure that you check the box that says ✔️ "**Add Python 3.8 to PATH**" at the bottom. This makes it easier to run Python from the command prompt.

3. **Installation**

   Click on `Install Now` and wait for the installation to complete.

4. **Verify Installation**

   Open a new command prompt or terminal window and type: `python --version`
   You should see `Python 3.8.x` displayed.


## 🛠 Installation

1. **Clone the Repository**
```git clone https://github.com/Penlo/SneakMath.git```

2. **Navigate to Project Directory**
```cd sneakmath```

3. **Install Python Libraries**
```pip install -r requirements.txt```

4. **Tesseract OCR Setup**

The Tesseract OCR executable is included within the `Tesseract-OCR` folder in the repository. Ensure your script or environment is correctly pointed to use this local version.

## 🎮 Usage

1. **Prepare the Game/Application**

Ensure it's running and in focus.

2. **Run the Script**
```python sneakmath.py```

3. **Wait for the Magic ✨**

The script scans the bottom-left corner for math problems, solves them, and types the answers in the chat.

## 🤝 Contribution

- 🍴 Fork this repository.
- 🎋 Create your feature branch (`git checkout -b feature/fooBar`).
- ✔️ Commit your changes (`git commit -am 'Add some fooBar'`).
- 🔄 Push to the branch (`git push origin feature/fooBar`).
- 📩 Open a new Pull Request.

## 🐞 Reporting Issues

We welcome feedback and bug reports! If you encounter any problems or have suggestions, please create an issue so we can address it. Follow the steps below to create an issue:

1. **Navigate to the Issues Tab**
   
   Go to the [Issues](https://github.com/Penlo/SneakMath/issues) tab of the GitHub repository.

2. **Check Existing Issues**

   Before creating a new issue, please check if someone else has reported the same problem or suggested the same enhancement. This helps avoid duplicate entries.

3. **Create a New Issue**

   If your issue or suggestion is not already listed, click on the "New Issue" button.

4. **Fill in the Issue Template**

   Provide as much information as possible in the issue template. Clear descriptions, steps to reproduce, and relevant screenshots can greatly assist in resolving issues faster.

5. **Submit**

   After filling in the necessary details, submit the issue.

We appreciate your patience as we work through reported issues, and we prioritize them based on impact and user feedback. Thanks for helping improve SneakMath!

