# Tutorial: https://pygame-zero.readthedocs.io/en/stable/introduction.html
import pgzrun
WIDTH = 500
HEIGHT = 400
yellow = (245,245,66)
ball_x_speed = 1
ball_y_speed = 1

ball = Actor("ball")
paddle = Actor("paddle")
paddle.left = 0
paddle.bottom = HEIGHT 

def draw():
    screen.fill(yellow)
    ball.draw()
    paddle.draw()

def update():
    move_ball()

def on_mouse_move(pos) :
  print(pos)
  print(ball.bottom)


def move_ball():
  
  ball.x += ball_x_speed
  ball.y += ball_y_speed

  check_boundaries()


def check_boundaries():
  global ball_x_speed, ball_y_speed

  if ball.bottom > HEIGHT or ball.top < 0 :
    ball_y_speed *= -1

  elif ball.left < 0 or ball.right > WIDTH :
    ball_x_speed *=-1  



pgzrun.go()    


