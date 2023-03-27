import tkinter
from random import shuffle, choice, randint
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = website_input.get()
    email = email_input.get()
    pwd = password_input.get()
    new_data = {
        web:
            {"email": email,
             "password": pwd,
            }
    }
    if web == "" or pwd == "" or email == "":
        messagebox.showinfo(title="Failed", message=f"You forget something" )
    else:
        try:
            with open("savepwd.json", mode="r") as filepwd:
                # Reading old data
                data = json.load(filepwd)
        except FileNotFoundError:
            with open("savepwd.json", mode="w") as filepwd:
                #Saving update data
                json.dump(new_data, filepwd, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("savepwd.json", mode="w") as filepwd:
                #Saving update data
                json.dump(data, filepwd, indent=4)
        finally:
            website_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)

def find_password():
    website = website_input.get()
    try:
        with open("savepwd.json") as data_file:
            file = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in file:
            email = file[website]["email"]
            password = file[website]["password"]
            messagebox.showinfo(title="Website", message=f"the Email: {email} \nthe password: {password} ")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
image_key = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image_key)
canvas.grid(column=1,row=0)

##Labels
#Website Label
website_label = tkinter.Label(text="Website: ", font=("Arial", 10))
website_label.grid(column=0,row=1)
#Email Label
email_label = tkinter.Label(text="Email/Username: ", font=("Arial", 10))
email_label.grid(column=0 , row=2)
#Password Label
password_label = tkinter.Label(text="Password: ", font=("Arial", 10))
password_label.grid(column=0, row=3)

##Entry
#Website input
website_input = tkinter.Entry(width=32)
website_input.grid(row=1, column=1)
website_input.focus()
#Email input
email_input = tkinter.Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "Phithon@gmail.com")
#password_input
password_input = tkinter.Entry(width=32)
password_input.grid(row=3, column=1)

#password_generate button
password_button = tkinter.Button(text="Generate Password", width=14, command=generate_password)
password_button.grid(row=3, column=2)
#search_ button
search_button = tkinter.Button(text="Search", width= 14, command=find_password)
search_button.grid(row=1, column=2)
#Add_button
add_button = tkinter.Button(text="Add", width=42, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
