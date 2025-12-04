# Vương Giang Nam, mssv 245752021610085

import tkinter as tk

root = tk.Tk()
root.title("Ví dụ Indicator Radio Button")

v = tk.IntVar()
v.set(1)

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print("Bạn chọn:", v.get())

tk.Label(root,
         text="Chọn ngôn ngữ lập trình yêu thích:",
         justify=tk.LEFT,
         padx=20).pack()

# Tạo radio button nhưng hiển thị dạng nút bấm (indicatoron=0)
for language, val in languages:
    tk.Radiobutton(root,
                   text=language,
                   indicatoron=0,   # biến thành nút bấm
                   width=20,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()
