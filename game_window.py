import tkinter as tk
import player_display as p_d

# FUTURE FEATURE: More than one dificulty size. Smaller is harder. Then data persistence


window = tk.Tk()
window.title('Shariq\'s Snake Game')
window.resizable(False, False) # Change this at some point

label = tk.Label(window, text=f'SCORE{p_d.score}', font=('PT Sans', 40))
