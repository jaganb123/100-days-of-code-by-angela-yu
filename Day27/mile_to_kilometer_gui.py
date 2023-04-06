import tkinter

CONVERSION_VALUE = 1.609344
FONT = ("Airal", 12, "normal")

def mile_to_km(val):
    km = round(val * CONVERSION_VALUE, 2)
    return km


def update_label():
    km_lable.config(text=f"{mile_to_km(float(mile_entry.get()))}")


#creating tk window
window = tkinter.Tk()
window.title("Miles to KM Converter")
window.minsize(width=200, height=100)

#lable
miles = tkinter.Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)
km = tkinter.Label(text="Km", font=FONT)
km.grid(column=2, row=1)
km_lable = tkinter.Label(text="0", font=FONT, width=10)
km_lable.grid(column=1, row=1)
is_equal = tkinter.Label(text="is equal to", font=FONT, width=10)
is_equal.grid(column=0, row=1)

#entry
mile_entry = tkinter.Entry(width=10)
mile_entry.grid(column=1, row=0)

#Button
button = tkinter.Button(text="calculate", command=update_label)
button.grid(column=1, row=2)


window.mainloop()