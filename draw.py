import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_snowman():
    turtle.speed(2)
    turtle.bgcolor("sky blue")

    # Draw bottom circle
    draw_circle("white", 60, 0, -100)

    # Draw middle circle
    draw_circle("white", 45, 0, 0)

    # Draw top circle
    draw_circle("white", 30, 0, 80)

    # Draw eyes
    draw_circle("black", 5, -15, 110)
    draw_circle("black", 5, 15, 110)

    # Draw nose
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.color("orange")
    turtle.begin_fill()
    turtle.circle(5, steps=3)
    turtle.end_fill()

    # Draw buttons
    draw_circle("black", 5, 0, 70)
    draw_circle("black", 5, 0, 40)
    draw_circle("black", 5, 0, 10)

    # Draw arms
    turtle.penup()
    turtle.goto(-45, 0)
    turtle.pendown()
    turtle.pensize(5)
    turtle.goto(-100, 50)
    turtle.penup()
    turtle.goto(45, 0)
    turtle.pendown()
    turtle.goto(100, 50)

    turtle.hideturtle()

draw_snowman()
turtle.done()

