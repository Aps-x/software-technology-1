import tkinter

window = tkinter.Tk()
window.title("Pounds to Kilograms Converter")
window.geometry("350x150")

# Constants
pounds_kilos_ratio = 0.454

# Functions
def convert_and_display ():
    entry = float(pounds_entry.get())
    result = pounds_kilos_ratio * entry
    result_label.config(text=str(round(result, 3))+" kg")

# Pounds label
pounds_label = tkinter.Label(window, text="Pounds: ")
pounds_label.grid(row=0, column=0,)
# Pounds entry
pounds_entry = tkinter.Entry(window)
pounds_entry.grid(row=0, column=1)
# Kilos label
kilos_label = tkinter.Label(window, text="Kilograms: ")
kilos_label.grid(row=1, column=0)

# Conversion button
button = tkinter.Button(window, text="Convert", command= convert_and_display)
button.grid(row=2, column=0)

# Conversion result label
result_label = tkinter.Label(window, text="")
result_label.grid(row=1, column=1)

# Pad GUI elements
for widget in window.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()