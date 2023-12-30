# mile to km converter
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_in_km = Label(text="0")
result_in_km.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)


# Button
def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609
    result_in_km.config(text=f"{round(km, 3)}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
