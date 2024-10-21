import tkinter as tk
from tkinter import messagebox

# creating a add task method for adding the task in todo list
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# creating delete method for delete the added task from the todo list
def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to clear all tasks
def clear_all():
    listbox.delete(0, tk.END)

#creating the GUI window
window = tk.Tk()
window.title("To-Do List")

frame = tk.Frame(window)
frame.pack(pady=10)

listbox = tk.Listbox(frame, height=8, width=50, font=("Helvetica", 12))
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(window, font=("Helvetica", 12), width=40)
entry.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all)
clear_button.pack(side=tk.LEFT, padx=10)

window.mainloop()
