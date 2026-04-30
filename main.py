from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)


    password_list = [choice(letters) for _ in range(nr_letters)]
    password_list.extend([choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([choice(numbers) for _ in range(nr_numbers)])

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    email_data = email_username_entry.get()
    password_data = password_entry.get()

    new_website_data = website_data.strip()
    new_email_data = email_data.strip()
    new_password_data = password_data.strip()

    if not new_password_data or not new_email_data or not new_website_data:
        messagebox.showwarning(title= "", message= "Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title= "", message= f"These are the details entered: \n"
                                                           f"Website: {website_data} \nEmails: {email_data}\n"
                                                           f"Password: {password_data} \nIs it okay to save?")

        if is_ok:
            with open("data.txt", "a") as d:
                d.write(f"{website_data} | {email_data} | {password_data} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

# Labels
website_label = Label(text= "Website:")
website_label.grid(column= 0, row= 1)

email_username_label = Label(text= "Email/Username:")
email_username_label.grid(column= 0, row= 2)

password_label = Label(text= "Password:")
password_label.grid(column= 0, row= 3)

# Entries
website_entry = Entry(width= 38)
website_entry.focus()
website_entry.grid(column= 1, row= 1, columnspan= 2)

email_username_entry = Entry(width= 38)
email_username_entry.insert(0, "sushil@gmail.com")
email_username_entry.grid(column= 1, row= 2, columnspan= 2)

password_entry = Entry(width= 21)
password_entry.grid(column= 1, row= 3)

# Buttons
generate_button = Button(text= "Generate Password", command= generate_password)
generate_button.grid(column= 2, row= 3)

add_button = Button(text= "Add", width= 36, command= save)
add_button.grid(column= 1, row= 4, columnspan= 2)

# Canvas
canvas = Canvas(width= 200, height= 200, )
logo = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= logo)
canvas.grid(column= 1, row= 0)


window.mainloop()