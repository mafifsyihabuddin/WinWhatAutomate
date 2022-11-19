import pyautogui
import pyperclip
from time import sleep

def getImagePosition(image_location, detection_confidance = .9):
    image = pyautogui.locateOnScreen(image_location, confidence = detection_confidance)
    x_position = image[0] + image[2]/2
    y_position = image[1] + image[3]/2
    return (x_position, y_position)

def clickImage(image_location, detection_confidance = .9):
    imagePosition = getImagePosition(image_location, detection_confidance)
    pyautogui.moveTo(imagePosition)
    pyautogui.click()

def moveToImage(image_location, detection_confidance = .9, offsetX = 0, offsetY = 0):
    imagePosition = getImagePosition(image_location, detection_confidance)
    pyautogui.moveTo(imagePosition[0] + offsetX, imagePosition[1] + offsetY)

clickImage("images\whatsapp_notification.png", .92)

while True:
    try:
        clickImage("images\green_dot_notification.png")
    except:
        print("can't find")
        pyautogui.hotkey("win", "m")

    sleep(1)
    moveToImage("images\smiley_n_paperclip.png", .8, -20, -65)
    pyautogui.rightClick(interval=.05)
    sleep(1)
    moveToImage("images\copy.png")
    pyautogui.doubleClick()
    recievedMessage = pyperclip.paste().lower()

    pyautogui.hotkey("alt", "space")
    pyautogui.write(recievedMessage)
    sleep(2)
    pyautogui.keyDown("enter")
    sleep(2)
    pyautogui.hotkey("fn", "printscreen")
    sleep(1)
    clickImage("images\whatsapp.png")
    moveToImage("images\smiley_n_paperclip.png", .9, 200, 0)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "v")
    sleep(2)
    pyautogui.press("enter")
    sleep(5)