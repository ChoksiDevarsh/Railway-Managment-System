import pyodbc
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def connection():
    return pyodbc.connect("Driver={SQL Server};"
                          "Server=DEVARSHC5502\SQLEXPRESS;"
                          "Database=PROJECT_DBMS_1;"
                          "Trusted_Connection=yes;")

def fetch_data():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("EXEC FetchAllTrains")
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_data_into_treeview():
    rows = fetch_data()
    for row in rows:
        tree.insert("", "end", values=row)

def insert():
    T_ID = T_IDEntry.get()
    T_NAME = TrainNameEntry.get()
    P_NAME = PassengerNameEntry.get()
    P_ID = PassengerIDEntry.get()
    STATION = StationEntry.get()

    if not all([T_ID, T_NAME, P_NAME, P_ID, STATION]):
        messagebox.showinfo("Insert Status", "All Fields are required")
        return

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("EXEC InsertTrain ?, ?, ?, ?, ?", (T_ID, T_NAME, P_NAME, P_ID, STATION))
    conn.commit()
    conn.close()

    for entry in [T_IDEntry, TrainNameEntry, PassengerNameEntry, PassengerIDEntry, StationEntry]:
        entry.delete(0, END)

    messagebox.showinfo("Insert Status", "Inserted Successfully")
    for item in tree.get_children():
        tree.delete(item)
    insert_data_into_treeview()

def delete():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showinfo("Delete Status", "Select a record to delete")
        return

    T_ID = tree.item(selected_item)['values'][0]
    
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("EXEC DeleteTrain ?", (T_ID,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Delete Status", "Deleted Successfully")
    tree.delete(selected_item)

def update():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showinfo("Update Status", "Select a record to update")
        return

    T_ID = tree.item(selected_item)['values'][0]

    new_T_NAME = TrainNameEntry.get()
    new_P_NAME = PassengerNameEntry.get()
    new_P_ID = PassengerIDEntry.get()
    new_STATION = StationEntry.get()

    if not all([new_T_NAME, new_P_NAME, new_P_ID, new_STATION]):
        messagebox.showinfo("Update Status", "All Fields are required")
        return

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("EXEC UpdateTrain ?, ?, ?, ?, ?", (T_ID, new_T_NAME, new_P_NAME, new_P_ID, new_STATION))
    conn.commit()
    conn.close()

    for entry in [T_IDEntry, TrainNameEntry, PassengerNameEntry, PassengerIDEntry, StationEntry]:
        entry.delete(0, END)

    messagebox.showinfo("Update Status", "Updated Successfully")
    for item in tree.get_children():
        tree.delete(item)
    insert_data_into_treeview()

def search():
    T_ID = T_IDEntry.get()
    T_NAME = TrainNameEntry.get()
    P_NAME = PassengerNameEntry.get()
    P_ID = PassengerIDEntry.get()
    STATION = StationEntry.get()

    conn = connection()
    cursor = conn.cursor()
    query = "SELECT * FROM train3 WHERE T_ID = ? OR TrainName = ? OR PassengerName = ? OR PassengerID = ? OR Station = ?"
    cursor.execute(query, (T_ID, T_NAME, P_NAME, P_ID, STATION))
    rows = cursor.fetchall()
    conn.close()

    for item in tree.get_children():
        tree.delete(item)
    
    for row in rows:
        tree.insert("", "end", values=row)

def on_tree_select(event):
    selected_item = tree.selection()
    if selected_item:
        values = tree.item(selected_item)['values']
        T_IDEntry.delete(0, END)
        TrainNameEntry.delete(0, END)
        PassengerNameEntry.delete(0, END)
        PassengerIDEntry.delete(0, END)
        StationEntry.delete(0, END)
        
        T_IDEntry.insert(0, values[0])
        TrainNameEntry.insert(0, values[1])
        PassengerNameEntry.insert(0, values[2])
        PassengerIDEntry.insert(0, values[3])
        StationEntry.insert(0, values[4])

def login():
    username = username_entry.get()
    password = password_entry.get()

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("EXEC CheckUserCredentials ?, ?", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result and result[0] == 1:
        login_frame.pack_forget()
        main_frame.pack(fill=BOTH, expand=True)
        insert_data_into_treeview()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = Tk()
root.title("Railway Management System")
root.geometry("1080x720")

login_frame = Frame(root)
login_frame.pack(fill=BOTH, expand=True)

main_frame = Frame(root)

Label(login_frame, text="Login", font=('Arial Bold', 30)).pack(pady=20)
Label(login_frame, text="Username", font=('Arial', 15)).pack(pady=10)
username_entry = Entry(login_frame, width=25, bd=5, font=('Arial', 15))
username_entry.pack(pady=5)
Label(login_frame, text="Password", font=('Arial', 15)).pack(pady=10)
password_entry = Entry(login_frame, width=25, bd=5, font=('Arial', 15), show="*")
password_entry.pack(pady=5)
Button(login_frame, text="Login", padx=20, pady=10, font=('Arial', 15), bg="#84F894", command=login).pack(pady=20)

label = Label(main_frame, text="Railway Management (CRUD MATRIX)", font=('Arial Bold', 30))
label.pack(pady=20)

frame = Frame(main_frame)
frame.pack(pady=10)

T_IDLabel = Label(frame, text="Train ID", font=('Arial', 15))
TrainNameLabel = Label(frame, text="Train Name", font=('Arial', 15))
PassengerNameLabel = Label(frame, text="Passenger Name", font=('Arial', 15))
PassengerIDLabel = Label(frame, text="Passenger Seat No", font=('Arial', 15))
StationLabel = Label(frame, text="Station", font=('Arial', 15))

T_IDLabel.grid(row=0, column=0, padx=10, pady=5)
TrainNameLabel.grid(row=1, column=0, padx=10, pady=5)
PassengerNameLabel.grid(row=2, column=0, padx=10, pady=5)
PassengerIDLabel.grid(row=3, column=0, padx=10, pady=5)
StationLabel.grid(row=4, column=0, padx=10, pady=5)

T_IDEntry = Entry(frame, width=25, bd=5, font=('Arial', 15))
TrainNameEntry = Entry(frame, width=25, bd=5, font=('Arial', 15))
PassengerNameEntry = Entry(frame, width=25, bd=5, font=('Arial', 15))
PassengerIDEntry = Entry(frame, width=25, bd=5, font=('Arial', 15))
StationEntry = Entry(frame, width=25, bd=5, font=('Arial', 15))

T_IDEntry.grid(row=0, column=1, padx=10, pady=5)
TrainNameEntry.grid(row=1, column=1, padx=10, pady=5)
PassengerNameEntry.grid(row=2, column=1, padx=10, pady=5)
PassengerIDEntry.grid(row=3, column=1, padx=10, pady=5)
StationEntry.grid(row=4, column=1, padx=10, pady=5)

button_frame = Frame(main_frame)
button_frame.pack(pady=20)

addBtn = Button(button_frame, text="Add", padx=20, pady=10, width=10, font=('Arial', 15), bg="#84F894", command=insert)
deleteBtn = Button(button_frame, text="Delete", padx=20, pady=10, width=10, font=('Arial', 15), bg="#FF9999", command=delete)
updateBtn = Button(button_frame, text="Update", padx=20, pady=10, width=10, font=('Arial', 15), bg="#ADD8E6", command=update)
searchBtn = Button(button_frame, text="Search", padx=20, pady=10, width=10, font=('Arial', 15), bg="#F4FE82", command=search)

addBtn.grid(row=0, column=0, padx=20)
deleteBtn.grid(row=0, column=1, padx=20)
updateBtn.grid(row=0, column=2, padx=20)
searchBtn.grid(row=0, column=3, padx=20)

tree_frame = Frame(main_frame)
tree_frame.pack(pady=20)

tree = ttk.Treeview(tree_frame, columns=("T_ID", "TrainName", "PassengerName", "PassengerID", "Station"), show="headings", height="8")
tree.column("T_ID", anchor=CENTER, width=100)
tree.column("TrainName", anchor=CENTER, width=200)
tree.column("PassengerName", anchor=CENTER, width=200)
tree.column("PassengerID", anchor=CENTER, width=150)
tree.column("Station", anchor=CENTER, width=200)

tree.heading("T_ID", text="Train ID", anchor=CENTER)
tree.heading("TrainName", text="Train Name", anchor=CENTER)
tree.heading("PassengerName", text="Passenger Name", anchor=CENTER)
tree.heading("PassengerID", text="Passenger Seat No", anchor=CENTER)
tree.heading("Station", text="Station", anchor=CENTER)

tree.pack()
tree.bind("<<TreeviewSelect>>", on_tree_select)

root.mainloop()
