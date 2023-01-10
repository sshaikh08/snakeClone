#This file is code directly taken from the youtube bro code. It's for me to experiment with and compare to my version of game_window which will be the final implementation

from tkinter import *


BACKGROUND_COLOR = '#000000'
GAME_HEIGHT = 700
GAME_WIDTH = 700

window = Tk() #This inst
window.title("Snake game")
window.resizable(False,False)




score = 0

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

print(f"{window_width}x{window_height}+{x}+{y}")
print("x = "+str(x))
print("y = "+str(y))
print("window.winfo_width() = " + str(window.winfo_width()))
print("window.winfo_height() = " + str(window.winfo_height()))