from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red" , "orange","yellow", "green", "blue" , "purple"]
turtles = []
x = -230
y = 100

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    y -= 30
    t.goto(x, y)
    turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



screen.exitonclick()