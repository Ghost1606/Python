'''
kor = [60,70,80,90,100]
total = kor[0]+kor[1]+kor[2]+kor[3]+kor[4]
print(total // 5)

name =[]
name.append("Hong")
name.append("Kim")
name.append("Lee")
name.append("Park")
print(name)

score = [60,70,80,90,100]
print(score)
score.append(50)
print(score)

sum = score[0]+score[1]+score[2]+score[3]+score[4]+score[5]

avg = sum / 6
print("총점= "+str(sum)+"평균= "+str(avg)+"입니다.")'''

eng = []
a = int(input("영어점수를 입력해주세요!"))
eng.append(a)

a = int(input("영어점수를 입력해주세요!"))
eng.append(a)

a = int(input("영어점수를 입력해주세요!"))
eng.append(a)

a = int(input("영어점수를 입력해주세요!"))
eng.append(a)

a = int(input("영어점수를 입력해주세요!"))
eng.append(a)

print(eng)

sum = eng[0]+eng[1]+eng[2]+eng[3]+eng[4]
avg = sum / 5
print("총점 = "+str(sum)+"평균 = "+str(avg))
