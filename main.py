import tkinter as tk
from tkinter import messagebox 
import random
import string
import sqlite3

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")
        return
    
    use_special = special_var.get()
    
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Function to save password 
def save_password():
    password = password_var.get()
    if not password:
        messagebox.showerror("Error", "No password generated!")
        return
    
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY AUTOINCREMENT, password TEXT)")
    cursor.execute("INSERT INTO passwords(password) VALUES(?)", (password,))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Password saved successfully!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "8")

special_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=1, columnspan=2)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, state="readonly", width=30).grid(row=2, columnspan=2)

tk.Button(root, text="Generate", command=generate_password).grid(row=3, column=0)
tk.Button(root, text="Save", command=save_password).grid(row=3, column=1)

root.mainloop()
