from visual import *
ball = sphere(pos=(-5,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=(6,0,0), size=(0.2,12,12), color=color.green)
ball.velocity = vector(25,0,0)
deltat = 0.005
t = 0
ball.pos = ball.pos + ball.velocity*deltat
while t<3:
    ball.pos = ball.pos + ball.velocity*deltat
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
    elif  ball.pos.x < -20:
        ball.velocity.x = -ball.velocity.x
    rate(100)
    t = t + deltat