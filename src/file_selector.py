# Resume Helper
# file_selector.py

# Import statements
import tkinter as tk
from tkinter import filedialog

# Function allows user to select desired resume file from file explorer
def select_file():
    # print("select_file function")
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select file",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
    )
    if file_path:
        pass

    return file_path