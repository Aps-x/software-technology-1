import tkinter

window = tkinter.Tk()
window.title("Stadium Seating Revenue Calculator")

# Constants
a_ticket_price = 20
b_ticket_price = 15
c_ticket_price = 10

# Functions
def calculate_income ():
    a_tickets_sold = int(a_entry.get())
    b_tickets_sold = int(b_entry.get())
    c_tickets_sold = int(c_entry.get())
    result = (a_tickets_sold * a_ticket_price) + (b_tickets_sold * b_ticket_price) + (c_tickets_sold * c_ticket_price)
    result_label.config(text="Total revenue from ticket sales: " + "$" + str(result))

# A
a_label = tkinter.Label(window, text="Enter class A seat tickets sold)")
a_label.grid(row=0, column=0,)
a_entry = tkinter.Entry(window)
a_entry.grid(row=0, column=1)
# B
b_label = tkinter.Label(window, text="Enter class B seat tickets sold")
b_label.grid(row=1, column=0,)
b_entry = tkinter.Entry(window)
b_entry.grid(row=1, column=1)
# C
c_label = tkinter.Label(window, text="Enter class C seat tickets sold")
c_label.grid(row=2, column=0,)
c_entry = tkinter.Entry(window)
c_entry.grid(row=2, column=1)

# Calculate income button
button = tkinter.Button(window, text="Calculate income", command= calculate_income)
button.grid(row=4, column=0, sticky="WENS")

# Result label
result_label = tkinter.Label(window, text="")
result_label.grid(row=5, column=0)

# Pad GUI elements
for widget in window.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()