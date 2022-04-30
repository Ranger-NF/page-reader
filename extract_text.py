from pdf2image import convert_from_bytes

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

from colorama import Fore, Back, Style
from configparser import ConfigParser


config = ConfigParser()

config.read('config.ini')
pytesseract.pytesseract.tesseract_cmd = config.get('main', 'tesseract')

def extract_from_image(target_path):
    text = pytesseract.image_to_string(Image.open(target_path))

    return text

def extract_from_pdf(target_path):
    print(Fore.CYAN + "\nYou gave PDF format, This may take about 30 seconds to load, so please wait!\n")
    print(Style.RESET_ALL)
    images = convert_from_bytes(open(target_path, 'rb').read())
    text = ''


    for image in images:
        text += pytesseract.image_to_string(image)

    return text