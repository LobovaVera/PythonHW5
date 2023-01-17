# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота 'интеллектом'

# cin - количество конфет - rand
import tkinter as tk
from random import randint
from tkinter import *
from tkinter import ttk
# программа

# def get_data():
#     global data
#     data = val.get()   
    
win = tk.Tk()
photo = tk.PhotoImage(file = 'candy2.png')
win.iconphoto(False, photo)
win.config( bg = '#F5CAF2')
win.title("Конфетки")
win.geometry("500x500+100+100")
win.resizable(False, False)

btn1 = tk.Button(win,
text = "Играем вдвоем",
bg = "pink",
font = ('Arial', 15, 'bold'),
relief = tk.RAISED,
bd = 10
# command = two_players_mode
)
btn1.pack()  


    
candies = int(randint(30, 101))
btn1['text'] = f"На столе лежит {candies} конфет! Возьмите от 1 до 28 конфет!"
player_switch = randint(0,2)
    
while candies != 0:
    if player_switch:
        tk.Label(win, text = f"Ход первого игрока. Осталось {candies} конфет. Сколько конфет вы берете?").pack()
        val = tk.Entry(win)
        val.pack() 
        global candy_num
        getBtn = ttk.Button(win, text = 'Беру', command = lambda: val.get())
        getBtn.pack()
            
        candy_num=4
        if candy_num > 28 or candy_num <= 0:
            btn1['text'] = "Ошибка ввода. Пожалуйста, введите целое число от 1 до 28"
        else:
            candies -= candy_num
            player_switch = False
    else:
        tk.Label(f"Ход второго игрока. Осталось {candies} конфет. Сколько конфет вы берете? ").pack()
           
        val = tk.Entry(win)
        val.pack()
            
        getBtn = tk.Button(win, text = 'Беру', command = get_data(val))
        getBtn.pack()

        data = val.get()
        candy_num=int(data)

        if candy_num > 28 or candy_num <= 0:
            btn1['text'] = "Ошибка ввода. Пожалуйста, введите целое число от 1 до 28"
        else:
            candies -= candy_num
                
        player_switch = True

if player_switch:
    btn1['text'] = "Игра закончилась, победил второй игрок!"
else:
    btn1['text'] = "Игра закончилась, победил первый игрок!"



# def bot_mode():
#     candies = int(randint(30, 101))
#     candy_bot_num = 0
#     print(f"На столе лежит {candies} конфет! Возьмите от 1 до 28 конфет!")
#     player_switch = randint(0,2)
#     while candies != 0:
#         if player_switch:
#             candy_num = int(input(
#                 f"Ход игрока. Осталось {candies} конфет. Сколько конфет вы берете? "))
#             if candy_num > 28 or candy_num <= 0:
#                 print("Ошибка ввода. Пожалуйста, введите целое число от 1 до 28")
#             else:
#                 candies -= candy_num
#                 player_switch = False
#         else:
#             print(f"На столе лежит {candies} конфет! Ходит Умный Бот")
#             if candies <= 28:
#                 candy_bot_num = candies
#             elif candies%29 == 0:
#                 print("Умный Бот признает превосходство человеческого интеллекта. Вы победили!")
#                 break

#             else:
#                 candy_bot_num = candies%29
#             candies -= candy_bot_num
#             print(f"Умный Бот забрал {candy_bot_num} конфет")
#             player_switch = True
#     if player_switch:
#         print("Игра закончилась, победил Умный Бот!")
#     else:
#         print("Игра закончилась, Вы победили!")

# bot_mode()



# графическое оформление


# btn2 = tk.Button(win,
# text = "Игра против бота",
# bg = "pink",
# font = ('Arial', 15, 'bold'),
# relief = tk.RAISED,
# bd = 10,
# command = bot_mode)
# btn2.pack()

win.mainloop()
