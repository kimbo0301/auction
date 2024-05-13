import tkinter as tk
from views.gui import setup_ui, get_user_input, display_results
from models.data_collector import collect_data
import asyncio

async def main(root):
    await root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    setup_ui(root)
    asyncio.run(main(root))