from tkinter import *
import random
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = "aquickbrownfoxjumpsoveralazydog"
    numbers = "1234567890"
    symbols = "!@#$$%^&*()"

    nr_letters = random.randint(a=6, b=8)
    nr_numbers = random.randint(a=3, b=5)
    nr_symbols = random.randint(a=1, b=2)

    a = random.sample(list(letters), nr_letters)
    b = random.sample(list(numbers), nr_symbols)
    c = random.sample(list(symbols), nr_numbers)


    nr_upper = random.randint(3, 4)

    upper_letters = "".join(a[:nr_upper]).upper()

    passcode = list(upper_letters) + a[nr_upper:] + b + c
    passcode = "".join(passcode)
    #print(passcode)
    password_entry.insert(0, passcode)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    site = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        site: {
            "Email": email,
            "Password": password,
        }
    }

    if len(password) == 0 or len(site) == 0 or len(email) == 0:
        messagebox.showinfo(title="OOps", message="Please make sure you haven't left any filed empty")

    else:
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered: \nEmail: {email}\n"
                                                           f"Password: {password}\nDO you want to Save?")
        if is_ok:
            # Reading Data
            try:
                with open("password.json", "r") as f:
                    # Reading old data
                    data = json.loads(f)
            except FileNotFoundError:
                with open("password.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                # Updating Old data with new data
                data.update(new_data)

                # writing Data
                with open("password.json", "w") as f:
                    json.dump(data, f, indent=4)

                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_pass)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
