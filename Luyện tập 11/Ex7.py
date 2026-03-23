import csv

name = input("Tên: ")
age = input("Tuổi: ")
id = input("ID: ")

with open("nv.txt", "w") as f:
    f.write(name + " " + age + " " + id)

with open("nv.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([name, age, id])

print("Đã lưu file")