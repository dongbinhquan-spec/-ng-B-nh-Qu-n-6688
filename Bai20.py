import tkinter as tk
from tkinter import messagebox

def tinh_tien():
    try:
        kw = int(entry_kw.get())
        
        if kw < 0:
            messagebox.showerror("Lỗi", "Số kW phải >= 0")
            return
        
        if kw <= 100:
            tien = kw * 500
        elif kw <= 250:
            tien = 100 * 500 + (kw - 100) * 800
        elif kw <= 350:
            tien = 100 * 500 + 150 * 800 + (kw - 250) * 1000
        else:
            tien = 100 * 500 + 150 * 800 + 100 * 1000 + (kw - 350) * 1500
        
        label_kq.config(text=f"Chi phí: {tien} đồng")
    
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")

# Tạo cửa sổ
window = tk.Tk()
window.title("Tính tiền điện")
window.geometry("350x200")

# Tiêu đề
label_title = tk.Label(window, text="TÍNH TIỀN ĐIỆN", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

# Nhập kW
frame = tk.Frame(window)
frame.pack()

label_kw = tk.Label(frame, text="Nhập số kW:")
label_kw.pack(side="left", padx=5)

entry_kw = tk.Entry(frame)
entry_kw.pack(side="left")

# Nút tính
btn = tk.Button(window, text="Tính tiền", command=tinh_tien)
btn.pack(pady=10)

# Kết quả
label_kq = tk.Label(window, text="Chi phí: ")
label_kq.pack()

# Chạy chương trình
window.mainloop()
