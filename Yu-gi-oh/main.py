import tkinter as tk
import requests
from bs4 import BeautifulSoup

class YugiohCardList:
    def __init__(self, master):
        self.master = master
        self.master.title("Liste des cartes Yu-Gi-Oh!")
        self.master.geometry("500x400")

        # Création de la zone de liste
        self.card_listbox = tk.Listbox(self.master, width=50)
        self.card_listbox.pack(pady=10)

        # Création du bouton de tri par type de carte
        self.type_button = tk.Button(self.master, text="Trier par type de carte", command=self.sort_by_type)
        self.type_button.pack(pady=5)

        # Récupération des données de cartes depuis le site web
        self.card_data = []
        url = "https://db.ygoprodeck.com/search"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        cards = soup.find_all("div", class_="card-info")
        for card in cards:
            name = card.find("div", class_="card-name").text.strip()
            card_type = card.find("div", class_="card-type").text.strip()
            self.card_data.append((name, card_type))

        # Ajout des cartes à la zone de liste
        for card in self.card_data:
            self.card_listbox.insert(tk.END, f"{card[0]} - {card[1]}")

    def sort_by_type(self):
        # Tri des cartes par type de carte
        sorted_data = sorted(self.card_data, key=lambda x: x[1])
        self.card_listbox.delete(0, tk.END)
        for card in sorted_data:
            self.card_listbox.insert(tk.END, f"{card[0]} - {card[1]}")

root = tk.Tk()
app = YugiohCardList(root)
root.mainloop()
