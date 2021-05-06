import pyautogui
import pyperclip
import time

pyautogui.alert("Let's Begin")

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(2)

pyautogui.click(x=439, y=72)
link = 'https://www.myinstants.com/instant/ps1/'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

time.sleep(2)

pyautogui.click(x=982, y=884,clicks=1)


pyautogui.alert ("Done")
