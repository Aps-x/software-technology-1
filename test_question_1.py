import tkinter
import tkinter.messagebox
import math

window = tkinter.Tk()
window.title("Paint Job Cost Estimator")

# Constants
WALL_SPACE_FACTOR = 112
LABOR_FACTOR = 8
LABOR_COST_PER_HOUR = 35

# Functions
def calculate_costs ():
    wall_space = float(a_entry.get())
    paint_price = float(b_entry.get())
    paint_needed = math.ceil(wall_space / WALL_SPACE_FACTOR)
    labor_hours = (paint_needed * LABOR_FACTOR)
    labor_costs = (labor_hours * LABOR_COST_PER_HOUR)
    paint_costs = (paint_needed * paint_price)
    total_costs = (paint_costs + labor_costs)
    tkinter.messagebox.showinfo(title="Paint Job Cost Estimates", message=f"Gallons of paint: {paint_needed}\nHours of Labor: {labor_hours}\nPaint Charges: ${paint_costs:,}\nLabor Charges: ${labor_costs:,}\nTotal Cost: ${total_costs:,}")

# A
a_label = tkinter.Label(window, text="Wall space in feet:")
a_label.grid(row=0, column=0,)
a_entry = tkinter.Entry(window)
a_entry.grid(row=0, column=1)
# B
b_label = tkinter.Label(window, text="Paint price per gallon:")
b_label.grid(row=1, column=0,)
b_entry = tkinter.Entry(window)
b_entry.grid(row=1, column=1)

# Calculate result button
button = tkinter.Button(window, text="Estimate Painting Job Costs", command= calculate_costs)
button.grid(row=2, column=0, sticky="WENS")

# Quit button
button = tkinter.Button(window, text="Quit", command= quit)
button.grid(row=2, column=1, sticky="WENS")

# Pad GUI elements
for widget in window.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()