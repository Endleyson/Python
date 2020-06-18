import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.shape('triangle')
    brad.color('yellow')
    brad.speed(2)
    brad.forward(100)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(200)
    brad.right(90)
    window.exitonclick()
    
draw_square()