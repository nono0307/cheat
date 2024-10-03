import tkinter as tk
from tkinter import ttk

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Combien vaut ton prénom ?")
        self.root.geometry("800x600")

        # Champ de texte pour entrer un prénom
        self.entry_prenom = tk.Entry(self.root, font=("Helvetica", 24), justify="center")
        self.entry_prenom.grid(row=0, column=1, padx=20, pady=20)
        self.entry_prenom.bind("<Return>", self.calculer_valeur)  # Lier la touche "Entrée" à l'ajout du prénom

        # Bouton pour calculer la valeur du prénom
        self.bouton_calculer = tk.Button(self.root, text="+", font=("Helvetica", 18), command=self.calculer_valeur)
        self.bouton_calculer.grid(row=0, column=2, padx=10)

        # Label pour afficher la valeur du prénom
        self.label_valeur = tk.Label(self.root, text="0 €", font=("Helvetica", 20), fg="green")
        self.label_valeur.grid(row=1, column=1, columnspan=2, pady=10)

        # Création du tableau pour le classement
        self.tree = ttk.Treeview(self.root, columns=("rang", "prenom", "prix"), show="headings", height=10)
        self.tree.heading("rang", text="Rang")
        self.tree.heading("prenom", text="Prénom")
        self.tree.heading("prix", text="Prix (€)")
        self.tree.column("rang", width=50, anchor="center")
        self.tree.column("prenom", width=250, anchor="center")
        self.tree.column("prix", width=200, anchor="center")
        self.tree.grid(row=2, column=0, columnspan=3, padx=20, pady=20)

        # Bouton pour démarrer une nouvelle manche
        self.bouton_nouvelle_manche = tk.Button(self.root, text="Nouvelle manche", font=("Helvetica", 16), command=self.nouvelle_manche)
        self.bouton_nouvelle_manche.grid(row=3, column=1, columnspan=2, pady=10)

        # Liste pour stocker les prénoms et valeurs
        self.utilisateurs = []

    def calculer_valeur(self, event=None):  # Ajout d'un paramètre par défaut pour l'événement
        prenom = self.entry_prenom.get().strip().capitalize()

        if not prenom:
            return

        # Facteur ajusté pour atteindre une valeur maximale de 1 000 000 €
        FACTEUR = 3846.15
        valeur = sum(ord(char) - 64 for char in prenom.upper() if 'A' <= char <= 'Z') * FACTEUR

        # Afficher la valeur sous le champ de texte
        self.label_valeur.config(text=f"{int(valeur):,} €")

        # Ajouter le prénom et la valeur à la liste
        self.utilisateurs.append((prenom, int(valeur)))

        # Trier la liste des utilisateurs par valeur décroissante
        self.utilisateurs.sort(key=lambda x: x[1], reverse=True)

        # Mettre à jour le classement
        self.mettre_a_jour_classement()

        # Effacer le texte après le calcul
        self.entry_prenom.delete(0, tk.END)

    def mettre_a_jour_classement(self):
        # Vider le tableau avant de le remplir à nouveau
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Remplir le tableau avec les utilisateurs triés
        for idx, (prenom, valeur) in enumerate(self.utilisateurs, start=1):
            self.tree.insert("", "end", values=(idx, prenom, f"{valeur:,} €"))

    def nouvelle_manche(self):
        # Réinitialiser le jeu
        self.utilisateurs = []
        self.entry_prenom.delete(0, tk.END)
        self.label_valeur.config(text="0 €")
        self.mettre_a_jour_classement()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
