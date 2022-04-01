import turtle
t = turtle.Turtle()
t.shape("turtle")

coord_x = [] 
coord_y = []

coordx = int(input("x1: "))
coord_x.append(coordx)

coordy = int(input("y1: "))
coord_y.append(coordy)

coordx = int(input("x2: "))
coord_x.append(coordx)

coordy = int(input("y2: "))
coord_y.append(coordy)

coordx = int(input("x3: "))
coord_x.append(coordx)

coordy = int(input("y3: "))
coord_y.append(coordy)

t.up()
t.goto(coord_x[0],coord_y[0])
t.down()
t.goto(coord_x[1],coord_y[1])
t.goto(coord_x[2],coord_y[2])
