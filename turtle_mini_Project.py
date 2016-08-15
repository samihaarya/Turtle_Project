import turtle
def draw_name():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("black")
    brad.speed("slow")

    brad.dot()
    #for letter s
    #brad.right(-60)
    brad.forward(65)
    brad.left(90)
    brad.forward(40)
    brad.left(90)
    brad.forward(65)
    brad.right(90)
    brad.forward(40)
    brad.right(90)
    brad.forward(65)
    brad.backward(65)
    brad.left(90)
    brad.backward(40)
    brad.right(90)
    brad.forward(65)
    brad.right(90)
    brad.forward(40)
    brad.dot()
    brad.setpos(120,0)

#for letter a
    brad.dot()
    brad.right(-150)
    brad.forward(100)
    brad.right(120)
    brad.forward(100)
    brad.backward(50)
    brad.right(120)
    brad.forward(55)
    brad.backward(55)
    brad.left(120)
    brad.forward(50)
    brad.dot()




    window.exitonclick()
draw_name()
