import pyautogui

print("For stop press CTRL-C")
while True :
    x,y = pyautogui.position()
    pixelColour = pyautogui.screenshot().getpixel((x,y))
    print("x : " + str(x) + " y : " + str(y) + "   " + str(pixelColour), end="\r")