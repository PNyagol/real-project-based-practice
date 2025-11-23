import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("My To-Do List")
        self.window.geometry("400x500")
        
        self.task_list = []
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.window, text="My To-Do List", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.window)
        input_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(input_frame, width=30, font=("Arial", 12))
        self.task_entry.pack(side=tk.LEFT, padx=5)
        
        add_button = tk.Button(input_frame, text="Add Task", 
                              command=self.add_item, bg="lightgreen")
        add_button.pack(side=tk.LEFT, padx=5)
    
    def add_item(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_list.append({"task": task, "done": False})
            self.task_entry.delete(0, tk.END)
            self.update_display()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def update_display(self):
        print("Tasks:", self.task_list)
    
    def run(self):
        self.window.mainloop()

# Create and run the app
if __name__ == "__main__":
    app = TodoApp()
    app.run()