from tkinter import *
from tkinter import messagebox

# Registration window
def sign_up():
    username = entry1.get()
    password = entry2.get()

    if username and password:  # Check if both fields are non-empty
        file_path = "users.txt"
        with open(file_path, "a") as file:
            file.write(f"{username}:{password}\n")
        messagebox.showinfo("Success", "Registration Successful")
        registration_window.withdraw()  # Close the registration window
        login_window.deiconify()  # Show the login window

    else:
        messagebox.showerror("Error", "Both fields are required")


# Login window
def login():
    username = entry1_login.get()
    password = entry2_login.get()

    file_path = "users.txt"
    with open(file_path, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(":")
            if username == stored_username and password == stored_password:
                messagebox.showinfo("Success", "Login Successful")
                login_window.withdraw()  # Close the login window
                registration_window.deiconify()  # Show the registration window
                return

    messagebox.showerror("Error", "Incorrect username or password")        

#Registration Window

registration_window = Tk()
registration_window.title("Create Account")
registration_window.geometry("300x200")

Label(registration_window, text="Username").place(x=20, y=20)
Label(registration_window, text="Password").place(x=20, y=70)

entry1 = Entry(registration_window, bd=5)
entry1.place(x=140, y=20)

entry2 = Entry(registration_window, bd=5)
entry2.place(x=140, y=70)

Button(registration_window, text="Sign Up", command=sign_up, height=3, width=13, bd=6).place(x=100, y=120)


#Login Window

login_window = Tk()
login_window.title("Login")
login_window.geometry("300x200")

Label(login_window, text="Username").place(x=20, y=20)
Label(login_window, text="Password").place(x=20, y=70)

entry1_login = Entry(login_window, bd=5)
entry1_login.place(x=140, y=20)

entry2_login = Entry(login_window, bd=5)
entry2_login.place(x=140, y=70)

Button(login_window, text="Login", command=login, height=3, width=13, bd=6).place(x=100, y=120)

# Start with the registration window
login_window.withdraw()
registration_window.mainloop()
