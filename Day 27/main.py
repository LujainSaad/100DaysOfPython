from tkinter import *


def calculate():
    miles = float(entry.get())
    km = miles * 1.609
    label4.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)  # Adding padding to the window


# Label
label1 = Label(text="Miles", font=("Arial", 15))
label1.grid(row=0, column=2)

label2 = Label(text="Km", font=("Arial", 15))
label2.grid(row=1, column=2)

label3 = Label(text="is equal to", font=("Arial", 15))
label3.grid(row=1, column=0)

label4 = Label(text="0", font=("Arial", 15))
label4.grid(row=1, column=1)

# Button
button = Button(text="Calculate", command=calculate)  # The function without ()
button.grid(row=2, column=1)


# Entry
entry = Entry(width=7)
entry.insert(END,"0")
entry.grid(row=0, column=1)

window.mainloop()  # To keep the window running
