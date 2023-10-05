import pyautogui, time
time.sleep(5)  # tempo para começar a enviar

ler = open('msg_spam', 'r')
for word in ler:
    pyautogui.typewrite(word*500)  # quantidade de x que serão enviadas
    pyautogui.press('enter')
    