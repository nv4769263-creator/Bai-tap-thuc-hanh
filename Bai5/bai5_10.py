# Vương Giang Nam, mssv 245752021610085

def bubbleSort(arr):
    n = len(arr)
    # Lặp qua tất cả các phần tử
    for i in range(n - 1):
        swapped = False
        # Vòng lặp bên trong để so sánh các cặp phần tử
        for j in range(n - i - 1):  # giảm dần phạm vi vì phần tử cuối đã đúng vị trí
            if arr[j] > arr[j + 1]:
                # Hoán đổi nếu phần tử trước lớn hơn phần tử sau
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Nếu không có hoán đổi nào thì mảng đã được sắp xếp
        if not swapped:
            break
    return arr

# Ví dụ sử dụng
data = [14, 46, 43, 27, 57, 41, 45, 21, 70]
print("Mảng ban đầu:", data)
print("Mảng sau khi sắp xếp:", bubbleSort(data))
