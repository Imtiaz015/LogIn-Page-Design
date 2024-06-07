import tkinter as tk
from tkinter import ttk, messagebox

# Initialize the main window
root = tk.Tk()
root.minsize(350, 550)
root.resizable(0, 0)
root.title("Calculator")
root.configure(bg="black")

# Configure styles
style = ttk.Style()
style.configure("Custom.TLabel", background="black", foreground="Fuchsia", font=("Book Antiqua", 25, 'bold'))

# Create a Label with the custom style
label = ttk.Label(root, text="Calculator", style="Custom.TLabel")
label.pack(pady=(50, 10))

# Create a frame for the entry widgets
frame1 = tk.Frame(root, bg="black")
frame1.pack(pady=10)

num1 = tk.Entry(frame1, font=("Lucida Fax", 15), highlightthickness=2, bg='black', fg='cyan', highlightcolor='white', justify='center', insertbackground="white")
num1.pack(side=tk.LEFT, padx=10)

num2 = tk.Entry(frame1, font=("Lucida Fax", 15), highlightthickness=2, bg='black', fg='cyan', highlightcolor='white', justify='center', insertbackground="white")
num2.pack(side=tk.LEFT, padx=10)

result = ttk.Label(root, text='', font=('times new roman', 15, 'bold'), background="black", foreground="Fuchsia")
result.pack(pady=20)

# Define the placeholder functionality
def add_placeholder(entry, placeholder):
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg='cyan', show='')

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(fg='white', show='')

    entry.insert(0, placeholder)
    entry.config(fg='white')
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Add placeholders
add_placeholder(num1, "1st Number")
add_placeholder(num2, "2nd Number")

# Define the operations
def add():
    try:
        a = float(num1.get())
        b = float(num2.get())
        res = a + b
        result.config(text=f"Result: {res}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def sub():
    try:
        a = float(num1.get())
        b = float(num2.get())
        res = a - b
        result.config(text=f"Result: {res}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def mul():
    try:
        a = float(num1.get())
        b = float(num2.get())
        res = a * b
        result.config(text=f"Result: {res}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

def div():
    try:
        a = float(num1.get())
        b = float(num2.get())
        res = a / b
        result.config(text=f"Result: {res}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

def mod():
    try:
        a = float(num1.get())
        b = float(num2.get())
        res = a % b
        result.config(text=f"Result: {res}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

# Create buttons for operations
plusbutton = tk.Button(root, text="+", font=("Book Antiqua", 15, 'bold'), bg='black', fg='Fuchsia', command=add)
plusbutton.pack(pady=10)

minusbutton = tk.Button(root, text="-", font=("Book Antiqua", 15, 'bold'), bg='black', fg='Fuchsia', command=sub)
minusbutton.pack(pady=10)

multiplicationbutton = tk.Button(root, text="x", font=("Book Antiqua", 15, 'bold'), bg='black', fg='Fuchsia', command=mul)
multiplicationbutton.pack(pady=10)

divisionbutton = tk.Button(root, text="/", font=("Book Antiqua", 15, 'bold'), bg='black', fg='Fuchsia', command=div)
divisionbutton.pack(pady=10)

modulesbutton = tk.Button(root, text="%", font=("Book Antiqua", 15, 'bold'), bg='black', fg='Fuchsia', command=mod)
modulesbutton.pack(pady=10)

# Set the window transparency
root.attributes('-alpha', 0.8)

# Run the main event loop
root.mainloop()
