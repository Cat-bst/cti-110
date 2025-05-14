import turtle

t = turtle.Turtle()

for _ in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.goto(-150, 0) 
t.pendown()

sides = 0
while sides < 3:
    t.forward(100)
    t.right(120)
    sides += 1

turtle.done()