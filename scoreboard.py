import turtle

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.display = turtle.Turtle()
        self.display.color("white")
        self.display.penup()
        self.display.hideturtle()
        self.display.goto(0, 260)
        self.update_display()

    def update_display(self):
        self.display.clear()
        self.display.write(
            f"Score: {self.score}  High Score: {self.high_score}", 
            align="center", 
            font=("Arial", 24, "normal")
        )

    def increase_score(self):
        self.score += 10
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_display()

    def reset(self):
        self.score = 0
        self.update_display()

    def game_over(self):
        self.display.goto(0, 0)
        self.display.write("Game Over", align="center", font=("Arial", 30, "normal"))
