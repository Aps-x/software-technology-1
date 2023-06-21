## Author: Adam Seaton
## Date created: 04/05/2023
## Date last changed: 16/05/2023
## This program prompts the user to input tool weights for each astronaut leaving on a trip to space.
## The program then calculates the leftover mass for each astronaut, the total available mass, the average available
## mass, and the equivalent average available mass on the destination celestial body. We will assume there will be
## three crew members and three mission specialists.
## Input: "celestial_bodies.csv" , Output: none

# Modules
import tkinter as tk
import csv

# Variables
error_bool = False

# Constants
NUM_ASTRONAUTS = 6
MIN_WEIGHT = 0
MAX_CREW_WEIGHT = 100
MAX_SPECIALIST_WEIGHT = 150

# Data structures
csv_file = "celestial_bodies.csv"
celestial_bodies_dict = {}


# Functions
def import_celestial_bodies():
    # The business rules stated that the celestial bodies and their mass multipliers *NOT* be hard coded.
    # Therefore, this program loads the celestial body data from a csv file.
    with open(csv_file) as file:
        # Read the file
        reader = csv.DictReader(file)
        # Insert values
        for row in reader:
            celestial_bodies_dict[row["celestial_body"]] = float(row["mass_multiplier"])


def calculate_results():
    global error_bool

    # Reset
    reset_program()

    # Gather crew data and validate
    crew_weights = gather_crew_weights()
    validate_crew_weights(crew_weights)

    # Gather specialist data and validate
    specialist_weights = gather_specialist_weights()
    validate_specialist_weights(specialist_weights)

    # Gather destination celestial body data
    celestial_body = drop_value.get()
    mass_multiplier = celestial_bodies_dict[celestial_body]

    # Check if error has been raised; If True, don't continue; If False, continue
    if error_bool:
        return

    # Calculate and display leftover mass for each crew member and specialist
    leftover_mass = calculate_leftover_mass(crew_weights, specialist_weights)
    display_leftover_mass(leftover_mass)

    # Calculate and display the total leftover mass for all astronauts
    calculate_and_display_total_leftover_mass(leftover_mass)

    # Calculate the average weight available for all astronauts
    average_weight = calculate_and_display_average_weight_available(leftover_mass)

    # Calculate and display the equivalent average weight available on destination celestial body
    calculate_and_display_equivalent_average(average_weight, mass_multiplier)


def gather_crew_weights():
    crew_weight_1 = ent_crew_1.get()
    crew_weight_2 = ent_crew_2.get()
    crew_weight_3 = ent_crew_3.get()
    return [crew_weight_1, crew_weight_2, crew_weight_3]


def gather_specialist_weights():
    specialist_weight_1 = ent_specialist_1.get()
    specialist_weight_2 = ent_specialist_2.get()
    specialist_weight_3 = ent_specialist_3.get()
    return [specialist_weight_1, specialist_weight_2, specialist_weight_3]


def validate_crew_weights(crew_weights):
    # Loop over crew weights
    for x in crew_weights:
        try:
            # Validate that the input was numerical
            x = float(x)
        except ValueError:
            # 'ValueError' used because an unacceptable value could be entered by the user e.g. a string/character
            flag_error()
        else:
            # Validate that the input is between 0 and 100
            if MIN_WEIGHT <= x <= MAX_CREW_WEIGHT:
                continue
            else:
                flag_error()


def validate_specialist_weights(specialist_weights):
    # Loop over specialist weights
    for x in specialist_weights:
        try:
            # Validate that the input was numerical
            x = float(x)
        except ValueError:
            # 'ValueError' used because an unacceptable value could be entered by the user e.g. a string/character
            flag_error()
        else:
            # Validate that the input is between 0 and 150
            if MIN_WEIGHT <= x <= MAX_SPECIALIST_WEIGHT:
                continue
            else:
                flag_error()


def calculate_leftover_mass(crew_weights, specialist_weights):
    leftover_mass = []
    # Calculate leftover mass for crew
    for weight in crew_weights:
        weight = MAX_CREW_WEIGHT - float(weight)
        leftover_mass.append(weight)
    # Calculate leftover mass for specialists
    for weight in specialist_weights:
        weight = MAX_SPECIALIST_WEIGHT - float(weight)
        leftover_mass.append(weight)
    return leftover_mass


def display_leftover_mass(leftover_mass):
    # Display leftover mass for crew
    lbl_available_mass_1.config(text=f"{round(leftover_mass[0], 2)}kg")
    lbl_available_mass_2.config(text=f"{round(leftover_mass[1], 2)}kg")
    lbl_available_mass_3.config(text=f"{round(leftover_mass[2], 2)}kg")
    # Display leftover mass for specialists
    lbl_available_mass_4.config(text=f"{round(leftover_mass[3], 2)}kg")
    lbl_available_mass_5.config(text=f"{round(leftover_mass[4], 2)}kg")
    lbl_available_mass_6.config(text=f"{round(leftover_mass[5], 2)}kg")


def calculate_and_display_total_leftover_mass(leftover_mass):
    total_leftover_mass = sum(leftover_mass)
    lbl_total_leftover_mass.config(text=f"Total leftover mass: {round(total_leftover_mass, 2)}kg")


def calculate_and_display_average_weight_available(leftover_mass):
    average_weight = sum(leftover_mass) / NUM_ASTRONAUTS
    lbl_average_weight.config(text=f"Average available weight is: {round(average_weight, 2)}kg")
    return average_weight


def calculate_and_display_equivalent_average(average_weight, mass_multiplier):
    lbl_equivalent_average.config(text=f"Equivalent average on destination: {round(average_weight * mass_multiplier, 2)}kg")


def flag_error():
    global error_bool
    ent_value.set("Please enter numbers only; Crew weight: 0 - 100; Specialist weight: 0 - 150")
    error_bool = True


def reset_program():
    # Reset error bool and text
    global error_bool
    ent_value.set("")
    error_bool = False
    # Reset leftover mass displays
    lbl_available_mass_1.config(text="-")
    lbl_available_mass_2.config(text="-")
    lbl_available_mass_3.config(text="-")
    lbl_available_mass_4.config(text="-")
    lbl_available_mass_5.config(text="-")
    lbl_available_mass_6.config(text="-")
    # Reset outputs
    lbl_total_leftover_mass.config(text="Total leftover mass: ")
    lbl_average_weight.config(text="Average available weight is: ")
    lbl_equivalent_average.config(text="Equivalent average on destination: ")


def update_mass_multiplier(loadbearing_argument):
    lbl_mass_multiplier.config(text=f"Mass multiplier for {drop_value.get()} is {celestial_bodies_dict[drop_value.get()]}")


# Load the celestial body data; this has to be done before the tkinter elements that use the data are created
import_celestial_bodies()

# Create the main window
window = tk.Tk()
window.title("Astronaut Mass Calculator")

# Create base frame
frm_base = tk.Frame(window)
frm_base.pack()

#=======================================================================================================================
# Information input frame
#=======================================================================================================================
frm_input = tk.LabelFrame(frm_base, text="Information Input", font="SegoeUI 10 bold")
frm_input.grid(row=1, column=0, padx=20, pady=(20, 10), sticky='W')

# Row Zero =============================================================================================================

# Destinations label
lbl_destinations = tk.Label(frm_input, text="Destinations", font="SegoeUI 12 bold")
lbl_destinations.grid(row=0, column=0)

# Max Tool Weights label
lbl_max_tool_weights = tk.Label(frm_input, text="Max Tool Weights", font="SegoeUI 12 bold")
lbl_max_tool_weights.grid(row=0, column=1)

# Tool Weights label
lbl_tool_weights = tk.Label(frm_input, text="Tool Weights", font="SegoeUI 12 bold")
lbl_tool_weights.grid(row=0, column=2)

# Available label
lbl_available = tk.Label(frm_input, text="Available", font="SegoeUI 12 bold")
lbl_available.grid(row=0, column=3)

# Row One ==============================================================================================================

# Option menu celestial bodies
drop_value = tk.StringVar()
# Takes the first value from dictionary so the program can accommodate changes to the list of celestial bodies
drop_value.set(list(celestial_bodies_dict.keys())[0])
drop = tk.OptionMenu(frm_input, drop_value, *celestial_bodies_dict, command=update_mass_multiplier)
drop.grid(row=1, column=0)

# Crew label
lbl_crew = tk.Label(frm_input, text="Crew: 100kg")
lbl_crew.grid(row=1, column=1)

# Crew 1 entry
ent_crew_1 = tk.Entry(frm_input)
ent_crew_1.grid(row=1, column=2)

# Available mass 1 display
lbl_available_mass_1 = tk.Label(frm_input, text="-")
lbl_available_mass_1.grid(row=1, column=3)

# Row Two ==============================================================================================================

# Crew 2 entry
ent_crew_2 = tk.Entry(frm_input)
ent_crew_2.grid(row=2, column=2)

# Available mass 2 display
lbl_available_mass_2 = tk.Label(frm_input, text="-")
lbl_available_mass_2.grid(row=2, column=3)

# Row Three ============================================================================================================

# Crew 3 entry
ent_crew_3 = tk.Entry(frm_input)
ent_crew_3.grid(row=3, column=2)

# Available mass 3 display
lbl_available_mass_3 = tk.Label(frm_input, text="-")
lbl_available_mass_3.grid(row=3, column=3)

# Row Four =============================================================================================================

# Specialist label
specialist_label = tk.Label(frm_input, text="Mission Specialist: 150kg")
specialist_label.grid(row=4, column=1)

# Specialist 1 entry
ent_specialist_1 = tk.Entry(frm_input)
ent_specialist_1.grid(row=4, column=2)

# Available mass 4 display
lbl_available_mass_4 = tk.Label(frm_input, text="-")
lbl_available_mass_4.grid(row=4, column=3)

# Row Five =============================================================================================================

# Specialist 2 entry
ent_specialist_2 = tk.Entry(frm_input)
ent_specialist_2.grid(row=5, column=2)

# Available mass 5 display
lbl_available_mass_5 = tk.Label(frm_input, text="-")
lbl_available_mass_5.grid(row=5, column=3)

# Row Six ==============================================================================================================

# Specialist 3 entry
ent_specialist_3 = tk.Entry(frm_input)
ent_specialist_3.grid(row=6, column=2)

# Available mass 6 display
lbl_available_mass_6 = tk.Label(frm_input, text="-")
lbl_available_mass_6.grid(row=6, column=3)


#=======================================================================================================================
# Information output frame
#=======================================================================================================================
frm_output = tk.LabelFrame(frm_base, text="Information Output", font="SegoeUI 10 bold")
frm_output.grid(row=2, column=0, padx=20, pady=(10, 20), sticky='W')

# Mass multiplier label
# Takes the first value from dictionary so the program can accommodate changes to the list of celestial bodies
lbl_mass_multiplier = tk.Label(frm_output, text=f"Mass multiplier for {list(celestial_bodies_dict.keys())[0]} is: {list(celestial_bodies_dict.values())[0]}")
lbl_mass_multiplier.grid(row=0, column=0, sticky='W', columnspan=3)

# Total label
lbl_total_leftover_mass = tk.Label(frm_output, text="Total leftover mass:")
lbl_total_leftover_mass.grid(row=1, column=0, sticky='W', columnspan=3)

# Average available weight
lbl_average_weight = tk.Label(frm_output, text="Average available weight is: ")
lbl_average_weight.grid(row=2, column=0, sticky='W', columnspan=3)

# Equivalent average on destination
lbl_equivalent_average = tk.Label(frm_output, text="Equivalent average on destination: ")
lbl_equivalent_average.grid(row=3, column=0, sticky='W', columnspan=3)


# Calculate button
btn_calculate = tk.Button(frm_output, text="Calculate", command=calculate_results, width="25", background="light green", font="SegoeUI 9 bold")
btn_calculate.grid(row=4, column=0, sticky="WENS")

# Padding label
lbl_padding = tk.Label(frm_output, text="", width=12)
lbl_padding.grid(row=1, column=1)

# Quit button
btn_quit = tk.Button(frm_output, text="Quit", command=window.destroy, width="25", background="firebrick1", font="SegoeUI 9 bold")
btn_quit.grid(row=4, column=2, sticky="WENS")

# Entry box used to meet requirements "Output data using an entry widget [5 marks]"
ent_value = tk.StringVar()
ent_error = tk.Entry(frm_output, relief="flat", bg="#F0F0F0", fg="red", textvariable=ent_value, font="SegoeUI 10 bold")
ent_error.grid(row=5, column=0, sticky="WENS", columnspan=3)

# Pad GUI elements
for widget in frm_input.winfo_children():
    widget.grid_configure(padx=10, pady=5)

for widget in frm_output.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Enter the tkinter main loop
tk.mainloop()
