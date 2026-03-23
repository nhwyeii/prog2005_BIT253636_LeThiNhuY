r = int(input("Hàng: "))
c = int(input("Cột: "))

A = []
B = []
2
print("Nhập A:")
for i in range(r):
    row = list(map(int, input().split()))
    A.append(row)
print("Nhập B:")
for i in range(r):
    row = list(map(int, input().split()))
    B.append(row)
C = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print("Kết quả:")
for row in C:
    print(row)