import random 
import pyautogui as pg
import time 

words =('world ', 'one and only ', 'angel','Princess', 'good girl')
time.sleep(8)

for i in range (15):
    a = random.choice(words)
    pg.write("i love you baby you are my  "+ a)
    pg.press ('enter')
    