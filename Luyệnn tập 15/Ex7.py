students = {"Linhden":9, "Hạnh":9, "Hy":8}
def average_score(data):
    return sum(data.values()) / len(data)

print("Điểm trung bình:", average_score(students))