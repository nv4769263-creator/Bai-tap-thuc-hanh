# Vương Giang Nam, mssv 245752021610085

# nhập dãy từ bàn phím, in ra từ dài nhất, in ra mọi từ cùng độ dài
ds = input("nhập dãy số:").split()
maxlen = max(len(w) for w in ds )
for w in ds:
    if len(w) == maxlen:
        print(w)