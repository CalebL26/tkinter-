import tkinter as tk 

def login():
    username = username_entry.get()
    password = password_entry.get()
    print("Username:", username)
    print("Password:", password)

root = tk.Tk()
root.title("Login Page")
root.geometry("300x150")

username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")

username_label.place(x=30, y=30)
password_label.place(x=30, y=60)

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

username_entry.place(x=120, y=30)
password_entry.place(x=120, y=60)

login_button = tk.Button(root, text="Login", command=login)
login_button.place(x=130, y=100)

root.mainloop()