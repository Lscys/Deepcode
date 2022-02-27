import pyautogui as pg
import time

pg.hotkey("win","r")
pg.typewrite("https://www.youtube.com/watch?v=MYQ79nDYO5Q&ab_channel=FrankyStyleVEVO\n")
time.sleep(2)
pg.typewrite("k")
pg.hotkey("win","r")
pg.typewrite("notepad\n")
time.sleep(1)
pg.typewrite("Este es mi primer progama\n")
time.sleep(3)
pg.typewrite("realizado con pyautogui\n")
time.sleep(2)
pg.typewrite("e automatizacion con python\n")