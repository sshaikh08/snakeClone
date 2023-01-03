import tkinter as tk
# from . import player_hud_constants as p_d
from . import canvas_constants as cnvs

# FUTURE FEATURE: More than one dificulty size. Smaller is harder. Then data persistence
WINDOW_SIZE = '1000x1000'

score = 0
high_score = 0

window = tk.Tk()
window.geometry(WINDOW_SIZE)
window.title('Shariq\'s Snake Game')

# window.resizable(False, False) # Main # Change this at some point
# window.resizable(True, True)  # TEST

score_label = tk.Label(window, text=f'SCORE: {score}\n')
                                    #f'HIGH SCORE: {high_score}')
high_score_label = tk.Label(window, text=f'HIGH SCORE: {high_score}')

#score_label.grid(row=0, column=0, columnspan=2, pady=0, sticky='W')
#high_score_label.grid(row=1, column=0, columnspan=2, pady=0, sticky='W')

score_label.place(anchor='nw')
high_score_label.place(anchor='nw', y=20)

canvas = tk.Canvas(window,
                   bg=cnvs.BACKGROUND_COLOR,
                   height=cnvs.GAME_HEIGHT,
                   relief=cnvs.GAME_RELIEF,
                   width=cnvs.GAME_WIDTH)

canvas.place(anchor='e')
#
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
