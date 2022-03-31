import turtle
t = turtle.Turtle()
t.shape("turtle")

color_list = [ "yellow", "red", "blue", "green" ]

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(100)
t.up()
t.goto(50 ,0)
t.down()
t.end_fill()

t.fillcolor(color_list[1])
t.begin_fill()
t.circle(100)
t.up()
t.goto(100 ,0)
t.down()
t.end_fill()

t.fillcolor(color_list[2])
t.begin_fill()
t.circle(100)
t.up()
t.goto(150 ,0)
t.down()
t.end_fill()

t.fillcolor(color_list[3])
t.begin_fill()
t.circle(100)
t.end_fill()
