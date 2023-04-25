from tkinter import *
from tkinter import ttk
from multi_cells import *
from country_box import *
from feet_to_meters import *
from temperature_convert import *

class App:
    def __init__(self, master):
        self.master = master
        master.title("Menu")


        # Ajout d'une étiquette de titre
        ttk.Label(master, text="Sélectionnez une fonctionnalité", font=("TkDefaultFont", 16)).grid(column=0, row=0, pady=20)

        # Création d'un conteneur pour les boutons
        self.button_frame = ttk.Frame(master)
        self.button_frame.grid(column=0, row=1, sticky=(N, S, E, W), padx=50, pady=20)

        # Ajout des boutons
        ttk.Button(self.button_frame, text="Feet to meters", command=self.open_feet_to_meters).grid(column=0, row=0, pady=10)
        ttk.Button(self.button_frame, text="Temperature convert", command=self.open_temperature_convert).grid(column=0, row=1, pady=10)
        ttk.Button(self.button_frame, text="Country box", command=self.open_country_box).grid(column=0, row=2, pady=10)
        ttk.Button(self.button_frame, text="Multi cells", command=self.open_multi_cells).grid(column=0, row=3, pady=10)

        # Ajout d'un bouton "Quitter"
        ttk.Button(master, text="Quitter", command=master.quit).grid(column=0, row=2, pady=10)

        # Étirer la rangée 0 pour remplir l'espace disponible
        master.grid_rowconfigure(0, weight=1)

        # Ajuster l'apparence des boutons
        for child in self.button_frame.winfo_children():
            child.config(width=25)

    def open_multi_cells(self):
        multi_cells()

    def open_temperature_convert(self):
        temperature_convert()
    
    def open_country_box(self):
        country_box()    

    def open_feet_to_meters(self):
        feet_to_meters()

root = Tk()
app = App(root)
root.mainloop()
