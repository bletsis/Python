import turtle

s = turtle.getscreen()
t = turtle
t.speed(1000)
t.pencolor("white")
t.goto(-700, 400)
t.pencolor("black")
for i in range(1, 1000, 5):
    t.fd(i)
    t.rt(90)
    t.fd(i)
    t.rt(90)
    t.fd(i)
    t.rt(90)
    t.fd(i)
    t.rt(90)
