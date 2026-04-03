import tkinter as tk
import os

# 1. HÀM TẠO FILE DỮ LIỆU MẪU (Để bạn có cái để chạy thử)
def tao_du_lieu_mau():
    with open("NUMBER1.TXT", "w") as f:
        f.write("1 5 9 13 17 19")
    with open("NUMBER2.TXT", "w") as f:
        f.write("2 6 10 14 18 22")
    return "Đã tạo 2 file mẫu: NUMBER1.TXT và NUMBER2.TXT\n"

# 2. HÀM TRỘN FILE (LOGIC CHÍNH)
def merge_files():
    f1_name = "NUMBER1.TXT"
    f2_name = "NUMBER2.TXT"
    f3_name = "NUMBER.TXT"
    
    log = tao_du_lieu_mau()
    
    try:
        # Mở 2 file nguồn để đọc và 1 file đích để ghi
        with open(f1_name, "r") as f1, open(f2_name, "r") as f2, open(f3_name, "w") as f3:
            # Đọc toàn bộ số và biến thành generator (để không dùng mảng phụ lớn)
            nums1 = (int(x) for x in f1.read().split())
            nums2 = (int(x) for x in f2.read().split())
            
            # Lấy số đầu tiên của mỗi bên
            val1 = next(nums1, None)
            val2 = next(nums2, None)
            
            ket_qua = []
            while val1 is not None or val2 is not None:
                if val1 is not None and (val2 is None or val1 <= val2):
                    f3.write(f"{val1} ")
                    ket_qua.append(str(val1))
                    val1 = next(nums1, None)
                else:
                    f3.write(f"{val2} ")
                    ket_qua.append(str(val2))
                    val2 = next(nums2, None)
            
            log += "Tron ket thuc...\n"
            log += f"Nội dung {f3_name}: " + " ".join(ket_qua)
            
        label_kq.config(text=log)
        
    except FileNotFoundError:
        label_kq.config(text="Lỗi: Không tìm thấy file nguồn!")

# 3. GIAO DIỆN
root = tk.Tk()
root.title("Bài 188 - Merge Files")
root.geometry("550x350")

tk.Label(root, text="BÀI 188: TRỘN HAI TẬP TIN SỐ NGUYÊN", font=("Arial", 12, "bold")).pack(pady=10)

# Khung mô phỏng màn hình console
label_kq = tk.Label(root, text="Nhấn nút để bắt đầu trộn...", font=("Courier", 10), 
                    bg="#222", fg="#00FF00", justify="left", anchor="nw", 
                    padx=10, pady=10, width=65, height=12, wraplength=500)
label_kq.pack(pady=10)

tk.Button(root, text="Chạy SORT NUMBER1 NUMBER2 NUMBER", command=merge_files, 
          bg="red", fg="white", font=("Arial", 10, "bold")).pack(pady=5)

root.mainloop()
