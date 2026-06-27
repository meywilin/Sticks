import random
def human_turn(sticks_left):
    while True:
        try:
            take=int(input(f"Ваш ход. Осталось {sticks_left}. Сколько возьмете? (1-3)"))
            if 1<= take <= min(3, sticks_left):
                return take
            else:
                print("Ошибка можно взять от 1 до 3 спичек")
        except ValueError:
            print("Ошибка, введите целое число")

def computer_turn(sticks_left):
        if sticks_left >= 4 and sticks_left%4 != 0:
            computer_take = sticks_left%4
        else:
            computer_take = random.randint(1, min(3, sticks_left))
        print(f"Компьютер берет {computer_take} спичек")
        return computer_take
