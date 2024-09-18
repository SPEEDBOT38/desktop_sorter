import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog
import time

def sort_files(directory):
    if not os.path.exists(directory):
        status_label.config(text="❌ Directory does not exist!", foreground="red")
        return

    files = os.listdir(directory)
    total_files = len(files)
    
    for idx, filename in enumerate(files):
        time.sleep(0.1) 
        progress_bar['value'] = (idx + 1) / total_files * 100
        root.update_idletasks()

        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            ext_dir = os.path.join(directory, ext)
            os.makedirs(ext_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(ext_dir, filename))
    
    status_label.config(text="🎉 Sorting completed!", foreground="green")

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

root = tk.Tk()
root.title("📂 File Sorter")
root.geometry("500x200")
root.configure(bg='#f0f8ff')

directory_entry = ttk.Entry(root, width=40)
directory_entry.grid(row=0, column=0, padx=10, pady=10)
ttk.Button(root, text="🔍 Browse", command=browse_directory).grid(row=0, column=1, padx=10)

ttk.Button(root, text="🚀 Sort Files", command=lambda: sort_files(directory_entry.get())).grid(row=1, column=0, columnspan=2, pady=10)

progress_bar = ttk.Progressbar(root, length=400, mode='determinate')
progress_bar.grid(row=2, column=0, columnspan=2, pady=10)

status_label = ttk.Label(root, text="🔄 Status: Waiting for action...", foreground="blue", background="#f0f8ff")
status_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
