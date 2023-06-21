import tkinter

window = tkinter.Tk()
window.title("ST1 Quiz Mark Calculator")
window.geometry("350x200")

def calculate_sum ():
    quiz1_marks = int(quiz1_entry.get())
    quiz2_marks = int(quiz2_entry.get())
    quiz3_marks = int(quiz3_entry.get())
    quiz4_marks = int(quiz4_entry.get())
    sum = quiz1_marks + quiz2_marks + quiz3_marks + quiz4_marks
    result_label.config(text="The quiz marks for ST1 unit is " + str(sum))

# Quiz 1
quiz1_label = tkinter.Label(window, text="Enter quiz 1 marks(out of 10)")
quiz1_label.grid(row=0, column=0,)
quiz1_entry = tkinter.Entry(window)
quiz1_entry.grid(row=0, column=1)
# Quiz 2
quiz2_label = tkinter.Label(window, text="Enter quiz 2 marks(out of 10)")
quiz2_label.grid(row=1, column=0,)
quiz2_entry = tkinter.Entry(window)
quiz2_entry.grid(row=1, column=1)
# Quiz 3
quiz3_label = tkinter.Label(window, text="Enter quiz 3 marks(out of 10)")
quiz3_label.grid(row=2, column=0,)
quiz3_entry = tkinter.Entry(window)
quiz3_entry.grid(row=2, column=1)
# Quiz 4
quiz4_label = tkinter.Label(window, text="Enter quiz 4 marks(out of 10)")
quiz4_label.grid(row=3, column=0,)
quiz4_entry = tkinter.Entry(window)
quiz4_entry.grid(row=3, column=1)

# Calculate grade button
button = tkinter.Button(window, text="Calculate Sum", command= calculate_sum)
button.grid(row=4, column=0, sticky="WENS")

# Result label
result_label = tkinter.Label(window, text=" ")
result_label.grid(row=5, column=0)

# Pad GUI elements
for widget in window.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()