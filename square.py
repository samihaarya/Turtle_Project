import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle() # this is how we grab the turtle
    #brad.forward(100) #here 100 is the distance we travelled
    #brad.right(90) #going straight at 90 degree
    brad.shape("circle")
    brad.color("yellow","brown")
    brad.speed("slowest")
    i = 0
    while(i<4):
        brad.forward(100)
        brad.right(90)
        i=i+1

    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("blue","black")
    angie.circle(50)

    mehgan = turtle.Turtle()
    mehgan.shape("arrow")
    mehgan.color("green")


    mehgan.right(120)
    j=0
    while (j < 6):
        mehgan.forward(70)
        mehgan.right(60)
        j =j+1

    sanya = turtle.Turtle()
    sanya.shape("classic")
    sanya.color("black")
    sanya.right(250)

    k=0
    while(k < 3):
        sanya.forward(80)
        sanya.right(120)
        k = k+1

    window.exitonclick()
    #turtle.bye()
draw_shapes()
