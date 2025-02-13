import turtle
import time
try:
    import winsound
except ImportError:
    winsound = None

from snake import Snake
from food import Food
from scoreboard import Scoreboard

def setup_screen():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen

def create_border():
    border = turtle.Turtle()
    border.color("white")
    border.penup()
    border.goto(-290, 290)
    border.pendown()
    border.pensize(3)
    for _ in range(4):
        border.forward(580)
        border.right(90)
    border.hideturtle()

def play_sound():
    if winsound:
        winsound.Beep(1000, 100)

def main():
    screen = setup_screen()
    create_border()

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_right, "Right")

    def game_loop():
        screen.update()
        snake.move()

        # Detect collision with food
        if snake.segments[0].distance(food.get_position()) < 20:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
            play_sound()

        # Detect collision with wall
        head = snake.segments[0]
        if (head.xcor() > 290 or head.xcor() < -290 or 
            head.ycor() > 290 or head.ycor() < -290):
            scoreboard.game_over()
            screen.update()
            time.sleep(2)
            snake.reset()
            scoreboard.reset()
            return

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if head.distance(segment) < 20:
                scoreboard.game_over()
                screen.update()
                time.sleep(2)
                snake.reset()
                scoreboard.reset()
                return

        screen.ontimer(game_loop, 100)

    game_loop()
    screen.mainloop()

if __name__ == "__main__":
    main()
