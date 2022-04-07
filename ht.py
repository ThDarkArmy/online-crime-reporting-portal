from time import sleep
import turtle

tr = turtle.Turtle()

def curve():
    for i in range(200):
        tr.right(1)
        tr.forward(1)

def hrt():
    tr.fillcolor("red")
    tr.begin_fill()
    tr.left(140)
    tr.forward(113)
    curve()
    tr.left(120)
    curve()
    tr.forward(122)
    tr.end_fill()


def tx():
    tr.up()
    tr.setpos(-68, 95)
    tr.down()
    tr.color("lightgreen")
    tr.write("Shweta", font={"verdana", 12, "bold"})



hrt()
tx()
sleep(100)

tr.ht()