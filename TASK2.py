# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

import tkinter as tk

def game():
    symbol = ''

    num_1 = False
    num_2 = False
    num_3 = False
    num_4 = False
    num_5 = False
    num_6 = False
    num_7 = False
    num_8 = False
    num_9 = False





win = tk.Tk()
win.title("Крестики-нолики")
# win.geometry("500x500+100+100")
win.resizable(False, False)



btn1 = tk.Button(win, text = f'').grid(row = 0, column = 0, stick='wens')
btn2 = tk.Button(win, text = f'').grid(row = 0, column = 1, stick='wens')
btn3 = tk.Button(win, text = f'').grid(row = 0, column = 2, stick='wens')
btn4 = tk.Button(win, text = f'').grid(row = 1, column = 0, stick='wens')
btn5 = tk.Button(win, text = f'').grid(row = 1, column = 1, stick='wens')
btn6 = tk.Button(win, text = f'').grid(row = 1, column = 2, stick='wens')
btn7 = tk.Button(win, text = f'').grid(row = 2, column = 0, stick='wens')
btn8 = tk.Button(win, text = f'').grid(row = 2, column = 1, stick='wens')
btn9 = tk.Button(win, text = f'').grid(row = 2, column = 2, stick='wens')



win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=200)
win.grid_columnconfigure(2, minsize=200)
win.grid_rowconfigure(0, minsize=200)
win.grid_rowconfigure(1, minsize=200)
win.grid_rowconfigure(2, minsize=200)
win.mainloop()

# графическое оформление
# win = tk.Tk()
# photo = tk.PhotoImage(file = 'candy2.png')
# win.iconphoto(False, photo)
# win.config( bg = '#F5CAF2')
# win.title("Конфетки")
# win.geometry("500x500+100+100")
# win.resizable(False, False)

# btn1 = tk.Button(win,
# text = "Играем вдвоем",
# bg = "pink",
# font = ('Arial', 15, 'bold'),
# relief = tk.RAISED,
# bd = 10,
# command = two_players_mode
# )
# btn1.pack()

# btn2 = tk.Button(win,
# text = "Игра против бота",
# bg = "pink",
# font = ('Arial', 15, 'bold'),
# relief = tk.RAISED,
# bd = 10,
# command = bot_mode)
# btn2.pack()

# win.mainloop()
