import random
import pyperclip
from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_letters + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if (len(website) == 0 or len(email) == 0 or len(password) == 0):
        messagebox.showerror(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: {email} \nPassword: {password}\nIs it ok to save?")

        if (is_ok):
            with open("passwordManager/passwords.txt", "a") as fhand:
                fhand.write(f"{website} | {email} | {password} \n")
                website_input.delete(0, "end")
                email_input.delete(0, "end")
                password_input.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="passwordManager/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=1, columnspan=3)

website_label = Label(text="website:", font=("Arial", 10))
website_label.grid(column=1, row=2)

website_input = Entry(width=35, font=("Arial", 10))
website_input.focus()
website_input.grid(column=2, row=2, columnspan=2, sticky="EW")

email_label = Label(text="email/username:", font=("Arial", 10))
email_label.grid(column=1, row=3)

email_input = Entry(width=35, font=("Arial", 10))
email_input.grid(column=2, row=3, columnspan=2, sticky="EW")

password_label = Label(text="password:", font=("Arial", 10))
password_label.grid(column=1, row=4)

password_input = Entry(width=21, font=("Arial", 10))
password_input.grid(column=2, row=4, sticky="EW")

generate_password_button = Button(text="Generate password", command=generate_password, font=("Arial", 10))
generate_password_button.grid(column=3, row=4, sticky="EW")

add_button = Button(text="Add", width=36, command=save_password, font=("Arial", 10))
add_button.grid(column=2, row=5, columnspan=2, sticky="EW")

window.mainloop()