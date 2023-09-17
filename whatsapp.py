import random 
import pyautogui as pg
import time 

words =('idiot', 'donkey ', 'dumb','fool', 'bozo')
time.sleep(8)

for i in range (25):
    a = random.choice(words)
    pg.write("You are "+ a)
    pg.press ('enter')
    
