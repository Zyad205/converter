import customtkinter as ctk
import decimal
from decimal import Decimal
from values import *


def btn_func(*_):
    if entry_input.get() == "":
        output_var.set("")
    else:
        try:
            # Using decimal for better accuracy to stop floating point system
            entry_value = Decimal(entry_input.get())
            input_multi = Decimal(VALUES_DICT[input_combobox_var.get()])
            output_multi = Decimal(VALUES_DICT[output_combobox_var.get()])
            result = (entry_value * input_multi) / output_multi
    
            output_var.set(result)
    
        except decimal.InvalidOperation:
            output_var.set("Invalid value")


def main_combobox_func(_):
    temp_list = MAIN_DICT[main_combobox_var.get()]
    input_combobox.configure(values=temp_list)
    input_combobox_var.set(temp_list[0])

    output_combobox.configure(values=temp_list)
    output_combobox_var.set(temp_list[-1])
    btn_func()


window = ctk.CTk()
window.geometry("350x200")

my_font = ctk.CTkFont(size=13)

main_combobox_var = ctk.StringVar(value='Mass')


main_combobox = ctk.CTkComboBox(
    window,
    variable=main_combobox_var,
    state="readonly",
    values=MAIN_COMBOBOX_VALUES,
    command=main_combobox_func)

main_combobox.bind("<KeyRelease>", lambda event: btn_func())

main_combobox.pack()
window.geometry("600x400")
window.minsize(550, 150)


entry_input = ctk.CTkEntry(window, font=my_font)
entry_input.place(x=3, rely=0.3, relwidth=0.2)

entry_input.bind("<KeyRelease>", lambda event: btn_func())

input_combobox_var = ctk.StringVar(value='Ton')

input_combobox = ctk.CTkComboBox(
    window,
    variable=input_combobox_var,
    values=SECONDARY_ITEM_MASS,
    width=5,
    state='readonly',
    font=my_font,
    command=btn_func)

input_combobox.place(relx=0.21, rely=0.3, relwidth=0.15)

output_combobox_var = ctk.StringVar(value="g")
output_combobox = ctk.CTkComboBox(
    window,
    variable=output_combobox_var,
    values=SECONDARY_ITEM_MASS,
    width=5,
    state="readonly",
    font=my_font,
    command=btn_func)

output_combobox.place(anchor="ne", relx=0.99, rely=0.3, relwidth=0.15)

output_var = ctk.StringVar(value="Still waiting for a value")
output_entry = ctk.CTkEntry(
    window,
    textvariable=output_var,
    font=my_font,
    state="readonly",
    width=50)

output_entry.place(relx=0.63, rely=0.3, relwidth=0.2)


window.mainloop()
