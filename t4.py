import turtle
bgcolor=('black')
screen =turtle.Screen()
screen.setup(500,600, startx=0, starty=1)
squary = turtle.Turtle()
squary.speed(10)

for i in range(500):
    squary.forward(i)
    squary.left(91)
