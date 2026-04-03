import tkinter as tk
import time

# 1. ĐỊNH NGHĨA NODE VÀ DANH SÁCH LIÊN KẾT
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

# 2. HÀM XỬ LÝ LOGIC ĐỆ QUY ĐỂ XÓA NGƯỢC
def xoa_nguoc_de_quy(node, log_func):
    if node is None:
        return None
    
    # Đệ quy đi sâu vào node tiếp theo trước
    node.next = xoa_nguoc_de_quy(node.next, log_func)
    
    # Sau khi đã quay lại từ node cuối, thực hiện xóa node hiện tại
    log_func(f"Xoa node [{node.data}]")
    del node # Giải phóng node
    return None

# 3. GIAO DIỆN ĐỒ HỌA
def chay_chuong_trinh():
    # Lấy dữ liệu nhập vào
    input_str = entry_list.get()
    try:
        numbers = [int(x) for x in input_str.split() if x != '0']
        
        # Tạo danh sách
        llist = LinkedList()
        display_list = ""
        for n in numbers:
            llist.add(n)
            display_list += f"[{n}]"
            
        txt_console.config(state='normal')
        txt_console.delete('1.0', tk.END)
        txt_console.insert(tk.END, f"List goc: {display_list}\n")
        
        # Hàm hỗ trợ in log ra màn hình đồ họa
        def log(msg):
            txt_console.insert(tk.END, msg + "\n")
            txt_console.see(tk.END)
            root.update() # Cập nhật giao diện ngay lập tức để thấy hiệu ứng
            time.sleep(0.5) # Tạm dừng một chút để dễ quan sát

        # Thực hiện xóa ngược
        llist.head = xoa_nguoc_de_quy(llist.head, log)
        txt_console.config(state='disabled')
        
    except ValueError:
        label_info.config(text="Lỗi: Vui lòng nhập các số nguyên cách nhau bằng khoảng trắng!")

root = tk.Tk()
root.title("Bài 205 - Xóa ngược Danh sách liên kết")
root.geometry("500x400")

tk.Label(root, text="Nhập các số (nhập 0 để dừng):", font=("Arial", 10)).pack(pady=5)
entry_list = tk.Entry(root, width=40, justify='center')
entry_list.insert(0, "1 2 3 0")
entry_list.pack(pady=5)

tk.Button(root, text="Bắt đầu xóa ngược", command=chay_chuong_trinh, bg="red", fg="white").pack(pady=10)

txt_console = tk.Text(root, height=12, width=50, bg="#222", fg="#00FF00", font=("Courier", 11))
txt_console.pack(pady=10)
txt_console.insert(tk.END, "Kết quả sẽ hiển thị tại đây...")

label_info = tk.Label(root, text="", fg="red")
label_info.pack()

root.mainloop()
