import numpy as np
import cv2
from PIL import Image
import pytesseract as pytess
def ratioCheck(Ar, breatth, height):
    ratio = float(breatth) / float(height)
    if ratio < 1:
       ratio = 1 / ratio
    if(Ar  73862.5) or (ratio  6):
        return False
    return True