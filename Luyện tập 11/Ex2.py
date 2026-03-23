chuoi5 = ['python', '111', 'hi', '2', 'a']
chuoi5.sort()

print("Danh sách sau khi sort:", chuoi5)
x = input("Nhập chuỗi")

left = 0
right = len(chuoi5) - 1
found = -1

while left <= right:
    mid = (left + right) // 2
    print("Đang xét:", chuoi5[mid])  # để dễ hiểu

    if chuoi5[mid] == x:
        found = mid
        break
    elif x < chuoi5[mid]:
        right = mid - 1
    else:
        left = mid + 1
if found != -1:
    print("Tìm thấy tại vị trí:", found)
else:
    print("Không tìm thấy")