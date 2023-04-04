import turtle
# import winsound                     #Import sound function

wn = turtle.Screen()
wn.title("Pong Game by @shreya-gb")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)                    #Shape of the paddle
paddle_a.penup()                                                    #No line should be seen
paddle_a.goto(-350, 0)                                              #Start the paddle from


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)                    #Shape of the paddle
paddle_b.penup()                                                    #No line should be seen
paddle_b.goto(350, 0)                                               #Start the paddle from


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()                                                    #No line should be seen
ball.goto(0, 0)
ball.dx = 0.2                                                   #Speed of ball wrt to center coordinates
ball.dy = -0.2

#Pen = Turtle Module
pen = turtle.Turtle()
pen.speed(0)                                                   #Animation Speed not movement speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)                                               #This is the placement of the Scocre board
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "bold"))

#Function for the paddles
def paddle_a_up():
    y = paddle_a.ycor()                                         #Paddle goes up
    y += 20                                                     # Movies 20 Steps upwards along y coordinate
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()                                         #Paddle goes up
    y -= 20                                                     # Movies 20 Steps upwards along y coordinate
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()                                         #Paddle goes up
    y += 20                                                     # Movies 20 Steps upwards along y coordinate
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()                                         #Paddle goes up
    y -= 20                                                     # Movies 20 Steps upwards along y coordinate
    paddle_b.sety(y)



#Keyboard Binding (Triggering the funtion)
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")                                 #Up - Camelcase states it is " Keyboard Arrow Keys"
wn.onkeypress(paddle_b_down, "Down")

#Main Game Loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checker for the game
    #Top Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1                                            # [*] The ball reflects back from the border, [=] Makes the ball to continue in the reflected path

    # winsound.Playsound("bounce.mp3", winsound.SND_ASYNC)                   # ASYNC - will not terminate the code after the ball collided with the borders

    #Bottom Border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Left Border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a, score_b) , align="center", font=("Courier", 24, "bold"))

    #Right Border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a , score_b) , align="center", font=("Courier", 24, "bold"))


    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1