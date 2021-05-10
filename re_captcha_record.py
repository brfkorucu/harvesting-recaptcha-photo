import pyautogui
import os
import time

for i in range(2000):
    print("JPG " + str(i) + "downloading")
    os.system("start chrome --url https://patrickhlauke.github.io/recaptcha/")
    time.sleep(4)

    pyautogui.moveTo(39,220, duration=0.3)
    pyautogui.click()
    time.sleep(2.5)

    screenshot = pyautogui.screenshot()
    os.chdir(r"C:\Users\HOPE\Desktop\WorkSpace\Deep-Learning\Head_DataSets")
    screenshot.save("pic{}.jpg".format(str(i)))

    pyautogui.moveTo(189,371, duration=0.3)
    pyautogui.rightClick()
    pyautogui.press("down")
    time.sleep(0.3)
    pyautogui.press("down")
    time.sleep(0.3)
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.moveTo(512,443, duration=0.3)
    pyautogui.click()


    pyautogui.moveTo(1417,14, duration=0.3)
    pyautogui.click()
    time.sleep(1)