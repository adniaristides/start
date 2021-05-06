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
link = 'https://www.linkedin.com/in/adni-aristides/'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

time.sleep(2)

pyautogui.click(x=188, y=931,clicks=1)


pyautogui.alert ("Done")
