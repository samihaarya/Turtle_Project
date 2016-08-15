print  "making the circles out of square"
import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.speed("normal")
    j = 0
    while(j<36):
        i = 0
        while(i<4):
            brad.forward(100)
            brad.right(90)
            i=i+1
        brad.right(10)
        j=j+1


draw_square()
