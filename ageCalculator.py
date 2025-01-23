import tkinter as tk
from datetime import datetime
import time

def calculate_age_in_microseconds(birthdate):
    current_time = datetime.now()
    age = current_time - birthdate
    years = age.days // 365
    days = age.days % 365
    hours, remainder = divmod(age.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    microseconds = age.microseconds
    return years, days, hours, minutes, seconds, microseconds

def format_age(years, days, hours, minutes, seconds, microseconds):
    formatted_age = []
    if years > 0:
        formatted_age.append(f"{years} Years")
    if days > 0:
        formatted_age.append(f"{days} Days")
    if hours > 0:
        formatted_age.append(f"{hours} Hours")
    if minutes > 0:
        formatted_age.append(f"{minutes} Minutes")
    formatted_age.append(f"{seconds:02} Seconds")
    formatted_age.append(f"{microseconds:06} Microseconds")
    return ", ".join(formatted_age)

def update_age_label():
    years, days, hours, minutes, seconds, microseconds = calculate_age_in_microseconds(birthdate)
    age_label.config(text=f"I'm this old: {format_age(years, days, hours, minutes, seconds, microseconds)}")
    root.after(1, update_age_label)

birthdate_str = input("Zadajte svoj dátum narodenia (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

root = tk.Tk()
root.title("Time of suffering")
root.geometry("400x200")

age_label = tk.Label(root, text="", font=("Helvetica", 20), bg="white", fg="black")
age_label.pack(expand=True, fill="both")

update_age_label()

root.mainloop()
