import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("#0b0c10")
screen.title('IT126')

t = turtle.Turtle()
t.speed(0)
t.width(2)

def draw_frame():
    t.penup()
    t.goto(-280, -110)
    t.pendown()
    t.width(4)

    sides = [560, 220, 560, 220]

    for i, length in enumerate(sides):
        color = colorsys.hsv_to_rgb(0.5 + i * 0.1, 0.9, 1.0)
        t.pencolor(color)
        t.forward(length)
        t.left(90)

def draw_text(text, y, size, color):
    t.penup()
    t.goto(3, y - 3)
    t.pencolor("#1f2833")
    t.write(text, align='center', font=("Arial", size, "bold"))

    t.goto(0, y)
    t.pencolor()
    t.write(text, align='center', font=("Arial", size, 'bold'))


def draw_start(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

draw_frame()

draw_text("IUCA", 45, 36, "#66fcf1")
draw_text('IT126', -15, 28, "#76122b")
draw_text('THE BEST', -75, 32, "#011006")


draw_start(-240, 60,25, "#d1486b")
draw_start(215, 60,25, "#d1486b")
draw_start(-240, 60,25, "#d1486b")
draw_start(215, 60,25, "#d1486b")


turtle.done()








# steps = 120

# for i in range(steps):
#     hue = 0.5 + (i / steps) *0.4
#     color = colorsys.hsv_to_rgb(hue, 0.85, 1.0)
#     t.pencolor(color)

#     t.forward(i*2.5)
#     t.right(144)
#     t.right(3)


# t.hideturtle()
# turtle.done()









# screen = turtle.Screen()
# screen.bgcolor('black')
# t = turtle.Turtle()
# t.speed(10)
# t.width(2)

# n = 72

# for i in range(n):
#     color = colorsys.hsv_to_rgb(i / n, 1.0, 1.0)
#     t.pencolor(color)

#     t.circle(120)
#     t.left(360 / n)

# t.hideturtle()
# turtle.done()