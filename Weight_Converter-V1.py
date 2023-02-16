import tkinter as tk
import tkinter.messagebox


a_font = "helvetica 12 bold"


def about():
    tk.messagebox.showinfo('Weight Converter V1.0',
                           '\nInput desired weight and'
                           ' choose your preferred\n'
                           'option of kgrams, pounds or stones.\n'
                           '\nNow click on Convert.\n'
                           '\nThis program is FREEWARE,\nbut remains'
                           ' (c) Steve Shambles Feb 2023')


def convert():

    try:
        weight = float(e1.get())
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

    label1.config(fg="green", font=a_font, text=f"{round(kg, 2)} kgrams")
    label2.config(fg="green", font=a_font, text=f"{round(stones, 2)} stones")
    label3.config(fg="green", font=a_font, text=f"{round(pounds, 2)} pounds")


root = tk.Tk()
root.title("Weight Converter")
root.geometry("300x180")
root.resizable(False, False)

e1 = tk.Entry(root)
e1.grid(row=0, column=0, pady=10, padx=10)

var = tk.StringVar(value="kgrams")
option = tk.OptionMenu(root, var, "stones", "pounds", "kgrams")
option.grid(row=0, column=1)

label1 = tk.Label(root, text="")
label1.grid(row=2, column=0)
label2 = tk.Label(root, text="")
label2.grid(row=3, column=0)
label3 = tk.Label(root, text="")
label3.grid(row=4, column=0)

b1 = tk.Button(root, text="     Convert   ", command=convert)
b1.grid(row=1, column=1)

# Create drop down menu.
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Info', menu=file_menu)
file_menu.add_command(label='Help', command=about)

root.config(menu=menu_bar)

root.mainloop()
