# -*- coding: utf-8 -*-

import time
import pyautogui
import io

from PIL import Image

def StartGrub(x0 : int, y0 : int, x1 : int, y1 : int, savePath : str, key : str, keyDelay : int, pagesNum : int):
    '''
    x0 - x left up
    y0 - y left up
    x1 - x right down
    y1 - y right down
    savePath - path to save pdf
    key - emulating key to press
    keyDelay - delay before press key in ms
    pagesNum - number of pages / number of repeat
    '''

    pdfSavePath = fixPDF_savePath(savePath)

    keylist = key.strip().split()

    time.sleep(3)

    screens = []
    for circ in range(pagesNum):

        time.sleep(keyDelay/1000)

        dx = x1 - x0
        dy = y1 - y0
        screen = pyautogui.screenshot(region=(x0, y0, dx, dy))
        #screens.append( image2bytes(screen) )
        im = screen.convert("RGB")
        screens.append(im)

        if(circ != pagesNum-1):
            pressButtons(keylist)


    screens[0].save(pdfSavePath, save_all=True, append_images=screens[1:])


def image2bytes(image) -> bytes:
    img = image

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

def fixPDF_savePath(savePath : str) -> str:
    if(savePath[-4:].lower() == ".pdf"):
        return savePath
    else:
        return savePath + ".pdf"

def pressButtons(keylist : str):

    for key in keylist:
        if(key == "m_l"):
            pyautogui.click()
        elif(key == "m_r"):
            pyautogui.click(button='right')
        else:
            #pyautogui.press("down")
            #pyautogui.press("space")
            pyautogui.press(key)
        time.sleep(20 / 1000)

def saveFile(path : str, what : str):
    with open(path, 'w', encoding="utf-8") as temp:
        temp.write(what)