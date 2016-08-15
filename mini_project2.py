import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("white")

    sanya = turtle.Turtle()
    sanya.shape("circle")
    sanya.color("red")
    #sanya.right(250)
    sanya.right(90)
    j = 0
    while(j<36):
        k=0
        while(k < 3):
            sanya.forward(80)
            sanya.right(120)
            sanya.forward(80)
            sanya.dot()
            k = k+1
        sanya.right(10)
        j=j+1
    sanya.forward(220)

    window.exitonclick()
draw_square()
