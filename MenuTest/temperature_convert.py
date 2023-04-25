from tkinter import *
from tkinter import ttk

def temperature_convert():
    root = Tk()
    root.withdraw()
    temp_window = Toplevel(root)
    temp_window.title("Temperature Converter")

    def convert(*args):
        try:
            value = float(fahrenheit.get())
            celsius.set(int((value - 32) * 5/9 * 100.0 + 0.5)/100.0)
        except ValueError:
            pass

    def back():
        temp_window.destroy()
        root.deiconify()

    mainframe = ttk.Frame(temp_window, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    temp_window.columnconfigure(0, weight=1)
    temp_window.rowconfigure(0, weight=1)

    fahrenheit = StringVar()
    fahrenheit_entry = ttk.Entry(mainframe, width=7, textvariable=fahrenheit)
    fahrenheit_entry.grid(column=2, row=1, sticky=(W, E))

    celsius = StringVar()
    ttk.Label(mainframe, textvariable=celsius).grid(column=2, row=2, sticky=(W, E))

    ttk.Button(mainframe, text="Convert", command=convert).grid(column=3, row=3, sticky=W)

    ttk.Label(mainframe, text="Fahrenheit").grid(column=3, row=1, sticky=W)
    ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
    ttk.Label(mainframe, text="Celsius").grid(column=3, row=2, sticky=W)

    ttk.Button(mainframe, text="Back", command=back).grid(column=3, row=4, sticky=W)

    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    fahrenheit_entry.focus()
    temp_window.bind("<Return>", convert)
