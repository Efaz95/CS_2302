import tkinter as tk
from tkinter import ttk
import pymysql

root = tk.Tk()
tree = ttk.Treeview(root)
tree.pack()

db = pymysql.connect("localhost", "root", "123", "university")
cursor = db.cursor()

def student_department():
	tree.delete(*tree.get_children())

	tree["columns"] = ("Name", "DOB", "Department_name")
	tree.column("#0", width=100)
	tree.column("Name", width=100)
	tree.column("DOB", width=100)
	tree.column("Department_name", width=150)

	tree.heading("#0", text="Panther ID")
	tree.heading("Name", text="Name")
	tree.heading("DOB", text="Birth year")
	tree.heading("Department_name", text="Department name")

	sql ='''select Student.Panther_ID, Student.Name, Student.DOB, Department.Name
			from Student, Department
			where Student.Department_ID = Department.Department_ID'''

	cursor.execute(sql)
	result = cursor.fetchall()

	for i in range(0, len(result)):
		tree.insert("", i, text=str(result[i][0]), values=(str(result[i][1]), str(result[i][2]), str(result[i][3])))


def instructor_info():
	tree.delete(*tree.get_children())

	tree["columns"] = ("Name", "Department_ID")
	tree.column("#0", width=100)
	tree.column("Name", width=100)
	tree.column("Department_ID", width=100)

	tree.heading("#0", text="Instructor ID")
	tree.heading("Name", text="Name")
	tree.heading("Department_ID", text="Department ID")

	sql = "select * from Instructor"
	cursor.execute(sql)
	result = cursor.fetchall()

	for i in range(0, len(result)):
		tree.insert("", i, text=str(result[i][0]), values=(str(result[i][1]), str(result[i][2])))	


def student_info():
	tree.delete(*tree.get_children())

	tree["columns"] = ("Name", "DOB")
	tree.column("#0", width=100)
	tree.column("Name", width=100)
	tree.column("DOB", width=100)

	tree.heading("#0", text="Panther ID")
	tree.heading("Name", text="Name")
	tree.heading("DOB", text="Birth year")


	sql = "select * from Student"

	cursor.execute(sql)
	result = cursor.fetchall()

	for i in range(0, len(result)):
		tree.insert("", i, text=str(result[i][0]), values=(str(result[i][1]), str(result[i][2])))



btn1 = tk.Button(root, text="Student-Department", command=student_department).pack()
btn2 = tk.Button(root, text="Instructor_info", command=instructor_info).pack()
btn3 = tk.Button(root, text="Student_info", command=student_info).pack()

student_info()

root.mainloop()