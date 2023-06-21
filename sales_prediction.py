import tkinter

window = tkinter.Tk()
window.title("Sales Prediction Tool")
window.geometry("350x150")

# Constants
typical_profit_percentage = 0.23

# Functions
def calculate_profit_and_display ():
    entry = float(projected_sales_entry.get())
    profit = typical_profit_percentage * entry
    estimate_label.config(text="$" + str(round(profit, 2)))

# Project sales label
projected_sales_label = tkinter.Label(window, text="Projected total sales: ")
projected_sales_label.grid(row=0, column=0,)
# Projected sales entry
projected_sales_entry = tkinter.Entry(window)
projected_sales_entry.grid(row=0, column=1)
# Estimated profit entry
estimated_profit_label = tkinter.Label(window, text="Estimated Annual Profit: ")
estimated_profit_label.grid(row=1, column=0)

# Calculate profit button
button = tkinter.Button(window, text="Calculate Profit", command= calculate_profit_and_display)
button.grid(row=2, column=0, sticky="WENS")

# Estimated profit label
estimate_label = tkinter.Label(window, text="")
estimate_label.grid(row=1, column=1)

# Pad GUI elements
for widget in window.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()