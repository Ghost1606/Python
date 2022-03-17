a = 2000
b = 3000
c = 3500

a1 = int(input("아메리카노 판매 개수: "))
b1 = int(input("카페라떼 판매 개수: "))
c1 = int(input("카푸치노 판매 개수: "))

sales = a * a1
sales = sales + b * b1
sales = sales + c * c1
print("총 매출은" ,sales, "입니다")
