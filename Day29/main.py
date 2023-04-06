from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            'email' : email,
            'password' : password
        }
    }
    print(new_data)
    if website == "" or email == "" or password == "":
        messagebox.showwarning(title="Warning", message="Don't leave any blank field")
    else:
        try:
            with open("pword.json", "r") as pword:
                data = json.load(pword)
                data.update(new_data)
        except FileNotFoundError:
            with open("pword.json", 'w') as pword:
                json.dump(new_data, pword, indent=4)
        else:
            with open("pword.json", 'w') as pword:
                json.dump(data, pword, indent=4)
        finally:
            web_entry.focus()
            web_entry.delete(0, END)
            password_entry.delete(0, END)

# ----------------------------Search function-------------------------- #
def search_website():
    website = web_entry.get()
    try:
        with open("pword.json", "r") as pword:
            data = json.load(pword)
            output = data.get(website, False)
    except FileNotFoundError:
        messagebox.showinfo(title="oops", message="No data found")
    else:
        if output:
            messagebox.showinfo(title="Here's the Info", message=f"username: {output.get('email')}\npassword: {output.get('password')}")
        else:
            messagebox.showinfo(title="oops", message="No data found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
window.config(padx=20, pady=20)
# window.minsize(400, 400)

#canvas
canvas = Canvas(width=300, height=200)
my_image = PhotoImage(file="logo.png")
logo = canvas.create_image(150, 100, image=my_image)

#label
website_lable = Label(text="Website:")
email_lable = Label(text="Email/Username:")
password_lable = Label(text="Password:")

#Enrty
web_entry = Entry(width=20)
web_entry.focus()
email_entry = Entry(width=38)
email_entry.insert(0, "jagan2221997@gmail.com")
password_entry = Entry(width=20)

#Button
generate_password = Button(text="Generate Password", command=generate_password)
add_entry = Button(text="Add", command=save_data)
search = Button(text='Search', command=search_website)

#Packing on grid
website_lable.grid(column=0, row=1, sticky="e")
email_lable.grid(column=0, row=2, sticky="e")
password_lable.grid(column=0, row=3, sticky="e")
canvas.grid(column=0, row=0, columnspan=3)
web_entry.grid(column=1, row=1, columnspan=2, sticky="w")
email_entry.grid(column=1, row=2, columnspan=2, sticky="w")
password_entry.grid(column=1, row=3, sticky="w")
generate_password.grid(column=2, row=3, sticky="w")
add_entry.grid(column=1, row=4)
search.grid(column=2, row=1, sticky="w")

window.mainloop()