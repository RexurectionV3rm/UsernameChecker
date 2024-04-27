# Username Checker

Username Checker is a program finalized to check availability of Telegram Usernames, trying to avoid any rate limitation or such.
**ONLY ITALIAN!**

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages.

```bash
pip install pyautogui, pytesseract, requests, pillow
```
You must also download the Windows/Linux Debian version of Tesseract to make it function properly.
You can find Tesseract github's [here](https://github.com/tesseract-ocr/tesseract)

You must also change the directory path in the python code:
```python
pytesseract.pytesseract.tesseract_cmd = r'PATH_HERE'
```

## Usage

1. Open **Telegram**
2. Create a channel, and make it public
3. Change the channel's username
4. Start **start.py** with the following command:
  ```bash
  python start.py
  ```
6. Change the window to **Telegram** and let it work.
7. When a username is found, it will add it to a list and when it finishes it prints a list in the console.
8. Done!

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
