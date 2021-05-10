import pyautogui
import os
import time
from PIL import Image, ImageOps
import pytesseract
import optparse

def crop_pic(screenshot_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    print(screenshot_path)
    image_file = Image.open(r"{}".format(screenshot_path))
    image_file = image_file.convert("L")
    img1 = ImageOps.colorize(image_file, black = "white", white = "black")
    cropped = img1.crop((110,120,450,225))
    raw_text = pytesseract.image_to_string(cropped)
    a = raw_text.split("\n")
    fileName = a[0]
    fileName = fileName.replace(" ", "_")
    print(fileName)
    return fileName

def open_folder(fileName):
    d_path = r"C:\Users\HOPE\Desktop\WorkSpace\Deep-Learning\DataSets\{}".format(fileName)
    if os.path.isfile(d_path) == True:
        return d_path
    if os.path.isfile(d_path) == False:
        os.system("mkdir C:\\Users\\HOPE\\Desktop\\WorkSpace\\Deep-Learning\\DataSets\\{}".format(fileName))
        return d_path

def main():
    parser = optparse.OptionParser("usage%prog " + "-n <number-of-harvest> " + "-j <name of jpg's>")
    parser.add_option("-n", dest="repeat", type="int", help="specify number of harvest jpg")
    parser.add_option("-j", dest="nameJPG", type="string", help="specift jpg's name")
    (options, args) = parser.parse_args()
    repeat = options.repeat
    nameJPG = options.nameJPG
    if repeat == None or nameJPG == None:
        print(parser.usage)
        exit(0)

    for i in range(repeat):
        print("JPG " + str(i) + " downloading")
        os.system("start opera --private")
        time.sleep(1.5)
        pyautogui.moveTo(204,134, duration=0.1)
        pyautogui.click()

        pyautogui.moveTo(315,62, duration=0.1)
        pyautogui.click()
        pyautogui.typewrite("https://patrickhlauke.github.io/recaptcha/",interval=0.03)
        pyautogui.press("enter")

        while True:
            if pyautogui.locateOnScreen(r"C:\Users\HOPE\Desktop\WorkSpace\Deep-Learning\mouse project\button.png"):
                break

        pyautogui.moveTo(81,258, duration=0.3)
        pyautogui.click()
        time.sleep(1.5)

        reload_key = pyautogui.locateOnScreen(r"C:\Users\HOPE\Desktop\WorkSpace\Deep-Learning\mouse project\reaload.png")

        if reload_key != None:

            pyautogui.moveTo(209,50, duration=0.1)
            pyautogui.click()

            pyautogui.moveTo(204,134, duration=0.1)
            pyautogui.click()

            pyautogui.moveTo(315,62, duration=0.1)
            pyautogui.click()
            pyautogui.typewrite("https://patrickhlauke.github.io/recaptcha/",interval=0.03)
            pyautogui.press("enter")

            while True:
                if pyautogui.locateOnScreen(r"C:\Users\HOPE\Desktop\WorkSpace\Deep-Learning\mouse project\button.png"):
                    break

            pyautogui.moveTo(81,258, duration=0.3)
            pyautogui.click()
            time.sleep(2)

            screenshot = pyautogui.screenshot()
            screenshot.save(r"C:\Users\HOPE\Desktop\WorkSpace\Deep-Learning\mouse project\screenshot.jpg")
            screenshot_path = r"C:\Users\HOPE\Desktop\WorkSpace\Deep-Learning\mouse project\screenshot.jpg"

            fileName = crop_pic(screenshot_path)
            d_path = open_folder(fileName)

            pyautogui.moveTo(189,371, duration=0.3)
            pyautogui.rightClick()
            pyautogui.press("down")
            time.sleep(0.1)
            pyautogui.press("down")
            time.sleep(0.1)
            pyautogui.press("enter")
            time.sleep(1)

            pyautogui.moveTo(360,46, duration=0.3)
            pyautogui.click()
            pyautogui.typewrite(d_path, interval=0.015)
            pyautogui.press("enter")

            pyautogui.moveTo(282,377, duration=0.3)
            pyautogui.click()
            pyautogui.typewrite(nameJPG + str(i) + ".jpg")
            
            pyautogui.moveTo(513,446, duration=0.3)
            pyautogui.click()

            pyautogui.moveTo(1417,14, duration=0.3)
            pyautogui.click()
            time.sleep(1)

            continue

        screenshot = pyautogui.screenshot()
        screenshot.save(r"C:\Users\HOPE\Desktop\WorkSpace\Deep-Learning\mouse project\screenshot.jpg")
        screenshot_path = r"C:\Users\HOPE\Desktop\WorkSpace\Deep-Learning\mouse project\screenshot.jpg"
        
        fileName = crop_pic(screenshot_path)
        d_path = open_folder(fileName)

        pyautogui.moveTo(189,371, duration=0.3)
        pyautogui.rightClick()
        pyautogui.press("down")
        time.sleep(0.1)
        pyautogui.press("down")
        time.sleep(0.1)
        pyautogui.press("enter")
        time.sleep(1)

        pyautogui.moveTo(360,46, duration=0.3)
        pyautogui.click()
        pyautogui.typewrite(d_path, interval=0.015)
        pyautogui.press("enter")

        pyautogui.moveTo(282,377, duration=0.3)
        pyautogui.click()
        pyautogui.typewrite(nameJPG + str(i) + ".jpg")
            
        pyautogui.moveTo(513,446, duration=0.3)
        pyautogui.click()

        pyautogui.moveTo(1417,14, duration=0.3)
        pyautogui.click()
        time.sleep(1)

if __name__ == "__main__":
    main()