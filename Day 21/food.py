from turtle import Turtle
import random


class Food(Turtle):   # Inheriting variables & methods from the class Turtle

    def __init__(self):
        super().__init__()
        self.color("lime green")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)