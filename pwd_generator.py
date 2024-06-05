import tkinter as tk
from tkinter import messagebox
import secrets
import string

# Function to generate the random password
def generate_password():
    length = password_length.get()
    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number for password length.")
        return
    
    length = int(length)
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first!")

# Setting up the main application window
root = tk.Tk()
root.title("Random Password Generator")

# Creating widgets
tk.Label(root, text="Password Length:").pack(pady=5)
password_length = tk.Entry(root)
password_length.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Running the application
root.mainloop()