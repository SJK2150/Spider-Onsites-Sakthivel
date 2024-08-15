
import tkinter as tk
from tkinter import filedialog, messagebox
from text_extraction import extract_text_from_file

def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("All Files", "*.*"), ("PDF Files", "*.pdf"), ("Image Files", "*.png;*.jpg;*.jpeg"), ("Excel Files", "*.xls;*.xlsx"), ("Text Files", "*.txt")]
    )
    if file_path:
        try:
            text = extract_text_from_file(file_path)
            text_result.delete("1.0", tk.END)
            text_result.insert(tk.END, text)
        except Exception as e:
            messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Document Text Extractor")


browse_button = tk.Button(root, text="Browse File", command=browse_file)
browse_button.pack(pady=10)

text_result = tk.Text(root, height=20, width=80)
text_result.pack(pady=10)


root.mainloop()
