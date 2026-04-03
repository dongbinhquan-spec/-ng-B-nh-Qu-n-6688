import tkinter as tk
from tkinter import messagebox
import random

entries = []
matrix = []

def tao_ma_tran():
    global entries, matrix

    try:
        n = int(entry_n.get())
        if n <= 0:
            messagebox.showerror("Lỗi", "n > 0")
            return

        # Xóa bảng cũ
        for widget in frame_matrix.winfo_children():
            widget.destroy()

        entries = []
        matrix = []

        # Tạo bảng
        for i in range(n):
            row_entries = []
            row_values = []
            for j in range(n):
                val = random.randint(-100, 100)
                e = tk.Entry(frame_matrix, width=5, justify="center")
                e.grid(row=i, column=j, padx=2, pady=2)
                e.insert(0, str(val))

                row_entries.append(e)
                row_values.append(val)

            entries.append(row_entries)
            matrix.append(row_values)

    except:
        messagebox.showerror("Lỗi", "Nhập sai!")

def kiem_tra():
    try:
        n = len(entries)
        matrix = []

        # Lấy dữ liệu từ bảng
        for i in range(n):
            row = []
            for j in range(n):
                val = int(entries[i][j].get())
                row.append(val)
            matrix.append(row)

        la_don_vi = True

        for i in range(n):
            for j in range(n):
                if i == j and matrix[i][j] != 1:
                    la_don_vi = False
                if i != j and matrix[i][j] != 0:
                    la_don_vi = False

        label_kq.config(text="")

        if la_don_vi:
            label_kq.config(text="✅ Đây là ma trận đơn vị")
        else:
            text_kq.delete("1.0", tk.END)
            text_kq.insert(tk.END, "❌ Không phải ma trận đơn vị\n\n")
            text_kq.insert(tk.END, "Ma trận đơn vị:\n")

            for i in range(n):
                for j in range(n):
                    if i == j:
                        text_kq.insert(tk.END, "1 ")
                    else:
                        text_kq.insert(tk.END, "0 ")
                text_kq.insert(tk.END, "\n")

    except:
        messagebox.showerror("Lỗi", "Dữ liệu không hợp lệ!")

def reset():
    for widget in frame_matrix.winfo_children():
        widget.destroy()
    text_kq.delete("1.0", tk.END)
    label_kq.config(text="")

# Giao diện
window = tk.Tk()
window.title("Ma trận nâng cao")
window.geometry("600x450")

tk.Label(window, text="BÀI 88 (BẢNG)", font=("Arial", 14, "bold")).pack(pady=10)

frame_top = tk.Frame(window)
frame_top.pack()

tk.Label(frame_top, text="Nhập n:").pack(side="left")
entry_n = tk.Entry(frame_top, width=5)
entry_n.pack(side="left", padx=5)

tk.Button(window, text="Tạo ma trận", command=tao_ma_tran).pack(pady=5)
tk.Button(window, text="Kiểm tra", command=kiem_tra).pack(pady=5)
tk.Button(window, text="Reset", command=reset).pack(pady=5)

# Bảng ma trận
frame_matrix = tk.Frame(window)
frame_matrix.pack(pady=10)

# Kết quả
label_kq = tk.Label(window, text="", fg="green")
label_kq.pack()

text_kq = tk.Text(window, height=8, width=40)
text_kq.pack()

window.mainloop()
