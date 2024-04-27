import pyautogui
import pytesseract
import requests
from PIL import Image
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gab\AppData\Local\Tesseract-OCR\tesseract.exe'

checked_list = []
non_exist = []
base_url = 'https://t.me/'

def find_text(text):
    apertura = '<strong>'
    chiusura = '</strong>'
    
    start_pos = text.find(apertura)
    end_pos = text.find(chiusura, start_pos)
    
    if start_pos != -1 and end_pos != -1:
        start_text_pos = start_pos + len(apertura)
        extracted_text = text[start_text_pos:end_pos]
        
        return extracted_text
    else:
        return None
    
class Checker:
    def check_username_web():
        try:
            us_req = requests.get("https://www.wandery.it/randomword-ita.php")
            extracted_text = find_text(us_req.text)
            if 99 < len(extracted_text):
                print(f"{extracted_text} < 6")
            else:
                username = f'{extracted_text}'
                url = f'{base_url}{username}'
                response = requests.get(url)

                if response.status_code == 200:
                    webpage_content = response.text
                    existence_text = f'tgme_action_button_new shine'
                    if existence_text in webpage_content:
                        checked_list.append(username)
                    else:
                        print(f'The username "@{username}" does not exist or could not be verified.')
                        pyautogui.typewrite(username)
                else:
                    print(f'Failed to access the webpage. HTTP status code: {response.status_code}')

                time.sleep(1)
                return username
        except Exception as e:
            print("Timeout, aspetto 25 secondi.")
            time.sleep(25)

    def check_username_app(username):
        screenshot = pyautogui.screenshot()
        screenshot_gray = screenshot.convert('L')
        extracted_text = pytesseract.image_to_string(screenshot_gray)
        search_text = "This link is available"

        if search_text in extracted_text:
            non_exist.append(username)
            print(non_exist)
        else:
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')

        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')


for i in range(500):
    try:
        us = Checker.check_username_web()
        Checker.check_username_app(us)
    except KeyboardInterrupt:
        print("Finito.")
        print(f"Tag disponibili: {non_exist}")
        quit()


print(non_exist)