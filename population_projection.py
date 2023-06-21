from tkinter import *
root = Tk()
root.title("Population Projection Program")
root.geometry("800x500")

# There are 3.154e+7 seconds in a year
# 3.154e+7 / 7 = +4505714.28571 births in a year
# 3.154e+7 / 13 = -2426153.84615 deaths in a year
# 3.154e+7 / 45 = +700888.888889 migrants in a year
# Australia’s population was 25,978,935 people at 30 June 2022, last confirmed by the ABS
# Assuming a year is 365 days

### Constants ###
confirmed_pop_base = 25978935
births_in_year = 4505714.28571
deaths_in_year = 2426153.84615
migrants_in_year = 700888.888889

### Population estimates for each year ###
pop2023_estimate = confirmed_pop_base + 1*(births_in_year + migrants_in_year - deaths_in_year)
pop2024_estimate = confirmed_pop_base + 2*(births_in_year + migrants_in_year - deaths_in_year)
pop2025_estimate = confirmed_pop_base + 3*(births_in_year + migrants_in_year - deaths_in_year)
pop2026_estimate = confirmed_pop_base + 4*(births_in_year + migrants_in_year - deaths_in_year)
pop2027_estimate = confirmed_pop_base + 5*(births_in_year + migrants_in_year - deaths_in_year)
pop2028_estimate = confirmed_pop_base + 6*(births_in_year + migrants_in_year - deaths_in_year)

### Display ###
label_title = Label(root, text="Population Projection", font="Arial 20 bold")
label_explanation = Label(root, text="Assuming one birth every 7 seconds, one death every 13 seconds, and one new immigrant every 45 seconds", font="Arial, 12", pady=10)

label2022 = Label(root, text="2022 Population (confirmed): 25,978,935", anchor='w', font="Arial, 12", pady=20, padx=10)
label2023 = Label(root, text=f"2023 Population (projected): {int(pop2023_estimate):,}", anchor='w', font="Arial, 12", pady=20, padx=10)
label2024 = Label(root, text=f"2024 Population (projected): {int(pop2024_estimate):,}", anchor='w', font="Arial, 12", pady=20, padx=10)
label2025 = Label(root, text=f"2025 Population (projected): {int(pop2025_estimate):,}", anchor='w', font="Arial, 12", pady=20, padx=10)
label2026 = Label(root, text=f"2026 Population (projected): {int(pop2026_estimate):,}", anchor='w', font="Arial, 12", pady=20, padx=10)
label2027 = Label(root, text=f"2027 Population (projected): {int(pop2027_estimate):,}", anchor='w', font="Arial, 12", pady=20, padx=10)
label2028 = Label(root, text=f"2028 Population (projected): {int(pop2028_estimate):,}", anchor='w', font="Arial, 12", pady=20, padx=10)

label_title.pack()
label_explanation.pack()
label2022.pack(fill='both')
label2023.pack(fill='both')
label2024.pack(fill='both')
label2025.pack(fill='both')
label2026.pack(fill='both')
label2027.pack(fill='both')
label2028.pack(fill='both')

root.mainloop()