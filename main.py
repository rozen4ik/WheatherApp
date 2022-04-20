from weather_controller import *
from tkinter import *


def show_weather():
    label_weather.config(text=weather(message.get()))

root = Tk()
root.title("Приложение о погоде")
root.geometry("680x200+300+250")

label = Label(text="Введите название города, чтобы узнать погоду на сегодня", justify=LEFT, font="Arial 14")
label.grid(row=0, column=0, ipadx=10, ipady=6, padx=10, pady=10)

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.grid(row=0, column=1, ipadx=10, ipady=6, padx=10, pady=10)

message_button = Button(text="Узнать погоду", command=show_weather)
message_button.grid(row=1, column=1, ipadx=10, ipady=6, padx=10, pady=10)

label_weather = Label(text="", justify=LEFT, font="Arial 24")
label_weather.grid(row=1, column=0, ipadx=10, ipady=6, padx=10, pady=10)

root.mainloop()
