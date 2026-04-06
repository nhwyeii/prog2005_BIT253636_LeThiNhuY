s = input()

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(s)

print("Đã lưu vào file output.txt")