import tkinter

window = tkinter.Tk()
window.title("Fat and Carbs Tracker")
window.geometry("325x150")

# Constants
fat_multiplier = 3.9
carbs_multiplier = 4

# Functions
def calculate_fat ():
    fat = float(fat_entry.get())
    result = fat * fat_multiplier
    fat_result_label.config(text=str(result))

def calculate_carbs ():
    carbs = float(carbs_entry.get())
    result = carbs * carbs_multiplier
    carbs_result_label.config(text=str(result))

# Fat
fat_label = tkinter.Label(window, text="Enter fat grams")
fat_label.grid(row=0, column=0,)

fat_entry = tkinter.Entry(window)
fat_entry.grid(row=1, column=0, sticky="WENS")

fat_button = tkinter.Button(window, text="Calculate calories", command= calculate_fat)
fat_button.grid(row=2, column=0, sticky="WENS")

fat_result_label = tkinter.Label(window, text="")
fat_result_label.grid(row=3, column=0, sticky="WENS")

# Carbs
carbs_label = tkinter.Label(window, text="Enter carbohydrate grams")
carbs_label.grid(row=0, column=1,)

carbs_entry = tkinter.Entry(window)
carbs_entry.grid(row=1, column=1, sticky="WENS")

carbs_button = tkinter.Button(window, text="Calculate calories", command= calculate_carbs)
carbs_button.grid(row=2, column=1, sticky="WENS")

carbs_result_label = tkinter.Label(window, text="")
carbs_result_label.grid(row=3, column=1, sticky="WENS")

# Pad GUI elements
for widget in window.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()