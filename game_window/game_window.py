import tkinter as tk

from . import canvas_constants as cnvs

#import canvas_constants as cnvs

# from . import player_hud_constants as p_d

# FUTURE FEATURE: More than one dificulty size. Smaller is harder. Then data persistence
WINDOW_WIDTH = '550'
WINDOW_HEIGHT = '750'
WINDOW_SIZE = f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}'
WINDOW_COLOR = 'grey'

score = 0
high_score = 0

window = tk.Tk()
window.title('Shariq\'s Snake Game')
window.configure(bg=WINDOW_COLOR)
#window.geometry(WINDOW_SIZE) #First attempt to set the geometry



window.resizable(False, False) # Main # Change this at some point
# window.resizable(True, True)  # TEST

score_label = tk.Label(window, text=f'SCORE: {score}\n')
                                    #f'HIGH SCORE: {high_score}')
score_label.config(bg=WINDOW_COLOR)
high_score_label = tk.Label(window, text=f'HIGH SCORE: {high_score}')
high_score_label.config(bg=WINDOW_COLOR)



score_label.place(anchor='nw', y=30)
high_score_label.place(anchor='nw', y=50)

canvas = tk.Canvas(window,
                   bg=cnvs.BACKGROUND_COLOR,
                   height=cnvs.GAME_HEIGHT,
                   relief=cnvs.GAME_RELIEF,
                   width=cnvs.GAME_WIDTH)



canvas.place(x=525, y=375, anchor='e')

window.update()


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (int(WINDOW_WIDTH)/2))
y = int((screen_height/2) - (int(WINDOW_HEIGHT)/2))

window.geometry(f"{WINDOW_SIZE}+{x}+{y}")
# print('window_width: ' + str(window.winfo_width()))
# print('window_height: ' + str(window.winfo_height()))
# print('screen_width: ' + str(window.winfo_screenwidth()))
# print('screen_height: ' + str(window.winfo_screenheight()))
# print('x: ' + str((screen_width/2) - (window_width/2)))
# print('y: ' + str((screen_height/2) - (window_height/2)))
#
# print('Combining the above gets you the following result: ')
# print(f'{window_width}x{window_height}+{x}+{y}')

#################################################################
# print('Look what\'s here')
print(WINDOW_SIZE)
print(type(window.winfo_width()))
print("x = "+str(x))
print("y = "+str(y))
print("window.winfo_width() = " + str(window.winfo_width()))
print("window.winfo_height() = " +str(window.winfo_height()))
print("window.winfo_rewidth() = " +str(window.winfo_reqwidth()))



#score_label.grid(row=0, column=0, columnspan=2, pady=0, sticky='W')
#high_score_label.grid(row=1, column=0, columnspan=2, pady=0, sticky='W')

# canvas.grid(row=0, column=5, padx=50, pady=2, sticky='E')
#
# window.columnconfigure(3, weight=1)

# label = tk.Label(window, text=f'SCORE: {p_d.score}\n'
#                               f'HIGH SCORE: {p_d.high_score}',
#                          font=('PT Sans', 25))
# label.pack()
# label.place(x=5, y=20, anchor='w')


# label.grid(row=0, column=0)


# print(p_d.score) # test

# window.mainloop() # test
