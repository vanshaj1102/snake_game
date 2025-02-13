import turtle
from typing import List, Tuple

class Snake:
    def __init__(self):
        self.segments: List[turtle.Turtle] = []
        self.direction = "stop"
        self.initial_positions = [(-20, 0), (0, 0), (20, 0)]
        self._create_snake()

    def _create_snake(self):
        for position in self.initial_positions:
            self._add_segment(position)

    def _add_segment(self, position: Tuple[int, int]):
        segment = turtle.Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self._add_segment(self.segments[-1].position())

    def move(self):
        if self.direction != "stop":
            for i in range(len(self.segments) - 1, 0, -1):
                x, y = self.segments[i - 1].pos()
                self.segments[i].goto(x, y)

            if self.direction == "up":
                self.segments[0].sety(self.segments[0].ycor() + 20)
            elif self.direction == "down":
                self.segments[0].sety(self.segments[0].ycor() - 20)
            elif self.direction == "left":
                self.segments[0].setx(self.segments[0].xcor() - 20)
            elif self.direction == "right":
                self.segments[0].setx(self.segments[0].xcor() + 20)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.direction = "stop"
        self._create_snake()

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"

    def go_left(self):
        if self.direction != "right":
            self.direction = "left"

    def go_right(self):
        if self.direction != "left":
            self.direction = "right"
