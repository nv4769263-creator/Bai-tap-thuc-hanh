# Vương Giang Nam, mssv 245752021610085
# Chương trình máy tính đơn giản

# Hàm cộng hai số
def add(x, y):
    return x + y

# Hàm trừ hai số
def subtract(x, y):
    return x - y

# Hàm nhân hai số
def multiply(x, y):
    return x * y

# Hàm chia hai số
def divide(x, y):
    return x / y

# Hiển thị menu lựa chọn
print("Chọn phép tính:")
print("1. Cộng")
print("2. Trừ")
print("3. Nhân")
print("4. Chia")

# Nhập lựa chọn và hai số
choice = input("Nhập lựa chọn (1/2/3/4): ")

num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))

# Thực hiện phép tính
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    if num2 != 0:
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Lỗi: không thể chia cho 0!")
else:
    print("Lựa chọn không hợp lệ!")