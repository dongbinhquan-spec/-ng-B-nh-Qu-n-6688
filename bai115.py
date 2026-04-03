import tkinter as tk

# 1. HÀM MÔ PHỎNG LOGIC C
def strcmp(s1, s2):
    # Trả về số dương nếu s1 > s2, số âm nếu s1 < s2, 0 nếu bằng nhau
    return (s1 > s2) - (s1 < s2)

def strchr(s, char):
    # Tìm vị trí đầu tiên của ký tự char
    index = s.find(char)
    return s[index:] if index != -1 else "Không tìm thấy"

def strrchr(s, char):
    # Tìm vị trí cuối cùng (reverse) của ký tự char
    index = s.rfind(char)
    return s[index:] if index != -1 else "Không tìm thấy"

# 2. HÀM XỬ LÝ SỰ KIỆN KHI BẤM NÚT
def thuc_thi():
    chuoi = entry_s.get()
    char_m = 'm'
    char_o = 'o'
    
    # Thực hiện các hàm
    res_chr = strchr(chuoi, char_m)
    res_rchr = strrchr(chuoi, char_o)
    
    # Sắp xếp danh sách mẫu bằng strcmp
    danh_sach = ["brown", "black", "blue"]
    # Thuật toán sắp xếp cơ bản dùng logic strcmp
    danh_sach.sort(key=lambda x: x) # Python sort mặc định dùng logic so sánh tương tự strcmp
    
    # Hiển thị lên màn hình
    kq = f"Chuoi goc: [{chuoi}]\n"
    kq += f"strchr(s, '{char_m}'): [{res_chr}]\n"
    kq += f"strrchr(s, '{char_o}'): [{res_rchr}]\n"
    kq += f"Sap xep: {' '.join(danh_sach)}"
    
    label_kq.config(text=kq)

# 3. TẠO GIAO DIỆN ĐƠN GIẢN
root = tk.Tk()
root.title("Bài 115 - Simple")
root.geometry("500x300")

tk.Label(root, text="Nhập chuỗi:").pack(pady=5)
entry_s = tk.Entry(root, width=50)
entry_s.insert(0, "jackdaws love my big sphinx of quartz")
entry_s.pack(pady=5)

tk.Button(root, text="Chạy mô phỏng", command=thuc_thi, bg="lightblue").pack(pady=10)

label_kq = tk.Label(root, text="", justify="left", font=("Courier", 10), bg="white", width=50, height=8, anchor="nw")
label_kq.pack(pady=10)

root.mainloop()
