import tkinter

window = tkinter.Tk()
window.title("Student Information Display")
window.geometry("650x550")

frame = tkinter.Frame(window)
frame.pack()

def enter_student_info ():
    # Retrieve and display info
    display_student_name_label.config(text=str(student_name_entry.get()))
    display_student_address_label.config(text=str(student_address_entry.get()))
    display_student_suburb_label.config(text=str(student_suburb_entry.get()))
    display_student_state_label.config(text=str(student_state_entry.get()))
    display_student_postcode_label.config(text=str(student_postcode_entry.get()))
    display_student_telephone_label.config(text=str(student_telephone_entry.get()))
    display_student_course_label.config(text=str(student_course_entry.get()))

### Student info input ###
student_info_frame = tkinter.LabelFrame(frame, text="Student Information Input")
student_info_frame.grid(row=0, column=0, padx=20, pady=20, sticky='W')

# Name label
student_name_label = tkinter.Label(student_info_frame, text="Student Name")
student_name_label.grid(row=0, column=0)
# Name entry
student_name_entry = tkinter.Entry(student_info_frame)
student_name_entry.grid(row=1, column=0)

# Address label
student_address_label = tkinter.Label(student_info_frame, text="Address")
student_address_label.grid(row=2, column=0)
# Address entry
student_address_entry = tkinter.Entry(student_info_frame)
student_address_entry.grid(row=3, column=0)

# Suburb label
student_suburb_label = tkinter.Label(student_info_frame, text="Suburb")
student_suburb_label.grid(row=2, column=1)
# Suburb entry
student_suburb_entry = tkinter.Entry(student_info_frame)
student_suburb_entry.grid(row=3, column=1)

# State label
student_state_label = tkinter.Label(student_info_frame, text="State")
student_state_label.grid(row=2, column=2)
# State entry
student_state_entry = tkinter.Entry(student_info_frame)
student_state_entry.grid(row=3, column=2)

# Postcode label
student_postcode_label = tkinter.Label(student_info_frame, text="Postcode")
student_postcode_label.grid(row=2, column=3)
# Postcode entry
student_postcode_entry = tkinter.Entry(student_info_frame)
student_postcode_entry.grid(row=3, column=3)

# Telephone label
student_telephone_label = tkinter.Label(student_info_frame, text="Telephone Number")
student_telephone_label.grid(row=4, column=0)
# Telephone entry
student_telephone_entry = tkinter.Entry(student_info_frame)
student_telephone_entry.grid(row=5, column=0)

# Course label
student_course_label = tkinter.Label(student_info_frame, text="University Course")
student_course_label.grid(row=6, column=0)
# Course entry
student_course_entry = tkinter.Entry(student_info_frame)
student_course_entry.grid(row=7, column=0)

# Enter info button
button = tkinter.Button(student_info_frame, text="Enter Student Info", command= enter_student_info)
button.grid(row=8, column=0, sticky="WENS")

### Student info display ###
display_info_frame = tkinter.LabelFrame(frame, text="Student Information Display")
display_info_frame.grid(row=2, column=0, padx=20, pady=10, sticky="WENS")

# Name display
display_student_name_label = tkinter.Label(display_info_frame, text="")
display_student_name_label.grid(row=0, column=0, sticky='W')

# Address display
display_student_address_label = tkinter.Label(display_info_frame, text="")
display_student_address_label.grid(row=1, column=0, sticky='W')

# Suburb display
display_student_suburb_label = tkinter.Label(display_info_frame, text="")
display_student_suburb_label.grid(row=2, column=0, sticky='W')

# State display
display_student_state_label = tkinter.Label(display_info_frame, text="")
display_student_state_label.grid(row=3, column=0, sticky='W')

# Postcode display
display_student_postcode_label = tkinter.Label(display_info_frame, text="")
display_student_postcode_label.grid(row=4, column=0, sticky='W')

# Telephone display
display_student_telephone_label = tkinter.Label(display_info_frame, text="")
display_student_telephone_label.grid(row=5, column=0, sticky='W')

# Course display
display_student_course_label = tkinter.Label(display_info_frame, text="")
display_student_course_label.grid(row=6, column=0, sticky='W')

# Pad GUI elements
for widget in student_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()