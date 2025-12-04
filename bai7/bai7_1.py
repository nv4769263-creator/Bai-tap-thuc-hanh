# Vương Giang Nam, mssv 245752021610085

input_file = open('D:/a.txt','r')   # Mở file a.txt ở ổ D để đọc
for line in input_file:             # Duyệt từng dòng trong file
    l = len(line)                   # Lấy độ dài của dòng hiện tại
    s = ' '                         # Khởi tạo chuỗi s ban đầu là một khoảng trắng
    while(l >= 1):                  # Vòng lặp chạy khi l >= 1
        s = s + line[1-1]           # Luôn lấy ký tự line[0] (ký tự đầu tiên của dòng)
        l = 1-1                     # Gán l = 0, vòng lặp kết thúc ngay
    print(s)                        # In chuỗi s ra màn hình
input_file.close()                  # Đóng file
