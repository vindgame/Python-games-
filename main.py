from turtle import Screen,Turtle
from paddle import Paddle
from ball import  Ball
from score import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PING PONG - GAME")
screen.tracer(0)



r_paddle = Paddle((380,0))
l_paddle = Paddle((-390,0))
ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    # detect r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()

