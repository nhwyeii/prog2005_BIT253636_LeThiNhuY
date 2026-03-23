nums = list(map(int, input("Nhập").split()))
tong = 0
for x in nums:
    if x % 2 == 0:
        print(x)
        tong += x
print(tong)