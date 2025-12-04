# Vương Giang Nam, mssv 245752021610085

def binary_search(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == value:
            return True
        elif arr[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Nhập danh sách và sắp xếp
lst = list(map(int, input("Nhập danh sách số nguyên cách nhau bởi dấu cách: ").split()))
lst.sort()

# Nhập giá trị cần tìm
val = int(input("Nhập giá trị cần tìm: "))

# Gọi hàm tìm kiếm
if binary_search(lst, val):
    print("Giá trị tồn tại trong danh sách.")
else:
    print("Giá trị không tồn tại.")
