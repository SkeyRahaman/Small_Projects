# import colorgram
#
# rgb_colors = [(clr.rgb.r, clr.rgb.g, clr.rgb.b) for clr in colorgram.extract('color_palet.webp', 30)][5:]
#
# print(rgb_colors)
#
import random
import turtle
turtle.colormode(255)
tim = turtle.Turtle()
tim.speed(1000)

colors = [(54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]
dis =50
move = 100
for row in range(10):
    for col in range(10):
        tim.penup()
        tim.goto((dis*row)-move,(dis*col)-move)
        tim.pendown()
        tim.dot(20,random.choice(colors))


        pass

_ = input()
