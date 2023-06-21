import tkinter
import tkinter.messagebox

window = tkinter.Tk()
window.title("Cups to Ounces Converter")

# Constants
CUP_TO_KILOS_FACTOR = 8

# Functions
def convert_and_display ():
    entry = cups_entry.get()
    try:
        entry = float(entry)
    except:
        tkinter.messagebox.showwarning(title="Error message", message="Enter valid input")
    else:
        result = entry * CUP_TO_KILOS_FACTOR
        tkinter.messagebox.showinfo(title="Results", message=f"{entry} cups is equal to {result} ounces.")


# Pounds label
cups_label = tkinter.Label(window, text="Cups: ")
cups_label.grid(row=0, column=0,)
# Pounds entry
cups_entry = tkinter.Entry(window)
cups_entry.grid(row=0, column=1)

# Conversion button
button = tkinter.Button(window, text="Convert", command= convert_and_display)
button.grid(row=1, column=0)

# Quit button
button = tkinter.Button(window, text="Quit", command= quit)
button.grid(row=1, column=1, sticky="WENS")

# Pad GUI elements
for widget in window.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()