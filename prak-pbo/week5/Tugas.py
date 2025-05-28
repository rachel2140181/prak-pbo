import tkinter as tk
from tkinter import messagebox

users = {}

def logout():
    messagebox.showinfo("Logout", "You have been logged out.")
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

def open_register_window():
    register_window = tk.Toplevel(window)
    register_window.title("Register")

    tk.Label(register_window, text="Username:").grid(row=0, column=0)
    tk.Label(register_window, text="Password:").grid(row=1, column=0)
    tk.Label(register_window, text="Confirm Password:").grid(row=2, column=0)

    entry_username = tk.Entry(register_window)
    entry_password = tk.Entry(register_window, show="*")
    entry_confirm = tk.Entry(register_window, show="*")

    entry_username.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)
    entry_confirm.grid(row=2, column=1)

    def toggle_password():
        if show_var.get():
            entry_password.config(show="")
            entry_confirm.config(show="")
        else:
            entry_password.config(show="*")
            entry_confirm.config(show="*")

    show_var = tk.BooleanVar()
    tk.Checkbutton(register_window, text="Show Password", variable=show_var, command=toggle_password).grid(row=3, column=1)

    def register():
        username = entry_username.get()
        password = entry_password.get()
        confirm = entry_confirm.get()

        if not username or not password:
            messagebox.showerror("Error", "Username dan password tidak boleh kosong.")
        elif password != confirm:
            messagebox.showerror("Error", "Password tidak sama!")
        elif username in users:
            messagebox.showerror("Error", "Username sudah terdaftar!")
        else:
            users[username] = password
            messagebox.showinfo("Registration Successful", "You have successfully registered.")
            register_window.destroy()

    tk.Button(register_window, text="Register", command=register).grid(row=4, column=0, columnspan=2, pady=10)

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        logout_btn.config(state=tk.NORMAL)
    else:
        messagebox.showerror("Login Failed", "Username atau password salah.")

def toggle_password_login():
    if show_password_var.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

window = tk.Tk()
window.title("Login")

tk.Label(window, text="Username:").grid(row=0, column=0)
tk.Label(window, text="Password:").grid(row=1, column=0)

entry_username = tk.Entry(window)
entry_password = tk.Entry(window, show="*")

entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

show_password_var = tk.BooleanVar()
tk.Checkbutton(window, text="Show Password", variable=show_password_var, command=toggle_password_login).grid(row=2, column=1, sticky="w")

tk.Button(window, text="Login", width=10, command=login).grid(row=3, column=0, pady=10)
tk.Button(window, text="Register", width=10, command=open_register_window).grid(row=3, column=1)

logout_btn = tk.Button(window, text="Logout", width=22, command=logout, state=tk.DISABLED)
logout_btn.grid(row=4, column=0, columnspan=2)

window.mainloop()