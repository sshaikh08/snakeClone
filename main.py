# FUTURE FEATURE
# valid_difficulties = {'easy', 'medium', 'hard'}
# if difficulty.lower() not in valid_difficulties:
#    raise ValueError("results: status must be one of %r." % valid_difficulties)

import game_window as g_w


def run_snake_game():
    g_w.window.mainloop()


if __name__ == '__main__':
    run_snake_game()
