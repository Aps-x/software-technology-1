import pickle
import tkinter as tk

# Constants
LATITUDE_FACTOR = 10000
LONGITUDE_FACTOR = 100000

# Load the prediction model
with open('best_regr_model.h5', 'rb') as file:
    prediction_model = pickle.load(file)


# Functions
def predict_house_price(house_data):
    house_price_prediction = prediction_model.predict([house_data])
    return house_price_prediction


def custom_slider_value_display(load_bearing_argument):
    latitude_result_label.config(text=str(latitude_scale.get() / LATITUDE_FACTOR))
    longitude_result_label.config(text=str(longitude_scale.get() / LONGITUDE_FACTOR))


def process_house_price(house_price_raw):
    # Convert to string to strip unnecessary characters
    house_price_str = str(house_price_raw).strip('[].')
    # Convert to number and round
    house_price = round(float(house_price_str), 2)
    # Return processed house price value
    return house_price


def enter_info_and_display_price():
    # Collect primary information
    rooms = rooms_entry.get()
    bedrooms = bedrooms_entry.get()
    bathrooms = bathrooms_entry.get()
    carports = carports_entry.get()
    # Collect secondary information
    land = land_entry.get()
    building = building_entry.get()
    latitude = latitude_scale.get() / LATITUDE_FACTOR
    longitude = longitude_scale.get() / LONGITUDE_FACTOR

    # Collate house data
    house_data = (rooms, bedrooms, bathrooms, carports, land, building, latitude, longitude)
    # Predict the house price
    house_price_raw = predict_house_price(house_data)
    # Process house price
    house_price = process_house_price(house_price_raw)
    # Display the predicted house price
    result_label.config(text=f'${house_price:,}')


# Create the main window.
window = tk.Tk()
window.title("House Price Predictor")

# Create frame
base_frame = tk.Frame(window)
base_frame.pack()

# Create title label
title_label = tk.Label(base_frame, text="Melbourne House Price Predictor (2016 - 2017)", font="Arial 20 bold")
title_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky='WENS')

# Create primary information input frame
info_frame_1 = tk.LabelFrame(base_frame, text="Primary Information Input")
info_frame_1.grid(row=1, column=0, padx=20, pady=(20, 10), sticky='W')

# Rooms label
rooms_label = tk.Label(info_frame_1, text="Rooms")
rooms_label.grid(row=0, column=0)
# Rooms entry
rooms_entry = tk.Entry(info_frame_1)
rooms_entry.grid(row=1, column=0)

# Bedrooms label
bedrooms_label = tk.Label(info_frame_1, text="Bedrooms")
bedrooms_label.grid(row=0, column=1)
# Bedrooms entry
bedrooms_entry = tk.Entry(info_frame_1)
bedrooms_entry.grid(row=1, column=1)

# Bathrooms label
bathrooms_label = tk.Label(info_frame_1, text="Bathrooms")
bathrooms_label.grid(row=0, column=2)
# Bathrooms entry
bathrooms_entry = tk.Entry(info_frame_1)
bathrooms_entry.grid(row=1, column=2)

# Carports label
carports_label = tk.Label(info_frame_1, text="Carports")
carports_label.grid(row=0, column=3)
# Carports entry
carports_entry = tk.Entry(info_frame_1)
carports_entry.grid(row=1, column=3)

# Create secondary information input frame
info_frame_2 = tk.LabelFrame(base_frame, text="Secondary Information Input")
info_frame_2.grid(row=2, column=0, padx=20, pady=(10, 20), sticky='W')

# Land size label
land_label = tk.Label(info_frame_2, text="Land Size")
land_label.grid(row=0, column=0)
# land size entry
land_entry = tk.Entry(info_frame_2)
land_entry.grid(row=1, column=0)

# Building area label
building_label = tk.Label(info_frame_2, text="Building Area")
building_label.grid(row=0, column=1)
# Building area entry
building_entry = tk.Entry(info_frame_2)
building_entry.grid(row=1, column=1)

# Latitude label
latitude_label = tk.Label(info_frame_2, text="Latitude")
latitude_label.grid(row=0, column=2)
# Latitude scale
latitude_scale = tk.Scale(info_frame_2, length=119, showvalue=False, from_=-381826, to=-374085, orient='horizontal', command=custom_slider_value_display)
latitude_scale.grid(row=1, column=2,)
latitude_scale.set(-381826)
# Latitude result label
latitude_result_label = tk.Label(info_frame_2, text="-37.4085")
latitude_result_label.grid(row=2, column=2)

# Longitude label
longitude_label = tk.Label(info_frame_2, text="Longitude")
longitude_label.grid(row=0, column=3)
# Longitude scale
longitude_scale = tk.Scale(info_frame_2, length=119, showvalue=False, from_=14443181, to=14552635, orient='horizontal', command=custom_slider_value_display)
longitude_scale.grid(row=1, column=3,)
# Longitude result label
longitude_result_label = tk.Label(info_frame_2, text="144.43181")
longitude_result_label.grid(row=2, column=3)

# Create tertiary information input frame
info_frame_3 = tk.LabelFrame(base_frame, text="House Price Prediction Output")
info_frame_3.grid(row=3, column=0, padx=20, pady=(10, 20), sticky='W')

# Padding labels (ignore)
padding_label1 = tk.Label(info_frame_3, text="", width=24)
padding_label1.grid(row=0, column=0)
padding_label2 = tk.Label(info_frame_3, text="", width=24)
padding_label2.grid(row=0, column=1)
padding_label3 = tk.Label(info_frame_3, text="", width=24)
padding_label3.grid(row=0, column=2)

# Enter info button
predict_button = tk.Button(info_frame_3, text="Predict House Price", command=enter_info_and_display_price)
predict_button.grid(row=1, column=0, sticky="WENS")

# Result label
result_label = tk.Label(info_frame_3, text="")
result_label.grid(row=1, column=1, sticky="WENS")

# Quit button
quit_button = tk.Button(info_frame_3, text="Quit", command=window.destroy)
quit_button.grid(row=1, column=2, sticky="WENS")

# Accuracy label
accuracy_label = tk.Label(base_frame, text="This model predicts Melbourne house prices (2016 - 2017) with an accuracy of 82%")
accuracy_label.grid(row=4, column=0, padx=20, pady=(1, 20), sticky="W")

# Pad GUI elements
for widget in info_frame_1.winfo_children():
    widget.grid_configure(padx=10, pady=5)

for widget in info_frame_2.winfo_children():
    widget.grid_configure(padx=10, pady=5)

for widget in info_frame_3.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Enter the tkinter main loop.
tk.mainloop()
