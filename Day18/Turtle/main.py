from turtle import Turtle, Screen
import random

tim = Turtle()
#tim.shape("turtle")
tim.color("pink")
#tim.pensize(15)
tim.speed("fastest")

# # Challenge 1: Draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# # Challenge 2: Draw a dashed line
# for i in range(20):
#     tim.forward(10)
#     if tim.isdown():
#         tim.penup()
#     else:
#         tim.pendown()

# # Challenge 3: Draw a triangle, square pentagon, hexagon, heptagon, octagon, nonagon and decagon
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(50)
#         tim.right(angle)
#
# for shape_side_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


import turtle
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)  # Create a tuple with the 3 colors
    return color

# # Challenge 4: Generate a random walk
# directions = [0, 90, 180, 270] # [North, East, South, West]
#
# for _ in range(100):
#     tim.forward(30)
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))


# Challenge 5: Create a flower of circles
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)








screen = Screen()
screen.exitonclick()