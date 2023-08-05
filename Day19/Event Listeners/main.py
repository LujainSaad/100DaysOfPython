from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()


# Activates event listeners
screen.listen()
screen.onkey(key="w", fun=move_forwards)  # Without () ❌
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
screen.onkey(clear, "c")
screen.exitonclick()
