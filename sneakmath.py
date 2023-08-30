import datetime
import re
import time
import pyautogui
import pytesseract
from PIL import ImageGrab
from pynput.keyboard import Controller, Key

# constants
pytesseract.pytesseract.tesseract_cmd = './Tesseract-OCR/tesseract.exe'

# adjustable variables
percentage_of_width_to_capture_from_bottom_left_corner = 0.25 # example: 1920px * 0.25 = 480px
percentage_of_height_to_capture_from_bottom_left_corner = 0.25 # example: 1080px * 0.25 = 270px
time_before_next_capture = 1 # increase to reduce CPU usage, decrease to increase CPU usage
time_before_writing_answer = 0.15
time_before_pressing_enter = 0.1


def capture_screen_region():
    screen_width, screen_height = pyautogui.size()
    region_width = int(screen_width * percentage_of_width_to_capture_from_bottom_left_corner)
    region_height = int(screen_height * percentage_of_height_to_capture_from_bottom_left_corner)

    return ImageGrab.grab(bbox=(0, screen_height - region_height, region_width, screen_height))


def extract_and_solve_expression(screen_region):
    extracted_text = pytesseract.image_to_string(screen_region)

    # search for the pattern in the extracted text
    match = re.search(r'\[SNK.SRV\] (\d+) ([+-/*]) (\d+) = \?\?', extracted_text)
    if not match return None

    num1, operator, num2 = int(match.group(1)), match.group(2), int(match.group(3))

    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Division by zero"
    }
    
    return operations[operator]


def main():
    keyboard = Controller()
    last_answered = None

    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        screen_region = capture_screen_region()
        answer = extract_and_solve_expression(screen_region)

        # note: it is possible that the next question has the same answer again, this means automatic answer will not trigger
        if answer is not None and answer != last_answered:
            print(f"[{current_time}] Pattern found! The answer is: {answer}")

            # simulate key presses and typing
            keyboard.press('y')
            keyboard.release('y')
            time.sleep(time_before_writing_answer)

            # type the answer and press enter
            keyboard.type(str(int(answer)))
            time.sleep(time_before_pressing_enter)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

            # update the last_answered
            last_answered = answer

        # sleep before checking again
        time.sleep(time_before_next_capture)


if __name__ == "__main__":
    main()

