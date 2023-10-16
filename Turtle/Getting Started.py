import sys
import turtle as t
import random


# draw a circle
tim = t.Turtle()
tim.width(5)
tim.speed(5000000)
tim.circle(radius=50)
while True:
    tim.color("#{:06x}".format(random.randrange(256 ** 3)))
    tim.circle(radius=200)
    tim.left(20)

sys.exit()

tim = t.Turtle()
tim.width(10)
tim.speed(5000000)
limit = 400
while True:
    color = "#{:06x}".format(random.randrange(256 ** 3))
    dir = random.choice([z for z in range(361) if z % 90 == 0])

    tim.left(dir)
    if not (-0 <= tim.position()[0] < limit and -0 <= tim.position()[1] < limit):
        tim.penup()
        tim.goto(tim.position()[0] % limit, tim.position()[1] % limit)
        tim.pendown()
        if random.randint(0,600) % 3 == 0:
            tim.color(color)
    else:
        tim.forward(40)

# Draw a dashed line
tim = t.Turtle()
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

for side in range(3, 15):
    for _ in range(side):
        angle = 360 - (360 // side)
        tim.forward(100)
        tim.right(angle)
