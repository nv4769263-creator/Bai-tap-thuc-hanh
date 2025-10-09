# Vương Giang Nam, mssv 245752021610085

str=input("nhập chuỗi:")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
    print (dict)