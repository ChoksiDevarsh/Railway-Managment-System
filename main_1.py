import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

# Database setup
def create_db():
    conn = sqlite3.connect("train.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS USER (
        user_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        aadhar_no TEXT,
        mobile_no TEXT,
        email TEXT,
        password TEXT,
        address TEXT,
        city TEXT,
        state TEXT,
        pincode TEXT,
        age INTEGER,
        gender TEXT,
        security_ques TEXT,
        security_ans TEXT
    )''')
    conn.commit()
    conn.close()

# Add user
def add_user():
    conn = sqlite3.connect("train.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO USER 
    (first_name, last_name, aadhar_no, mobile_no, email, password, address, city, state, pincode, age, gender, security_ques, security_ans) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (first_name_entry.get(), last_name_entry.get(), aadhar_entry.get(), mobile_entry.get(),
                    email_entry.get(), password_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(),
                    pincode_entry.get(), age_entry.get(), gender_var.get(), security_ques_entry.get(), security_ans_entry.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "User added successfully!")
    clear_fields()
    view_users()

# View users
def view_users():
    conn = sqlite3.connect("train.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM USER")
    rows = cursor.fetchall()
    user_list.delete(0, END)
    for row in rows:
        user_list.insert(END, row)
    conn.close()

# Delete user
def delete_user():
    conn = sqlite3.connect("train.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM USER WHERE user_id = ?", (user_id_entry.get(),))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "User deleted successfully!")
    clear_fields()
    view_users()

# Update user
def update_user():
    conn = sqlite3.connect("train.db")
    cursor = conn.cursor()
    cursor.execute('''UPDATE USER SET 
    first_name = ?, last_name = ?, aadhar_no = ?, mobile_no = ?, email = ?, password = ?, 
    address = ?, city = ?, state = ?, pincode = ?, age = ?, gender = ?, 
    security_ques = ?, security_ans = ? WHERE user_id = ?''',
                   (first_name_entry.get(), last_name_entry.get(), aadhar_entry.get(), mobile_entry.get(),
                    email_entry.get(), password_entry.get(), address_entry.get(), city_entry.get(), state_entry.get(),
                    pincode_entry.get(), age_entry.get(), gender_var.get(), security_ques_entry.get(),
                    security_ans_entry.get(), user_id_entry.get()))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "User updated successfully!")
    clear_fields()
    view_users()

# Clear input fields
def clear_fields():
    user_id_entry.delete(0, END)
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    aadhar_entry.delete(0, END)
    mobile_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    address_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    pincode_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_var.set(None)
    security_ques_entry.delete(0, END)
    security_ans_entry.delete(0, END)

# UI setup
root = Tk()
root.title("User Management System")

main_frame = Frame(root)
main_frame.pack(pady=10)

form_frame = Frame(main_frame)
form_frame.grid(row=0, column=0, padx=10, pady=10)

Label(form_frame, text="User ID").grid(row=0, column=0, padx=5, pady=5)
user_id_entry = Entry(form_frame)
user_id_entry.grid(row=0, column=1, padx=5, pady=5)

Label(form_frame, text="First Name").grid(row=1, column=0, padx=5, pady=5)
first_name_entry = Entry(form_frame)
first_name_entry.grid(row=1, column=1, padx=5, pady=5)

Label(form_frame, text="Last Name").grid(row=2, column=0, padx=5, pady=5)
last_name_entry = Entry(form_frame)
last_name_entry.grid(row=2, column=1, padx=5, pady=5)

Label(form_frame, text="Aadhar No").grid(row=3, column=0, padx=5, pady=5)
aadhar_entry = Entry(form_frame)
aadhar_entry.grid(row=3, column=1, padx=5, pady=5)

Label(form_frame, text="Mobile No").grid(row=4, column=0, padx=5, pady=5)
mobile_entry = Entry(form_frame)
mobile_entry.grid(row=4, column=1, padx=5, pady=5)

Label(form_frame, text="Email").grid(row=5, column=0, padx=5, pady=5)
email_entry = Entry(form_frame)
email_entry.grid(row=5, column=1, padx=5, pady=5)

Label(form_frame, text="Password").grid(row=6, column=0, padx=5, pady=5)
password_entry = Entry(form_frame, show='*')
password_entry.grid(row=6, column=1, padx=5, pady=5)

Label(form_frame, text="Address").grid(row=7, column=0, padx=5, pady=5)
address_entry = Entry(form_frame)
address_entry.grid(row=7, column=1, padx=5, pady=5)

Label(form_frame, text="City").grid(row=8, column=0, padx=5, pady=5)
city_entry = Entry(form_frame)
city_entry.grid(row=8, column=1, padx=5, pady=5)

Label(form_frame, text="State").grid(row=9, column=0, padx=5, pady=5)
state_entry = Entry(form_frame)
state_entry.grid(row=9, column=1, padx=5, pady=5)

Label(form_frame, text="Pincode").grid(row=10, column=0, padx=5, pady=5)
pincode_entry = Entry(form_frame)
pincode_entry.grid(row=10, column=1, padx=5, pady=5)

Label(form_frame, text="Age").grid(row=11, column=0, padx=5, pady=5)
age_entry = Entry(form_frame)
age_entry.grid(row=11, column=1, padx=5, pady=5)

# Gender with radio buttons
Label(form_frame, text="Gender").grid(row=12, column=0, padx=5, pady=5)
gender_var = StringVar()
gender_male = ttk.Radiobutton(form_frame, text="Male", variable=gender_var, value="Male")
gender_female = ttk.Radiobutton(form_frame, text="Female", variable=gender_var, value="Female")
gender_male.grid(row=12, column=1, padx=5, pady=5, sticky=W)
gender_female.grid(row=12, column=1, padx=70, pady=5)

Label(form_frame, text="Security Question").grid(row=13, column=0, padx=5, pady=5)
security_ques_entry = Entry(form_frame)
security_ques_entry.grid(row=13, column=1, padx=5, pady=5)

Label(form_frame, text="Security Answer").grid(row=14, column=0, padx=5, pady=5)
security_ans_entry = Entry(form_frame)
security_ans_entry.grid(row=14, column=1, padx=5, pady=5)

# Buttons for CRUD operations
button_frame = Frame(main_frame)
button_frame.grid(row=1, column=0, pady=10)

Button(button_frame, text="Add User", command=add_user).grid(row=0, column=0, padx=10)
Button(button_frame, text="View Users", command=view_users).grid(row=0, column=1, padx=10)
Button(button_frame, text="Update User", command=update_user).grid(row=0, column=2, padx=10)
Button(button_frame, text="Delete User", command=delete_user).grid(row=0, column=3, padx=10)
Button(button_frame, text="Clear Fields", command=clear_fields).grid(row=0, column=4, padx=10)

# Listbox to display users with scrollbar
list_frame = Frame(main_frame)
list_frame.grid(row=2, column=0, pady=10)

user_list = Listbox(list_frame, height=10, width=80)
user_list.pack(side=LEFT)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)
user_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=user_list.yview)

# Create the database
create_db()

# Start the application
root.mainloop()
