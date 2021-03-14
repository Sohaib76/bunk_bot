# -*- coding: utf-8 -*-


import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string(Image.open("C:\\Users\\Sx\\Documents\\DARDM\\Sample Video-Pics\\ocr.png"))
print(text)


