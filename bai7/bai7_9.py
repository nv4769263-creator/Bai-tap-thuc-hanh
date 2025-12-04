# Vương Giang Nam, mssv 245752021610085

# Mở file nguồn để đọc
with open('nguon.txt', 'r', encoding='utf-8') as file_nguon:
    noi_dung = file_nguon.read()

# Mở file đích để ghi
with open('dich.txt', 'w', encoding='utf-8') as file_dich:
    file_dich.write(noi_dung)
