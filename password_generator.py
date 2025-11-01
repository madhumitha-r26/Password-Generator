import tkinter as tk
import random

# Define character sets
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "*@/|\-.?!+$%^#_&~"

all_chars = lower + upper + numbers + symbols

def generate_password():
    try:
        length = int(length_entry.get())
        if length >= 8 and length <= 15:
            # Ensure at least one of each type
            password_list = [
                random.choice(lower),
                random.choice(upper),
                random.choice(numbers),
                random.choice(symbols)
            ]
            # Fill the rest randomly from all_chars
            remaining_length = length - 4
            if remaining_length > 0:
                password_list.extend(random.sample(all_chars, remaining_length))
            # Shuffle to randomize order
            random.shuffle(password_list)
            password = "".join(password_list)
            
            # Store the password for copying
            global generated_password
            generated_password = password
            
            result_label.config(text=f"Your generated password: {password}", fg="black")
            copy_button.place(x=120, y=150)  # Show copy button
            copy_button.config(state=tk.NORMAL)  # Enable copy button
        else:
            result_label.config(text="Password length must be between 8 and 15!", fg="red")
            copy_button.place_forget()  # Hide copy button on invalid length
    except ValueError:
        result_label.config(text="Please enter a valid integer for length!", fg="red")
        copy_button.place_forget()  # Hide copy button on error

def clear_password():
    length_entry.delete(0, tk.END)
    result_label.config(text="")
    copy_button.place_forget()  # Hide copy button

def copy_password():
    if 'generated_password' in globals() and generated_password:
        root.clipboard_clear()
        root.clipboard_append(generated_password)
        result_label.config(text=f"Password copied to clipboard: {generated_password}", fg="#4a2345")
    else:
        result_label.config(text="No password to copy. Generate one first.", fg="red")

# Create the main window
root = tk.Tk()
root.geometry("400x250")
root.title("Password Generator")

# Create and place widgets
instruction_label = tk.Label(root, font="Calibri 14 bold", text="Enter the length of your password:")
instruction_label.place(x=10, y=10)

length_entry = tk.Entry(root, width=45, font="Calibri 12")
length_entry.place(x=10, y=50)

clear_button = tk.Button(root, font="Calibri 14 bold",  text="Clear", bg="red", fg="white", width=15, height=1, activebackground="#e14141", command=clear_password)
clear_button.place(x=210, y=100)


generate_button = tk.Button(root, font="Calibri 14 bold", text="Generate", bg="green", fg="white", width=20, height=1, activebackground="#32cd32", command=generate_password)
generate_button.place(x=20, y=100)

result_label = tk.Label(root, text="", font="Calibri 14")
result_label.place(x=40, y=200)



copy_button = tk.Button(root, font="Calibri 12 bold", text="Copy Password", bg="blue", fg="white", width=20, height=1, activebackground="#4169e1", command=copy_password, state=tk.DISABLED)
# Do not place initially; it will be placed after generation

# Start the GUI event loop
root.mainloop()
