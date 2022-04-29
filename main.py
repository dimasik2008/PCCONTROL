import pyautogui
import socket 
import colorama
from colorama import *
########
print(Fore.GREEN + Style.BRIGHT +'''
█▀█ █▀▀   █▀▀ █▀█ █▄░█ ▀█▀ █▀█ █▀█ █░░
█▀▀ █▄▄   █▄▄ █▄█ █░▀█ ░█░ █▀▄ █▄█ █▄▄
''')
print(Fore.GREEN + Style.BRIGHT +'''
█▄▄ █▄█   █░█ █▀▀ █▀█ █ █▀▀ █▀█ █▄░█ █▀ █▀█ █▀█
█▄█ ░█░   ▀▄▀ ██▄ █▀▄ █ █▄▄ █▄█ █░▀█ ▄█ █▄█ ▀▀█
''')
print(f"мой ip - {socket.gethostbyname(socket.gethostname())}")
print("скрипт запусчен!")
########
sock = socket.socket()
sock.bind(('', 7766))
sock.listen(0)
while True:
   conn, addr = sock.accept()
   print('connected:', addr)
   while True:
        data = conn.recv(1024).decode('utf-8').lower()#decode("ascii")
        if not data:
            break
        elif "vup" in data:
            pyautogui.press('volumeup') 
        elif "mute" in data:
            pyautogui.press('volumemute') 
        elif "vd" in data:
            pyautogui.press('volumedown') 
        ####
        elif "next" in data:
            pyautogui.press('nexttrack') 
        elif "pause" in data:
            pyautogui.press('playpause') 
        elif "prev" in data:
            pyautogui.press('prevtrack') 
        ####
        elif "enter" in data:
            pyautogui.press('return') 
        elif "del" in data:
            pyautogui.press('backspace') 
        elif "ctrlz" in data:
            pyautogui.hotkey('ctrl', 'z')
        elif "ctrly" in data:
            pyautogui.hotkey('ctrl', 'y')
        elif "copy" in data:
            pyautogui.hotkey('ctrl', 'c')
        elif "paste" in data:
            pyautogui.hotkey('ctrl', 'v')
        ####
        elif "lb" in data:
            pyautogui.click(button='left') 
        elif "rb" in data:
            pyautogui.click(button='right') 
        elif "mouse_up" in data:
            pyautogui.move(0, -10)
        elif "mouse_l" in data:
            pyautogui.move(-10, 0)
        elif "mouse_r" in data:
            pyautogui.move(10, 0)
        elif "mouse_down" in data:
            pyautogui.move(0, 10)
        ####



        
        


        else:
             pyautogui.write(data) 

        

        
