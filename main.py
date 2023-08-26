import datetime
import re
import time

import pyautogui
import pytesseract
from PIL import ImageGrab
from pynput.keyboard import Controller, Key

keyboard = Controller()

pytesseract.pytesseract.tesseract_cmd = './Tesseract-OCR/tesseract.exe'  # tesseract executable path


def capture_screen_region():
    screen_width, screen_height = pyautogui.size()
    region_width = int(screen_width * 0.25)  # Adjust as needed depending on your screen size
    region_height = int(screen_height * 0.25)  # Adjust as needed depending on your screen size

    return ImageGrab.grab(bbox=(0, screen_height - region_height, region_width, screen_height))


def extract_and_solve_expression(screen_region):
    extracted_text = pytesseract.image_to_string(screen_region)

    # Search for the pattern in the extracted text
    match = re.search(r'\[SNK.SRV\] (\d+) ([+-/*]) (\d+) = \?\?', extracted_text)

    if match:
        num1, operator, num2 = int(match.group(1)), match.group(2), int(match.group(3))

        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2 if num2 != 0 else "Division by zero"
    return None


def main():
    last_answered = None

    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        screen_region = capture_screen_region()
        answer = extract_and_solve_expression(screen_region)

        if answer is not None and answer != last_answered:
            print(f"[{current_time}] Pattern found! The answer is: {answer}")

            # Simulate key presses and typing
            keyboard.press('y')
            keyboard.release('y')
            time.sleep(0.15)  # Adjust the delay based on game's response time

            # Type the answer and press Enter
            keyboard.type(str(int(answer)))
            time.sleep(0.1)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            # Update the last_answered
            last_answered = answer

        # sleep for 1 seconds before checking again
        # increase the value if you want to reduce CPU usage
        # decrease the value if your CPU is fast enough
        time.sleep(1)


if __name__ == "__main__":
    main()

