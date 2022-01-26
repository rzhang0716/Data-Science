import tkinter

window = tkinter.Tk()

window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


def button_clicked():
    new_text = float(first_entry.get()) * 1.6
    fourth_label.config(text=f"{new_text}")


# First Label
first_label = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
first_label.grid(row=0, column=2)

# Second Label
second_label = tkinter.Label(text="is equal to", font=("Arial", 24, "bold"))
second_label.grid(row=1, column=0)

# Third Label
third_label = tkinter.Label(text="Km", font=("Arial", 24, "bold"))
third_label.grid(row=1, column=2)

# Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

# Fourth Label
fourth_label = tkinter.Label(text="0", font=("Arial", 24, "bold"))
fourth_label.grid(row=1, column=1)

# First Entry
first_entry = tkinter.Entry(width=10)
first_entry.grid(row=0, column=1)

window.mainloop()
