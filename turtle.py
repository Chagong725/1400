  """module docstring turtle"""

import turtle

def get_dimentions(turtle, window, width, height):
    """Fills background and changes size"""
    window.screensize(width, height)
    turtle.speed(10)
    window.bgcolor("green")
    turtle.penup()


def draw_hexagon(turtle, color, scale):
    """Draws a hexagon"""
    turtle.color("black")
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    count = 0
    while count < 6:
        turtle.forward(100 * scale)
        turtle.lt(60)
        count += 1
    turtle.end_fill()
    turtle.penup()

def draw_star(turtle):
    """ Draws a star"""
    turtle.color("pink")
    turtle.pendown()
    count = 0
    turtle.fillcolor("#c23e8f")
    while count < 5:
        turtle.begin_fill()
        turtle.forward(155.4)
        turtle.rt(150)
        turtle.forward(100)
        turtle.rt(66)
        turtle.forward(85.05)
        turtle.end_fill()
        count +=1
    count = 0
    turtle.color("#B76E79")
    turtle.fillcolor("#912668")
    while count < 5:
        turtle.begin_fill()
        turtle.forward(155.4)
        turtle.lt(150)
        turtle.forward(100)
        turtle.lt(66)
        turtle.forward(85.05)
        turtle.end_fill()
        count +=1
    turtle.penup()

def draw_shuriken(turtle):
    """ Draws a shuriken"""
    turtle.color("black")
    turtle.pendown()
    count = 0
    turtle.fillcolor("#B76E79")
    turtle.begin_fill()
    while count < 5:
        turtle.forward(155.4)
        turtle.rt(150)
        turtle.forward(100)
        turtle.rt(66)
        turtle.forward(85.05)
        count +=1
    turtle.end_fill()
    count =0
    turtle.fillcolor( "white")
    turtle.begin_fill()
    while count<5:
        turtle.forward(85.05)
        turtle.lt(66)
        turtle.forward(100)
        turtle.lt(150)
        turtle.forward(155.4)
        count +=1
    turtle.end_fill()
    turtle.penup()


def main():
    '''
    Program starts here.
    '''
    turt = turtle.Turtle()
    window = turt.getscreen()
    colors = ["white", "#F7CAC9",  "pink", "#B76E79","#a24857", "#8d1919", "#dc2f02", "#f37a48", "orange", "#f5e65e", "#bbf261", "#36D457",  "green", "#3eb489", "#5dc9b6", "#6495ed","#002366","#30106b", "#673147","purple"]

    try:
        width = int(input())
        height = int(input())

    except ValueError:
        print('Width and height must be positive integers.')
        return

    if width < 1 or height < 1:
        print('Width and height must be positive integers.')
        return

    get_dimentions(turt, window, width, height)
    turt.goto(100,150)
    count = 0
    scale = 1
    while scale > 0:
        draw_hexagon(turt, colors[count], scale)
        turt.rt(30)
        scale -= .05
        count += 1
    turt.goto(-200,100)
    draw_star(turt)
    turt.goto(0,-150)
    draw_shuriken(turt)
    window.exitonclick()

if __name__ == "__main__":
    main()
