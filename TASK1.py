# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота

# b) Подумайте как наделить бота 'интеллектом'

# cin - количество конфет - rand
import tkinter as tk
from random import randint
# программа

# def two_players_mode():
#     candies = int(randint(30, 101))
#     print(f"На столе лежит {candies} конфет! Возьмите от 1 до 28 конфет!")
#     player_switch = randint(0,2)
#     while candies != 0:
#         if player_switch:
#             candy_num = input(
#                 f"Ход первого игрока. Осталось {candies} конфет. Сколько конфет вы берете? ")
#             if int(candy_num) > 28 or int(candy_num) <= 0:
#                 print("Ошибка ввода. Пожалуйста, введите целое число от 1 до 28")
#             else:
#                 candies -= int(candy_num)
#                 player_switch = False
#         else:
#             candy_num = input(
#                 f"Ход второго игрока. Осталось {candies} конфет. Сколько конфет вы берете? ")
#             if int(candy_num) > 28 or int(candy_num) <= 0:
#                 print("Ошибка ввода. Пожалуйста, введите целое число от 1 до 28")
#             else:
#                 candies -= int(candy_num)
                
#             player_switch = True

#     if player_switch:
#         print("Игра закончилась, победил второй игрок!")
#     else:
#         print("Игра закончилась, победил первый игрок!")

# two_players_mode()



# def bot_mode():
#     candies = int(randint(30, 101))
#     print(f"На столе лежит {candies} конфет! Возьмите от 1 до 28 конфет!")
#     player_switch = True
#     while candies != 0:
#         if player_switch:
#             candy_num = input(
#                 f"Ход первого игрока. Осталось {candies} конфет. Сколько конфет вы берете? ")
#             if candy_num > 28 or candy_num <= 0:
#                 print("Ошибка ввода. Пожалуйста, введите целое число от 1 до 28")
#             else:
#                 candies -= int(candy_num)
#                 player_switch = False
#         else:
#             if candies <= 28:
#                 candy_bot_num = candies
#             else:
#                 next_bad_position = 29
#                 while next_bad_position < candies: 
#                     next_bad_position += 29
#                 candy_bot_num = candies - next_bad_position
#             candies -= int(candy_bot_num)
#             print(f"Умный бот забрал {candy_bot_num} конфет")
#             player_switch = True
#     if player_switch:
#         print("Игра закончилась, победил второй игрок!")
#     else:
#         print("Игра закончилась, победил первый игрок!")

# bot_mode()

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
# command = two_players_mode())
# btn1.pack()

# btn2 = tk.Button(win,
# text = "Игра против бота",
# bg = "pink",
# font = ('Arial', 15, 'bold'),
# relief = tk.RAISED,
# bd = 10)
# btn2.pack()

# win.mainloop()
