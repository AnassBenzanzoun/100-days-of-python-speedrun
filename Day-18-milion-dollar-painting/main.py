from turtle import *
import random

speed("fastest")
colormode(255)


def square_dashes():
    for _ in range(4):
        for _ in range(5):
            forward(10)
            up()
            forward(10)
            down()
        right(90)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_gons_circle_angle():
    tim = Turtle()

    for i in range(3, 11):
        for _ in range(i):
            tim.color(random_color())
            tim.forward(100)
            tim.circle(100)
            tim.right(360 / i)


def random_walk():
    tom = Turtle()
    directions = [0, 90, 180, 270]
    for _ in range(5000):
        tom.color(random_color())
        tom.forward(30)
        tom.right(random.choice(directions))


def spilograph(size_of_gap):
    tam = Turtle()
    for i in range(int(360 / size_of_gap)):
        tam.color(random_color())
        tam.circle(100)
        tam.setheading(tam.heading() + size_of_gap)


# square_dashes()
# random_walk()
# draw_gons_circle_angle()
# spilograph(5)


def milion_dollar_painting():
    hirst = Turtle()
    hirst.speed("fastest")
    hirst.penup()
    hirst.hideturtle()
    color_list = [
        (245, 243, 238),
        (246, 242, 244),
        (240, 245, 241),
        (237, 241, 245),
        (244, 240, 245),
        (240, 245, 243),
        (244, 240, 240),
        (240, 244, 240),
        (243, 240, 244),
        (240, 240, 244),
        (244, 240, 243),
        (236, 244, 240),
        (240, 240, 240),
        (240, 236, 244),
        (240, 240, 236),
        (240, 236, 240),
        (236, 240, 240),
        (236, 240, 236),
        (240, 236, 236),
        (236, 236, 240),
    ]
    hirst.setheading(225)
    hirst.forward(300)
    hirst.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        hirst.dot(20, random.choice(color_list))
        hirst.forward(50)

        if dot_count % 10 == 0:
            hirst.setheading(90)
            hirst.forward(50)
            hirst.setheading(180)
            hirst.forward(500)
            hirst.setheading(0)


milion_dollar_painting()
screen = Screen()
screen.exitonclick()
