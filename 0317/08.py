import turtle
t = turtle.Turtle()
t.shape("turtle")

a = int(input("몇각형을 그리시겠어요?(3-6):"))

for i in range(a) :
    t.forward(100)
    t.left(360//a)
