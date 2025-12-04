# Vương Giang Nam, mssv 245752021610085

import numpy as np

# Khai báo kiểu dữ liệu cho mảng có cấu trúc
data_type = [('name', 'U10'), ('class', int), ('height', float)]

# Danh sách sinh viên
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]

# Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)

print("Mảng ban đầu:")
print(students)

# Sắp xếp theo lớp, sau đó theo chiều cao
sorted_students = np.sort(students, order=['class', 'height'])

print("Mảng sau khi sắp xếp:")
print(sorted_students)
