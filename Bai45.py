import tkinter as tk
from tkinter import messagebox

def ve_tam_giac():
    try:
        n = int(entry_n.get())

        if n <= 0 or n >= 5:
            messagebox.showerror("Lỗi", "Nhập n (0 < n < 5)")
            return

        text_kq.delete("1.0", tk.END)

        # Tam giác trên
        for i in range(1, n + 1):
            dong = ""
            for j in range(1, i + 1):
                dong += str(j) + " "
            for j in range(i + 1, 2 * n):
                dong += "  "
            for j in range(i, 0, -1):
                dong += str(j) + " "
            text_kq.insert(tk.END, dong.strip() + "\n")

        # Tam giác dưới
        for i in range(n - 1, 0, -1):
            dong = ""
            for j in range(1, i + 1):
                dong += str(j) + " "
            for j in range(i + 1, 2 * n):
                dong += "  "
            for j in range(i, 0, -1):
                dong += str(j) + " "
            text_kq.insert(tk.END, dong.strip() + "\n")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Tạo cửa sổ
window = tk.Tk()
window.title("Vẽ tam giác đối đỉnh")
window.geometry("500x350")

# Tiêu đề
label_title = tk.Label(window, text="TAM GIÁC ĐỐI ĐỈNH", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

# Nhập n
frame = tk.Frame(window)
frame.pack()

label_n = tk.Label(frame, text="Nhập n (n < 5):")
label_n.pack(side="left", padx=5)

entry_n = tk.Entry(frame)
entry_n.pack(side="left")

# Nút vẽ
btn = tk.Button(window, text="Vẽ", command=ve_tam_giac)
btn.pack(pady=10)

# Hiển thị kết quả
text_kq = tk.Text(window, height=10, width=50)
text_kq.pack()

# Chạy chương trình
window.mainloop()
