import tkinter as tk
from tkinter import messagebox

def search_product():
    product_name = entry.get()
    if not product_name.strip():
        messagebox.showinfo("입력 오류", "제품명을 입력해주세요.")
        return
    # 데이터 수집 모듈을 트리거하는 코드 필요
    # 예: collected_data = collect_data(product_name)
    # 결과 표시: result_text.insert(tk.END, collected_data)
    
    # 테스트용 임시 결과 표시
    result_text.insert(tk.END, f"검색된 제품: {product_name}\n")

def setup_ui(window):
    global entry, result_text
    window.title("중고 명품 매입 결정 시스템")
    
    tk.Label(window, text="제품명 입력:").pack()
    
    entry = tk.Entry(window)
    entry.pack()
    
    search_button = tk.Button(window, text="검색", command=search_product)
    search_button.pack()
    
    result_text = tk.Text(window, height=10, width=50)
    result_text.pack()

if __name__ == "__main__":
    root = tk.Tk()
    setup_ui(root)
    root.mainloop()