from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    output.config(text=f"{km}")

input = Entry(width=7)
input.insert(0, "0")
input.grid(column=2, row=1)

label = Label(text="Miles")
label.grid(column=3, row=1)

label2 = Label(text="is equal to")
label2.grid(column=1, row=2)

output = Label(text="0")
output.grid(column=2, row=2)

label3 = Label(text="Kilometers")
label3.grid(column=3, row=2)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)

window.mainloop()