import pyautogui as at
x, y = at.size()
at.moveTo(x / 2, y / 2)
print at.position()
