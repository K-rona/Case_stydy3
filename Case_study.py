'''
Аронова Александра - 58
Якимова Антонина -
'''

from turtle import *
from math import *

colours_choice = ['красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'пурпурный', 'розовый']
colours_draw = ['red', 'blue', 'green', 'yellow', 'orange', 'magenta', 'pink']

print("Допустимые цвета заливки: ")
for i in colours_choice:
    print(i)


def get_color_choice():
    color1 = False
    color2 = False

    while not color1:
        choice1 = input("Пожалуйста, введите первый цвет: ")

        if choice1 in colours_choice:
            index1 = colours_choice.index(choice1)
            color1 = colours_draw[index1]

        else:
            print(choice1, "не является верным значением.")

    while not color2:
        choice2 = input("Пожалуйста, введите второй цвет: ")

        if choice2 in colours_choice:
            index2 = colours_choice.index(choice2)
            color2 = colours_draw[index2]

        else:
            print(choice2, "не является верным значением.")

    return color1, color2


def get_num_hexagons():
    num_hexagons = False
    numbers = [i for i in range(4, 21)]

    while not num_hexagons:
        choice = int(input("Пожалуйста, введите количество шестиугольников, располагаемых в ряд: "))
        if choice in numbers:
            num_hexagons = choice
        else:
            print("Оно должно быть от 4 до 12\n"
                  "Пожалуйста, повторите попытку: ")

    return int(num_hexagons)


def draw_hexagon(x, y, side_len, color_fill, brdclr='black'):

    speed(0)
    posit = pos()
    color(brdclr, color_fill)
    seth(90)
    head = heading()

    goto(x, y)
    pd()
    begin_fill()

    for i in range(7):
        fd(side_len)
        lt(60)
    pu()
    end_fill()

    goto(posit)
    seth(head)


color1, color2 = get_color_choice()
N = get_num_hexagons()
side = 500/(N * sqrt(3))
step_horizontal = int(side * sqrt(3))
step_vertical = int(2 * side - side/2)
counting_hexagons = 0
counting_row = 0

for j in range(step_vertical*N-200, -200, -step_vertical):

    if counting_row % 2 == 0:
        for i in range(-100, step_horizontal*N-100, step_horizontal):

            if counting_hexagons % 2 == 0:
                draw_hexagon(i, j, side, color1)
            else:
                draw_hexagon(i, j, side, color2)

            counting_hexagons += 1

    else:
        for i in range(-int(side * sqrt(3))//2-100, step_horizontal*N-100, step_horizontal):

            if counting_hexagons % 2 == 0:
                draw_hexagon(i, j, side, color1)
            else:
                draw_hexagon(i, j, side, color2)

            counting_hexagons += 1

    counting_row += 1

done()
