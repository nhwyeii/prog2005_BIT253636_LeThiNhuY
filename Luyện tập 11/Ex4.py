lst = [1, 2, 3, 4, 5]
#Thêm phần tử
x = int(input("Nhập thêm: "))
lst.append(x)

#Nhập k và kiểm tra số lần
k = int(input())
print( lst.count(k))

# Tổng các số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
tong = 0
for i in lst:
    if is_prime(i):
        tong += i
print(tong)

#Sắp xếp dsach
lst.sort()
print(lst)

#Xóa dsach
lst.clear()
print(lst)