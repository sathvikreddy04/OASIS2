import random
import tkinter as tk


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = int(letter_entry.get())
    nr_symbols = int(symbol_entry.get())
    nr_numbers = int(number_entry.get())

    password = []

    for _ in range(nr_letters):
        password.append(random.choice(letters))

    for _ in range(nr_symbols):
        password.append(random.choice(symbols))

    for _ in range(nr_numbers):
        password.append(random.choice(numbers))

    random.shuffle(password)
    generated_password = ''.join(password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)




window = tk.Tk()
window.minsize(height=400, width=850)
window.title("Password Generator")


letter_label = tk.Label(window, text="How many letters?")
letter_label.pack(pady=5)
letter_entry = tk.Entry(window)
letter_entry.pack()

symbol_label = tk.Label(window, text="How many symbols?")
symbol_label.pack(pady=5)
symbol_entry = tk.Entry(window)
symbol_entry.pack()

number_label = tk.Label(window, text="How many numbers?")
number_label.pack(pady=5)
number_entry = tk.Entry(window)
number_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

password_entry = tk.Entry(window, width=30)
password_entry.pack(pady=5)



window.mainloop()
