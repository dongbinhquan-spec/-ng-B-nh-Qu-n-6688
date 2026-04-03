import tkinter as tk

# 1. CẤU TRÚC NODE VÀ CÂY BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# 2. THUẬT TOÁN TÌM TỔ TIÊN CHUNG GẦN NHẤT (LCA)
def find_lca(root, x, y):
    if root is None:
        return None

    # Nếu cả x và y đều nhỏ hơn gốc, LCA nằm bên trái
    if x < root.key and y < root.key:
        return find_lca(root.left, x, y)

    # Nếu cả x và y đều lớn hơn gốc, LCA nằm bên phải
    if x > root.key and y > root.key:
        return find_lca(root.right, x, y)

    # Nếu x < root < y hoặc ngược lại, root chính là LCA
    return root

# 3. GIAO DIỆN ĐỒ HỌA
def xu_ly():
    try:
        # Lấy dữ liệu cây
        ds_so = [int(n) for n in entry_tree.get().split() if n != '0']
        if not ds_so: return
        
        # Xây dựng cây
        root_node = None
        for so in ds_so:
            root_node = insert(root_node, so)
        
        # Lấy cặp x, y cần tìm
        x = int(entry_x.get())
        y = int(entry_y.get())
        
        # Tìm LCA
        lca = find_lca(root_node, x, y)
        
        if lca:
            lbl_res.config(text=f"Node cha (LCA) của {x} và {y} là: {lca.key}", fg="blue")
        else:
            lbl_res.config(text="Không tìm thấy node trong cây!", fg="red")
            
    except ValueError:
        lbl_res.config(text="Vui lòng nhập số hợp lệ!", fg="red")

root = tk.Tk()
root.title("Bài 227 - Tìm cha chung gần nhất (BST)")
root.geometry("500x350")

# Input dãy số xây cây
tk.Label(root, text="Nhập dãy số xây cây (nhập 0 để dừng):").pack(pady=5)
entry_tree = tk.Entry(root, width=50)
entry_tree.insert(0, "9 3 16 14 2 5 4 8 18 0")
entry_tree.pack()

# Input x và y
frame_xy = tk.Frame(root)
frame_xy.pack(pady=10)

tk.Label(frame_xy, text="Nhập a:").grid(row=0, column=0)
entry_x = tk.Entry(frame_xy, width=5)
entry_x.insert(0, "4")
entry_x.grid(row=0, column=1, padx=5)

tk.Label(frame_xy, text="Nhập b:").grid(row=0, column=2)
entry_y = tk.Entry(frame_xy, width=5)
entry_y.insert(0, "14")
entry_y.grid(row=0, column=3, padx=5)

# Button
tk.Button(root, text="Tìm Node Cha", command=xu_ly, bg="green", fg="white").pack(pady=10)

# Kết quả
lbl_res = tk.Label(root, text="Node cha: ?", font=("Arial", 12, "bold"))
lbl_res.pack(pady=20)

# Ghi chú cho người dùng
tk.Label(root, text="(Dựa trên cây mẫu trong ảnh: 9 là gốc)", font=("Arial", 8, "italic")).pack()

root.mainloop()
