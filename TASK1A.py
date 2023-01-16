import tkinter as tk
from random import randint


def two_players_mode():
    candies = int(randint(30, 101))
    print(f"На столе лежит {candies} конфет! Возьмите от 1 до 28 конфет!")
    player_switch = randint(0, 2)
    while candies != 0:
        if player_switch:
            candy_num = int(input(
                f"Ход первого игрока. Осталось {candies} конфет. Сколько конфет вы берете? "))
            if candy_num > 28 or candy_num <= 0 or candies < candy_num:
                print("Ошибка ввода. Пожалуйста, введите целое число от 1 до 28")
            else:
                candies -= candy_num
                player_switch = False
        else:
            candy_num = int(input(
                f"Ход второго игрока. Осталось {candies} конфет. Сколько конфет вы берете? "))
            if candy_num > 28 or candy_num <= 0:
                print("Ошибка ввода. Пожалуйста, введите целое число от 1 до 28")
            else:
                candies -= candy_num

            player_switch = True

    if player_switch:
        print("Игра закончилась, победил второй игрок!")
    else:
        print("Игра закончилась, победил первый игрок!")


two_players_mode()
