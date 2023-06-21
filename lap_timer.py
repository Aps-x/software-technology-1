import tkinter

window = tkinter.Tk()
window.title("Lap Timer Tool")
window.geometry("400x250")

lap_times = []

def lap_times_prompts ():
    # Initialize variables & reset objects for re-usability
    i = 1
    j = 0
    laps_num = int(laps_entry.get())
    lap_times.clear()
    fastest_lap_label.config(text="")
    slowest_lap_label.config(text="")
    average_lap_label.config(text="")
    # Loop
    for x in range(laps_num):
        # Generate prompt to enter lap times
        lap_time_label.config(text="Enter the time for lap " + str(i))
        # Lap entry
        laps_time_entry = tkinter.Entry(window)
        laps_time_entry.grid(row=1, column=1)
        # Button to enter time and move to next lap
        button_pressed = tkinter.StringVar()
        button = tkinter.Button(window, text="Enter", command=lambda: button_pressed.set("button pressed"))
        button.grid(row=1, column=2)
        # Wait for button to be pressed
        button.wait_variable(button_pressed)
        # Submit lap time to list
        lap_times.insert(j,  float(laps_time_entry.get()))
        # Increment variables
        i += 1
        j += 1
    calculate_results()

def calculate_results ():
    lap_times.sort()
    fastest_lap_label.config(text="You fastest lap time was " + str(round(lap_times[0], 2)))
    slowest_lap_label.config(text="You slowest lap time was " + str(round(lap_times[-1], 2)))
    average_lap_label.config(text="You average lap time was " + str(round(sum(lap_times)/len(lap_times), 2)))

# Laps input label
laps_label = tkinter.Label(window, text="Enter number of laps")
laps_label.grid(row=0, column=0,)
# Laps input entry
laps_entry = tkinter.Entry(window)
laps_entry.grid(row=0, column=1)

# Enter laps button
button = tkinter.Button(window, text="Start", command= lap_times_prompts)
button.grid(row=0, column=2, sticky="WENS")

# Lap time label
lap_time_label = tkinter.Label(window, text="")
lap_time_label.grid(row=1, column=0)

# Fastest lap label
fastest_lap_label = tkinter.Label(window, text="")
fastest_lap_label.grid(row=2, column=0)

# Slowest lap label
slowest_lap_label = tkinter.Label(window, text="")
slowest_lap_label.grid(row=3, column=0)

# Average lap label
average_lap_label = tkinter.Label(window, text="")
average_lap_label.grid(row=4, column=0)

# Pad GUI elements
for widget in window.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()