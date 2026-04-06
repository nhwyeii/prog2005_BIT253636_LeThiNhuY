a = float(input())
b = float(input())
c = float(input())

trung_binh = (a + b + c ) / 3
print(trung_binh)

if trung_binh >= 8:
    print("Giỏi")
elif 7.9 >= trung_binh >= 6.5:
    print("Khá")
elif 6.4 >= trung_binh >= 5:
    print("Trung bình")
else:
    print("Yếu")