import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from datetime import datetime
import json
import os

TASK_FILE = "tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List with Calendar Deadline")
        self.root.geometry("480x600")
        self.tasks = []

        # === Task Entry ===
        tk.Label(root, text="Enter Task:").pack()
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=5)

        # === Calendar Date Picker ===
        tk.Label(root, text="Select Deadline Date:").pack()
        self.cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
        self.cal.pack(pady=5)

        # === Time Picker ===
        time_frame = tk.Frame(root)
        time_frame.pack(pady=5)
        tk.Label(time_frame, text="Time:").grid(row=0, column=0)

        self.hour_cb = ttk.Combobox(time_frame, values=[f"{i:02}" for i in range(24)], width=3)
        self.hour_cb.grid(row=0, column=1)
        self.hour_cb.set("12")

        tk.Label(time_frame, text=":").grid(row=0, column=2)

        self.min_cb = ttk.Combobox(time_frame, values=[f"{i:02}" for i in range(0, 60, 5)], width=3)
        self.min_cb.grid(row=0, column=3)
        self.min_cb.set("00")

        # === Add Task Button ===
        tk.Button(root, text="➕ Add Task", command=self.add_task, bg="lightblue").pack(pady=10)

        # === Task List Display ===
        self.task_listbox = tk.Listbox(root, width=60, height=15)
        self.task_listbox.pack(pady=10)

        # === Mark Done & Delete Buttons ===
        tk.Button(root, text="✔️ Mark as Done", command=self.mark_done, bg="lightgreen").pack(pady=5)
        tk.Button(root, text="🗑️ Delete Task", command=self.delete_task, bg="salmon").pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Input Error", "Task cannot be empty.")
            return

        # Combine selected date and time
        date = self.cal.get_date()
        hour = self.hour_cb.get()
        minute = self.min_cb.get()
        deadline = f"{date} {hour}:{minute}"

        # Validate deadline format
        try:
            datetime.strptime(deadline, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter a valid time.")
            return

        # Add task to list
        task_obj = {
            "task": task,
            "deadline": deadline,
            "done": False
        }
        self.tasks.append(task_obj)
        self.update_listbox()
        self.task_entry.delete(0, tk.END)
        self.save_tasks()

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("No Selection", "Select a task to mark as done.")
            return
        index = selected[0]
        self.tasks[index]["done"] = True
        self.update_listbox()
        self.save_tasks()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("No Selection", "Select a task to delete.")
            return
        index = selected[0]
        del self.tasks[index]
        self.update_listbox()
        self.save_tasks()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✔️" if task["done"] else "❌"
            display = f"{status} {task['task']} - Due: {task['deadline']}"
            self.task_listbox.insert(tk.END, display)

    def save_tasks(self):
        with open(TASK_FILE, "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r") as file:
                self.tasks = json.load(file)
            self.update_listbox()

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
