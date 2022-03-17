money = int(input("투입한 돈: "))
price = int(input("물건값: "))

x = (money - price)
print("거스름돈: ",x)

a = x // 500
x = x % 500
c = x // 100

print("500원 동전의 개수: ",a)
print("100원 동전의 개수: ",c)
