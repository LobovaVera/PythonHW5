
import tkinter as tk
from random import randint

def bot_mode():
    candies = int(randint(30, 101))
    candy_bot_num = 0
    print(f"На столе лежит {candies} конфет! Возьмите от 1 до 28 конфет!")
    player_switch = randint(0,2)
    while candies != 0:
        if player_switch:
            candy_num = int(input(
                f"Ход игрока. Осталось {candies} конфет. Сколько конфет вы берете? "))
            if candy_num > 28 or candy_num <= 0:
                print("Ошибка ввода. Пожалуйста, введите целое число от 1 до 28")
            else:
                candies -= candy_num
                player_switch = False
        else:
            print(f"На столе лежит {candies} конфет! Ходит Умный Бот")
            if candies <= 28:
                candy_bot_num = candies
            elif candies%29 == 0:
                print("Умный Бот признает превосходство человеческого интеллекта. Вы победили!")
                break

            else:
                candy_bot_num = candies%29
            candies -= candy_bot_num
            print(f"Умный Бот забрал {candy_bot_num} конфет")
            player_switch = True
    if player_switch:
        print("Игра закончилась, победил Умный Бот!")
    else:
        print("Игра закончилась, Вы победили!")

bot_mode()