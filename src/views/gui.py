import tkinter as tk
from tkinter import messagebox

def get_user_input(window):
    return window.entry.get()

def setup_ui(window):
    window.title("중고 명품 매입 결정 시스템")
    tk.Label(window, text="제품명 입력:").pack()
    window.entry = tk.Entry(window)
    window.entry.pack()
    search_button = tk.Button(window, text="검색", command=lambda: display_results(window))
    search_button.pack()
    window.result_text = tk.Text(window, height=10, width=50)
    window.result_text.pack()

def display_results(window):
    product_name = get_user_input(window)
    if not product_name.strip():
        messagebox.showinfo("입력 오류", "제품명을 입력해주세요.")
        return
    # 이 부분에서 data_collector의 함수를 비동기적으로 호출하여 결과를 받아와야 함
    window.result_text.insert(tk.END, f"검색된 제품: {product_name}\n")