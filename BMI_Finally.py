import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector as mc

db = mc.connect(host="localhost", user="root", password="Aditya@2030", database="bmi_data")
cur = db.cursor(buffered=True)

# CLEAR BUTTON
def clear_fields():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    gender.delete(0, tk.END)
    entry_ht.delete(0, tk.END)
    entry_Wt.delete(0, tk.END)
    entry_Age.delete(0, tk.END)
    Goal.delete(0, tk.END)

# INSERTING ACCESSED DATA INTO DATABASE
def submit():
    try:
        # Get the height and weight from the entry widgets
        h = float(entry_ht.get())
        w = float(entry_Wt.get())

        # Check if height and weight are positive
        if h <= 0 or w <= 0:
            raise ValueError("Height and weight must be positive numbers.")

        # Calculate BMI
        calculated_bmi = round(w / (h ** 2), 2)

        # Insert the data along with the calculated BMI into the database
        cur.execute('INSERT INTO u_regi(username, password, gender, age, height, weight, goal, bmi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                    (entry_username.get(), entry_password.get(), gender.get(), entry_Age.get(), h, w, Goal.get(), calculated_bmi))
        db.commit()
        messagebox.showinfo("Success", "Registration successful!")
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

root = tk.Tk()
root.title("Login form")
root.geometry("400x700")

# Heading label
heading_lbl = tk.Label(root, text="NEW REGISTRATION", font=("georgia", 18))
heading_lbl.pack()

label_username = tk.Label(root, text="E-Mail ID  :", font=("georgia", 10))
label_username.place(x=50, y=100)
entry_username = tk.Entry(root, width=30)
entry_username.place(x=170, y=100)

# Create a label and entry for password
label_password = tk.Label(root, text="PASSWORD  :", font=("georgia", 10))
label_password.place(x=50, y=150)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.place(x=170, y=150)

# Gender
label_Gender = tk.Label(root, text="GENDER   :", font=("georgia", 10))
label_Gender.place(x=50, y=200)
gender = Combobox(root, width=27, values=['Male', 'Female', 'Other'])
gender.place(x=170, y=200)

# Age
label_Age = tk.Label(root, text="AGE  :", font=("georgia", 10))
label_Age.place(x=50, y=250)
entry_Age = tk.Entry(root, width=30)
entry_Age.place(x=170, y=250)

# Height
label_ht = tk.Label(root, text="HEIGHT(METER)  :", font=("georgia", 10))
label_ht.place(x=50, y=300)
entry_ht = tk.Entry(root, width=30)
entry_ht.place(x=170, y=300)

# Weight
label_Wt = tk.Label(root, text="WEIGHT(KG)  :", font=("georgia", 10))
label_Wt.place(x=50, y=350)
entry_Wt = tk.Entry(root, width=30)
entry_Wt.place(x=170, y=350)

# Health goals
label_Goal = tk.Label(root, text="HEALTH GOAL  :", font=("georgia", 10))
label_Goal.place(x=50, y=400)
Goal = Combobox(root, width=27, values=['Weight Loss', 'Weight Gain', 'Maintain'])
Goal.place(x=170, y=400)

# Submit button
submit_button = tk.Button(root, text="SUBMIT", font=("georgia", 10), command=submit, width=37)
submit_button.place(x=50, y=550)

# Create clear button
clear_button = tk.Button(root, text="CLEAR", font=("georgia", 10), command=clear_fields, width=16)
clear_button.place(x=50, y=500)

# EXIT BUTTON
EXT_button = tk.Button(root, text="EXIT", font=("georgia", 10), width=16, command=root.quit)
EXT_button.place(x=220, y=500)

# Login Form
def login_form():
    reg = tk.Tk()
    reg.title("Login Form")
    reg.geometry("400x300")
    heading_lbl = tk.Label(reg, text="Login Form", font=("georgia", 18))
    heading_lbl.pack()

    lbl_user = tk.Label(reg, text="USERNAME   :", font=("georgia", 10))
    lbl_user.place(x=50, y=100)
    entry_user = tk.Entry(reg, width=35)
    entry_user.place(x=150, y=100)

    # Create a label and entry for password
    label_pass = tk.Label(reg, text="PASSWORD   :", font=("georgia", 10))
    label_pass.place(x=50, y=150)
    entry_pass = tk.Entry(reg, show="*", width=35)
    entry_pass.place(x=150, y=150)

    def Login_Button():
        user = entry_user.get()
        pwd = entry_pass.get()
        cur.execute('SELECT * FROM u_regi WHERE username = %s AND password = %s', (user, pwd))
        avluser = cur.fetchone()
        if avluser:
            def home():
                hm = tk.Tk()
                hm.title("Home Page")
                hm.geometry("400x300")
                heading_lbl = tk.Label(hm, text="Home Page", font=("georgia", 18))
                heading_lbl.pack()
                text_widget = tk.Text(hm, width=40, height=10)
                text_widget.pack(padx=10, pady=10)

                try:
                    cur.execute('SELECT * FROM u_regi WHERE username = %s', (user,))
                    uinfo = cur.fetchone()
                    if uinfo:
                        text_widget.insert('end', f"Hello {uinfo[0]}\nYOUR DETAILS\nGender  : {uinfo[2]}\nAge     : {uinfo[3]} Yr.\nHeight  : {uinfo[4]} Meters\nWeight  : {uinfo[5]} Kg.\nGoal    : {uinfo[6]}\nBMI     : {uinfo[-1]}\n")
                    else:
                        text_widget.insert('end', "User not found\n")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

            messagebox.showinfo("Login Successful", f"Welcome, {user}")
            home()
        else:
            messagebox.showerror("Error", "Invalid username or password. Please register if you don't have an account.")

    # LOGIN BUTTON
    Login = tk.Button(reg, text="Click For Login", font=("georgia", 13), command=Login_Button)
    Login.place(x=200, y=200)

# Login button
btn_login = tk.Button(root, text="Login...?", font=("georgia", 15), command=login_form)
btn_login.place(x=250, y=600)

root.mainloop()
