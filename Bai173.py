import tkinter as tk
import random

# 1. HÀM XỬ LÝ FILE
def thuc_thi_file():
    file_int = "INTEGER.DAT"
    file_real = "REAL.DAT"
    
    # --- GHI FILE ---
    # Tạo 5 số nguyên và 5 số thực ngẫu nhiên
    ds_int = [random.randint(1000, 30000) for _ in range(5)]
    ds_real = [round(random.uniform(0.1, 0.9), 6) for _ in range(5)]
    
    # Ghi số nguyên vào file
    with open(file_int, "w") as f:
        f.write(" ".join(map(str, ds_int)))
        
    # Ghi số thực vào file
    with open(file_real, "w") as f:
        f.write(" ".join(map(str, ds_real)))
        
    log_văn_ban = "Ghi xong file...\n"
    log_văn_ban += "  " + "  ".join(map(str, ds_int)) + "\n"
    log_văn_ban += "  " + "  ".join(map(str, ds_real)) + "\n"

    # --- ĐỌC FILE ---
    with open(file_int, "r") as f:
        doc_int = f.read()
        
    with open(file_real, "r") as f:
        doc_real = f.read()
        
    log_văn_ban += "Doc xong file...\n"
    log_văn_ban += f"Dữ liệu số nguyên: {doc_int}\n"
    log_văn_ban += f"Dữ liệu số thực: {doc_real}"

    # Cập nhật kết quả lên màn hình
    label_kq.config(text=log_văn_ban)

# 2. GIAO DIỆN ĐỒ HỌA
root = tk.Tk()
root.title("Bài 173 - Quản lý Tập tin")
root.geometry("500x350")

tk.Label(root, text="BÀI 173: GHI VÀ ĐỌC FILE .DAT", font=("Arial", 12, "bold")).pack(pady=10)

tk.Button(root, text="Bắt đầu Ghi & Đọc File", command=thuc_thi_file, 
          bg="#2196F3", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5).pack(pady=10)

# Khung hiển thị giống màn hình Console trong ảnh
label_kq = tk.Label(root, text="Chưa có dữ liệu...", font=("Courier", 10), 
                    bg="#333", fg="#0f0", justify="left", anchor="nw", 
                    padx=10, pady=10, width=60, height=10)
label_kq.pack(pady=10)

root.mainloop()
