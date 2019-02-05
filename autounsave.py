import pyautogui, time
saved_find = 0
exit_find = 0
saved_location = 0
exit_location = 0
unsave_num = 0
first_run = True
picture_location = 0


def picture_click():
    global first_run,picture_location
    if first_run == True:
        picture_find = pyautogui.locateOnScreen("text.png")
        picture_location = pyautogui.center(picture_find)


def location_find():
    global  saved_find, exit_find, saved_location, exit_location,first_run,picture_location
    if first_run == True:
        saved_find = pyautogui.locateOnScreen("saved.png")
        exit_find = pyautogui.locateOnScreen("exit.png")
        first_run = False

    if first_run == False:
        saved_find = pyautogui.locateOnScreen("saved.png", region = (saved_find[0]-100,saved_find[1]-200, 500,500))
        exit_find = pyautogui.locateOnScreen("exit.png")
    saved_location = pyautogui.center(saved_find)
    exit_location = pyautogui.center(exit_find)



def unsave():
    pyautogui.click(saved_location[0],saved_location[1])
    pyautogui.click(exit_location[0], exit_location[1])
    pyautogui.hotkey("ctrl","r")
    time.sleep(2)


while unsave_num != 5:
    picture_click()
    pyautogui.click(picture_location[0], picture_location[1]+100)
    time.sleep(1)
    location_find()
    unsave()
    unsave_num = unsave_num + 1


