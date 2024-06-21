import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        self.task_entry = tk.Entry(master, font=("Arial", 14), width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_listbox = tk.Listbox(master, font=("Arial", 12), width=40, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, font=("Arial", 12), bg="#f44336", fg="white")
        self.delete_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_tasks, font=("Arial", 12), bg="#ff9800", fg="white")
        self.clear_button.grid(row=2, column=1, padx=5, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks.pop(index)
            self.update_task_list()
        except IndexError:
            messagebox.showerror("Error", "No task selected.")

    def clear_tasks(self):
        self.tasks.clear()
        self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
