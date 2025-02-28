import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # type: ignore
import subprocess

def open_add_ns_ui():
    root.destroy()
    subprocess.run(["python", "add_ns_ui.py"])
   

def open_add_qltd_ui():
    root.destroy()
    subprocess.run(["python", "add_qltd_ui.py"])
    
def open_add_qlpc_ui():
    root.destroy()
    subprocess.run(["python", "add_qlpc_ui.py"])
    

def open_add_ccvlt_ui():
    root.destroy()
    subprocess.run(["python", "add_ccvlt_ui.py"])
   

def open_add_qlhd_ui():
    root.destroy()
    subprocess.run(["python", "add_qlhd_ui.py"])
   



root = tk.Tk()
root.title("CHỨC NĂNG DÀNH CHO QTV")
root.geometry("600x400")
root.resizable(False, False)

# Load image
img = Image.open("IMG/question.png")
img = img.resize((100, 100))
photo = ImageTk.PhotoImage(img)

# Image Label
img_label = tk.Label(root, image=photo)
img_label.pack(pady=10)

# Title
title_label = tk.Label(root, text="BẠN MUỐN QUẢN LÝ ĐIỀU GÌ?", font=("Arial", 14, "bold"), fg="red")
title_label.pack(pady=5)

# Buttons
buttons = [
    ("📂 QUẢN LÝ HỒ SƠ NHÂN SỰ", open_add_ns_ui),
    ("📝 QUẢN LÝ HỢP ĐỒNG LAO ĐỘNG", open_add_qlhd_ui),
    ("📊 QUẢN LÝ CHẤM CÔNG VÀ LƯƠNG THƯỞNG", open_add_ccvlt_ui),
    ("📋 QUẢN LÝ PHÂN CÔNG", open_add_qlpc_ui),
    ("👨‍💼 QUẢN LÝ TUYỂN DỤNG", open_add_qltd_ui)
]

for text, cmd in buttons:
    tk.Button(root, text=text, font=("Arial", 10, "bold"), command=cmd, width=40).pack(pady=5)

root.mainloop()