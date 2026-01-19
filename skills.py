import os
import webbrowser
import datetime
import pyautogui

def open_notepad():
    os.system("notepad")
    return "Opened Notepad."

def open_chrome():
    # Adjust path if necessary for your OS
    webbrowser.open("https://www.google.com")
    return "Opened Google Chrome."

def get_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    return f"The current time is {now}."

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    return "Screenshot saved as screenshot.png."

# The Dictionary Mapping (Crucial for the Brain to find the tools)
AVAILABLE_TOOLS = {
    "open_notepad": open_notepad,
    "open_chrome": open_chrome,
    "get_time": get_time,
    "take_screenshot": take_screenshot
}