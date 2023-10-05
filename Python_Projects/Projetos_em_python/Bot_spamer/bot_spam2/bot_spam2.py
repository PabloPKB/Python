import time
import pyautogui

for i in range(0, 10):
    pyautogui.click(519, 797)
    pyautogui.typewrite('Mensagem enviada')
    pyautogui.press('enter')
    time.sleep(4)
