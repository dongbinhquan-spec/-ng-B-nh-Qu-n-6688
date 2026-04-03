import tkinter as tk
import random

# 1. HÀM TÍNH ĐỊNH THỨC (ĐỆ QUY)
def tinh_dinh_thuc(matrix):
    n = len(matrix)
    # Trường hợp cơ bản: Ma trận 1x1
    if n == 1:
        return matrix[0][0]
    # Trường hợp cơ bản: Ma trận 2x2 (để chạy nhanh hơn)
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        # Tạo ma trận con bằng cách bỏ dòng 0 và cột j
        sub_matrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        # Công thức truy hồi: (-1)^j * a[0][j] * det(ma trận con)
        det += ((-1) ** j) * matrix[0][j] * tinh_dinh_thuc(sub_matrix)
    return det

# 2. HÀM XỬ LÝ GIAO DIỆN
def thuc_thi():
    try:
        n = int(entry_n.get())
        if n < 1: raise ValueError
        
        # Tạo ma trận ngẫu nhiên từ [-10, 10]
        matrix = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
        
        # Hiển thị ma trận lên màn hình
        txt_matrix.config(state='normal')
        txt_matrix.delete('1.0', tk.END)
        for row in matrix:
            txt_matrix.insert(tk.END, "  ".join(f"{x:3}" for x in row) + "\n")
        txt_matrix.config(state='disabled')
        
        # Tính và hiển thị định thức
        ket_qua = tinh_dinh_thuc(matrix)
        lbl_res.config(text=f"Det(A) = {ket_qua}")
        
    except ValueError:
        lbl_res.config(text="Vui lòng nhập số nguyên dương!")

# 3. GIAO DIỆN
root = tk.Tk()
root.title("Bài 157 - Tính Định Thức Ma Trận")
root.geometry("400x450")

tk.Label(root, text="Nhập bậc ma trận (n):", font=("Arial", 10)).pack(pady=5)
entry_n = tk.Entry(root, width=10, justify='center')
entry_n.insert(0, "4")
entry_n.pack()

tk.Button(root, text="Tạo Ma Trận & Tính", command=thuc_thi, bg="orange").pack(pady=10)

tk.Label(root, text="Ma trận ngẫu nhiên:").pack()
txt_matrix = tk.Text(root, height=10, width=40, state='disabled', font=("Courier", 12))
txt_matrix.pack(pady=5)

lbl_res = tk.Label(root, text="Det(A) = ?", font=("Arial", 12, "bold"), fg="blue")
lbl_res.pack(pady=10)

root.mainloop()
