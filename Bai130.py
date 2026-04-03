import tkinter as tk
from fnmatch import fnmatch

# 1. HÀM LOGIC TÌM KIẾM
def tim_kiem_wildcard():
    # Lấy danh sách từ và mẫu tìm kiếm từ giao diện
    danh_sach_raw = entry_ds.get()
    mau_tim_kiem = entry_mau.get()
    
    # Chuyển chuỗi thành danh sách các từ
    ds_tu = danh_sach_raw.split()
    ket_qua = []
    
    for tu in ds_tu:
        # fnmatch kiểm tra xem 'tu' có khớp với 'mau_tim_kiem' (có dấu *) không
        if fnmatch(tu, mau_tim_kiem):
            ket_qua.append(tu)
    
    # Hiển thị kết quả lên giao diện
    hien_thi = f"Tim [{mau_tim_kiem}]: " + (" ".join(ket_qua) if ket_qua else "Không thấy")
    label_kq.config(text=hien_thi)

# 2. GIAO DIỆN ĐỒ HỌA ĐƠN GIẢN
root = tk.Tk()
root.title("Bài 130 - Tìm kiếm Wildcard")
root.geometry("500x350")
root.configure(padx=20, pady=20)

# Nhập danh sách từ
tk.Label(root, text="Danh sách các từ (cách nhau bởi khoảng trắng):").pack(anchor="w")
entry_ds = tk.Entry(root, width=50)
entry_ds.insert(0, "television menu editions education")
entry_ds.pack(pady=5)

# Nhập mẫu tìm kiếm
tk.Label(root, text="Nhập mẫu tìm kiếm (ví dụ: *e*u*):").pack(anchor="w", pady=(10, 0))
entry_mau = tk.Entry(root, width=20)
entry_mau.insert(0, "*e*u*")
entry_mau.pack(anchor="w", pady=5)

# Nút thực hiện
tk.Button(root, text="Tìm kiếm", command=tim_kiem_wildcard, bg="#4CAF50", fg="white").pack(pady=15)

# Khu vực hiển thị kết quả
tk.Label(root, text="KẾT QUẢ:", font=("Arial", 10, "bold")).pack(anchor="w")
label_kq = tk.Label(root, text="", font=("Courier", 11), fg="blue", wraplength=450, justify="left")
label_kq.pack(pady=10, fill="x")

root.mainloop()
