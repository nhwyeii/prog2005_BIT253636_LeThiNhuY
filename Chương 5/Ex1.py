import matplotlib.pyplot as plt
labels = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yếu', 'Kém']
values = [6, 10, 12, 4, 1]
plt.bar(labels, values)

# Tiêu đề và nhãn
plt.title('Kết quả học tập')
plt.xlabel('Mức độ')
plt.ylabel('Số lượng')

plt.show()
