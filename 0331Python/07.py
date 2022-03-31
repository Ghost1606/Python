'''
score = int(input("성적을 입력하시오: "))
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")

num = int(input("정수를 입력하시오: "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

age = int(input("나이를 입력하시오: "))
if age >= 15:
    print("이 영화를 보실 수 있습니다.")
else:
    print("이 영화를 보실 수 업습니다.")

import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(100,100)
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(100,0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100,-100)
t.write("거북이가 여기로 오면 음수입니다.")

t.goto(0,0)
t.pendown()
s = turtle.textinput("", "숫자를 입력하시오: ")
r = int(s)

if r > 0:
    t.goto(100,100)
if r == 0:
    t.goto(100,0)
if r < 0:
    t.goto(100,-100)'''

age = int(input("나이를 입력하시오: "))
height = int(input("키를 입력하시오: "))

if (age >= 10 and height >=165) :
    print("놀이기구를 탈 수 있다.")
else:
    print("놀이기구를 탈 수 없다.")
    
