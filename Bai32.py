import tkinter as tk
from tkinter import messagebox

def sinh_day():
    try:
        n = int(entry_n.get())

        if n <= 0:
            messagebox.showerror("Lỗi", "Nhập số nguyên dương!")
            return

        day = []
        dem = 1
        x = n

        day.append(str(x))

        while x != 1:
            if x % 2 == 0:
                x = x // 2
            else:
                x = 3 * x + 1
            day.append(str(x))
            dem += 1

        # Hiển thị kết quả
        text_kq.delete("1.0", tk.END)
        text_kq.insert(tk.END, " ".join(day))
        label_dem.config(text=f"Số phần tử: {dem}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Tạo cửa sổ
window = tk.Tk()
window.title("Dãy Hailstone (Collatz)")
window.geometry("500x300")

# Tiêu đề
label_title = tk.Label(window, text="DÃY HAILSTONE", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

# Nhập n
frame = tk.Frame(window)
frame.pack()

label_n = tk.Label(frame, text="Nhập n:")
label_n.pack(side="left", padx=5)

entry_n = tk.Entry(frame)
entry_n.pack(side="left")

# Nút sinh dãy
btn = tk.Button(window, text="Sinh dãy", command=sinh_day)
btn.pack(pady=10)

# Hiển thị dãy
text_kq = tk.Text(window, height=5, width=60)
text_kq.pack()

# Hiển thị số phần tử
label_dem = tk.Label(window, text="Số phần tử: ")
label_dem.pack(pady=5)

# Chạy chương trình
window.mainloop()
