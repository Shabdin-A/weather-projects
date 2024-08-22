import tkinter
from tkinter import messagebox, Tk, Label, Entry, Button
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def get_weather():
    try:
        city_field = textfield.get()
        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city_field)
        lat = location.latitude
        lng = location.longitude
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=lng, lat=lat)
        city.config(text=result.split("/")[1])

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text="LOCAL TIME")

        api_key="enter your api key"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"
        json_data = requests.get(api).json()
        condition_data = json_data["weather"][0]["main"]
        description_data = json_data["weather"][0]["description"]
        temp_data = int(json_data["main"]["temp"] - 273.15)
        pressure_data = json_data["main"]["pressure"]
        humidity_data = json_data["main"]["humidity"]
        wind_data = json_data["wind"]["speed"]

        temp.config(text=f"{temp_data} °")
        condition.config(text=f"{condition_data} | FEELS LIKE {temp} °")
        wind.config(text=wind_data)
        humidity.config(text=humidity_data)
        description.config(text=description_data)
        pressure.config(text=pressure_data)



    except Exception as error:
        print(error)
        messagebox.showerror("Weather App", "Invalid Entry!")


window = Tk()
window.title("Weather App")
window.geometry("900x500+300+200")
window.resizable(False, False)

search_box = tkinter.PhotoImage(file="image/search.png")
search_box_label = tkinter.Label(window, image=search_box)
search_box_label.pack(pady=20, side=tkinter.TOP)
textfield = tkinter.Entry(window, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", fg="white",
                          border=0)
textfield.place(x=300, y=40)

search = tkinter.PhotoImage(file="image/search_icon.png")
search_button = tkinter.Button(window, image=search, border=0, cursor="hand2", bg="#404040", command=get_weather)
search_button.place(x=590, y=34)

logo = tkinter.PhotoImage(file="image/logo.png")
logo_label = tkinter.Label(window, image=logo)
logo_label.pack(side=tkinter.TOP)

frame = tkinter.PhotoImage(file="image/box.png")
frame_label = tkinter.Label(window, image=frame)
frame_label.pack(pady=10, side=tkinter.BOTTOM)

city = tkinter.Label(window, font=("arial", 30, "bold"), fg="#e355cd")
city.place(x=120, y=160)

time = tkinter.Label(window, font=("arial", 20, "bold"), fg="#4b4bcc")
time.place(x=120, y=230)

clock = tkinter.Label(window, font=("Helvetica", 20, "bold"), fg="#4b4bcc")
clock.place(x=120, y=270)

label1_frame = tkinter.Label(window, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1_frame.place(x=120, y=400)

label2_frame = tkinter.Label(window, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2_frame.place(x=280, y=400)

label3_frame = tkinter.Label(window, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3_frame.place(x=450, y=400)

label4_frame = tkinter.Label(window, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4_frame.place(x=670, y=400)

temp = tkinter.Label(window, font=("arial", 60, "bold"), fg="#e355cd")
temp.place(x=590, y=170)

condition = tkinter.Label(window, font=("arial", 15, "bold"), fg="#4b4bcc")
condition.place(x=590, y=270)

wind = tkinter.Label(window, text="...", font=("arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
wind.place(x=120, y=430)

humidity = tkinter.Label(window, text="...", font=("arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
humidity.place(x=280, y=430)

description = tkinter.Label(window, text="...", font=("arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
description.place(x=450, y=430)

pressure = tkinter.Label(window, text="...", font=("arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
pressure.place(x=670, y=430)

window.mainloop()
