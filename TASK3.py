def bot_mode():
    candies = int(randint(30, 101))
    print(f"На столе лежит {candies} конфет! Возьмите от 1 до 23 конфет!")
    player_switch = True
    while candies != 0:
        if player_switch:
            candy_num = input(
                f"Ход первого игрока. Осталось {candies} конфет. Сколько конфет вы берете? ")
            if candy_num > 28 or candy_num <= 0:
                print("Ошибка ввода. Пожалуйста, введите целое число от 1 до 28")
            else:
                candies -= int(candy_num)
                player_switch = False
        else:
            if candies <= 28:
                candy_bot_num = candies
            else:
                next_bad_position = 29
                while next_bad_position < candies: 
                    next_bad_position += 29
                candy_bot_num = candies - next_bad_position
            candies -= int(candy_bot_num)
            print(f"Умный бот забрал {candy_bot_num} конфет")
            player_switch = True
    if player_switch:
        print("Игра закончилась, победил второй игрок!")
    else:
        print("Игра закончилась, победил первый игрок!")

bot_mode()