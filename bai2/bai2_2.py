# Vương Giang Nam, mssv 245752021610085

import math


x1=int(input("nhập giá trị n1:"))
y1=int(input("nhập giá trị y1:"))
x2=int(input("nhập giá trị x2:"))
y2=int(input("nhập giá trị y2:"))
d1=(x2-x1)*(x2-x1);
d2=(y2-y1)*(y2-y1);
res = math.sqrt(d1+d2)
print("khoảng cách giữa các điểm:",res);