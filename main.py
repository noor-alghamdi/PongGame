import turtle;

window = turtle.Screen();
window.title("Pong By @namacoconut")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle A ..
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
# to the left
paddle_a.goto(-350,0) 


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
# to the right
paddle_b.goto(350,0)

# moving the paddle a up
def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  y = paddle_a.sety(y)

# moving the paddle a down
def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  y = paddle_a.sety(y)

# moving the paddle b up
def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  y = paddle_b.sety(y)

# moving the paddle b down
def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  y = paddle_b.sety(y)  

# calling the move functions:
window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s") 
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
# to the right
ball.goto(0,0)
ball.movx = 0.1
ball.movy = 0.1


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.hideturtle()
pen.penup()
pen.goto(0, 260)
pen.write("Player A: 0     Player B: 0", align="center", font=("courier", 24, "normal"))

# Score
score_a = 0
score_b = 0

# Main game loop:
while True:
  window.update()

  # moving the ball:
  ball.setx(ball.xcor() + ball.movx)
  ball.sety(ball.ycor() + ball.movy)


  # border cheking:
  if ball.ycor() > 290:
    ball.sety(290)
    ball.movy *= -1

  if ball.ycor() < -290:
    ball.sety(-290)
    ball.movy *= -1

  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.movx *= -1

  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.movx *= -1

  
  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
    ball.setx(340)
    ball.movx *= -1
    score_a += 1
    pen.clear()
    pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
    ball.setx(-340)
    ball.movx *= -1
    score_b += 1
    pen.clear()
    pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))
    






