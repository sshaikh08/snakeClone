# FUTURE FEATURE
# valid_difficulties = {'easy', 'medium', 'hard'}
# idifficulty.lower() not in valid_difficulties:
#    raise ValueError("results: status must be one of %r." % valid_difficulties)

from gamewindow import game_window as g_w


def play_snake_game():
    g_w.window.mainloop()



if __name__ == '__main__':
    play_snake_game()
