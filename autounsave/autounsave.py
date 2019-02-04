import pyautogui, time
saved_find = 0
exit_find = 0
saved_location = 0
exit_location = 0
unsave_num = 0


def location_find():
    global  saved_find, exit_find, saved_location, exit_location
    saved_find = pyautogui.locateOnScreen("saved.png")
    exit_find = pyautogui.locateOnScreen("exit.png")
    saved_location = pyautogui.center(saved_find)
    exit_location = pyautogui.center(exit_find)


def unsave():
    pyautogui.click(saved_location[0],saved_location[1])
    pyautogui.click(exit_location[0], exit_location[1])
    pyautogui.hotkey("ctrl","r")
    time.sleep(2)


while unsave_num != 2:
    pyautogui.click(1382,1367)
    time.sleep(2)
    location_find()
    unsave()
    unsave_num = unsave_num + 1


