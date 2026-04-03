import tkinter as tk
from tkinter import messagebox

def tim_max_xuat_hien():
    try:
        # Lấy dữ liệu từ ô nhập (cách nhau bằng dấu cách)
        arr = entry_arr.get().strip().split()
        arr = list(map(int, arr))

        if len(arr) == 0:
            messagebox.showerror("Lỗi", "Vui lòng nhập mảng!")
            return

        # Đếm số lần xuất hiện
        dem = {}
        for x in arr:
            dem[x] = dem.get(x, 0) + 1

        max_lan = max(dem.values())

        # Lấy các phần tử xuất hiện nhiều nhất
        kq = []
        for k, v in dem.items():
            if v == max_lan:
                kq.append(f"{k}[{v}]")

        # Hiển thị
        label_kq.config(text="Phần tử nhiều nhất: " + " ".join(kq))

    except ValueError:
        messagebox.showerror("Lỗi", "Nhập số cách nhau bằng dấu cách!")

# Tạo cửa sổ
window = tk.Tk()
window.title("Tìm phần tử xuất hiện nhiều nhất")
window.geometry("500x250")

# Tiêu đề
tk.Label(window, text="BÀI 76", font=("Arial", 14, "bold")).pack(pady=10)

# Nhập mảng
frame = tk.Frame(window)
frame.pack()

tk.Label(frame, text="Nhập mảng:").pack(side="left")
entry_arr = tk.Entry(frame, width=40)
entry_arr.pack(side="left", padx=5)

# Nút xử lý
tk.Button(window, text="Tìm", command=tim_max_xuat_hien).pack(pady=10)

# Kết quả
label_kq = tk.Label(window, text="Kết quả: ")
label_kq.pack(pady=10)

# Chạy
window.mainloop()
