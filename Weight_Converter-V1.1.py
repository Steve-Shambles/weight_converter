"""Weight Converter V1.1. Input a number and have it converted to Pounds,
   Stones and Kgs.
   (c) Steve Shambles Feb 2023, Freeware, code is MIT Licence."""

import tkinter as tk
import tkinter.messagebox
import sys
from PIL import Image, ImageTk

a_font = "helvetica 12 bold"


def about():
    """ Pop up containg program info. """
    tk.messagebox.showinfo('Weight Converter V1.1',
                           '\nInput desired weight and'
                           ' choose your preferred\n'
                           'option of kgrams, pounds or stones.\n'
                           '\nNow click on Convert.\n'
                           '\nThis program is FREEWARE,\nbut remains'
                           ' (c) Steve Shambles Feb 2023')


def convert():
    """ Convert and display the input number to all three supported
        weight systems. """
    try:
        weight = float(entry_box.get())
    except ValueError:
        return

    unit = var.get()
    stones = 0
    pounds = 0
    kg = 0

    if unit == "stones":
        stones = weight
        pounds = weight * 14
        kg = weight * 6.35
    elif unit == "pounds":
        stones = weight / 14
        pounds = weight
        kg = weight * 0.453592
    elif unit == "kgrams":
        stones = weight / 6.35
        pounds = weight / 0.453592
        kg = weight

    message = f"{round(kg, 2)} kgrams\n{round(stones, 2)} stones\n{round(pounds, 2)} pounds    "
    tk.messagebox.showinfo('Weight Converter V1.1', message)


root = tk.Tk()
root.title("Weight Convert")
root.resizable(False, False)

# Load and display logo in a frame.
logo_frame = tk.LabelFrame(root)
logo_frame.grid()

try:
    logo_image = Image.open("wc.jpg")
except FileNotFoundError as e:
    tk.messagebox.showinfo("FileNotFoundError",
                           "wc.jpg not found.")
    root.destroy()
    sys.exit(1)

logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(logo_frame, image=logo_photo)
logo_label.logo_image = logo_photo
logo_label.grid(padx=2, pady=2, row=0, column=0)

# Create entry box in its own frame.
widget_frame = tk.LabelFrame(root)
widget_frame.grid(row=1, column=0)

entry_box = tk.Entry(widget_frame, width=10)
entry_box.grid(row=0, column=1, pady=10, padx=10)

# Create option menu.
var = tk.StringVar(value="kgrams")
option = tk.OptionMenu(widget_frame, var, "stones", "pounds", "kgrams")
option.grid(row=0, column=2)

# Create the Convert button.
b1 = tk.Button(root, text="     Convert   ", bg="lime", command=convert)
b1.grid(row=2, column=0, pady=12)

# Create drop down menu.
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Info', menu=file_menu)
file_menu.add_command(label='Help', command=about)
root.config(menu=menu_bar)


root.mainloop()
