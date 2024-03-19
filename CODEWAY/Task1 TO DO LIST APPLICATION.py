import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.geometry("400x300")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add Task", width=10, height=2, command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.tasks_frame = tk.Frame(master)
        self.tasks_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.view_button = tk.Button(master, text="View Tasks", width=10, height=2, command=self.view_tasks)
        self.view_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(master, text="Delete Task", width=10, height=2, command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def view_tasks(self):
        view_window = tk.Toplevel(self.master)
        view_window.title("View Tasks")
        view_window.geometry("300x200")
        task_listbox = tk.Listbox(view_window)
        for task in self.tasks:
            task_listbox.insert(tk.END, task)
        task_listbox.pack(padx=10, pady=10)

    def delete_task(self):
        if self.tasks:
            delete_window = tk.Toplevel(self.master)
            delete_window.title("Delete Task")
            delete_window.geometry("300x200")
            delete_label = tk.Label(delete_window, text="Select task to delete:")
            delete_label.pack(padx=10, pady=10)
            task_listbox = tk.Listbox(delete_window)
            for task in self.tasks:
                task_listbox.insert(tk.END, task)
            task_listbox.pack(padx=10, pady=10)
            delete_button = tk.Button(delete_window, text="Delete", width=10, height=2,
                                      command=lambda: self.remove_task(task_listbox))
            delete_button.pack(padx=10, pady=10)
        else:
            messagebox.showinfo("Info", "No tasks to delete.")

    def remove_task(self, listbox):
        selected_task = listbox.curselection()
        if selected_task:
            index = selected_task[0]
            del self.tasks[index]
            listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
