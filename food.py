import turtle
import random

class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.refresh()

    def refresh(self):
        self.food.goto(random.randint(-280, 280), random.randint(-280, 280))

    def get_position(self):
        return self.food.position()
