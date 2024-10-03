import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import csv

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Combien vaut ton prénom ?")

        # Définir une taille de fenêtre plus petite
        self.taille_fenetre = "360x640"
        self.root.geometry(self.taille_fenetre)

        # Champ de texte pour entrer un prénom
        self.entry_prenom = tk.Entry(self.root, font=("Helvetica", 18), justify="center")
        self.entry_prenom.pack(padx=10, pady=10, fill=tk.X)
        self.entry_prenom.bind("<Return>", self.calculer_valeur)  # Lier la touche "Entrée" à l'ajout du prénom

        # Bouton pour calculer la valeur du prénom
        self.bouton_calculer = tk.Button(self.root, text="+", font=("Helvetica", 16), command=self.calculer_valeur)
        self.bouton_calculer.pack(padx=10, pady=5, fill=tk.X)

        # Label pour afficher la valeur du prénom
        self.label_valeur = tk.Label(self.root, text="0 €", font=("Helvetica", 16), fg="green")
        self.label_valeur.pack(padx=10, pady=10)

        # Création du tableau pour le classement
        self.tree = ttk.Treeview(self.root, columns=("rang", "prenom", "prix"), show="headings", height=10)
        self.tree.heading("rang", text="Rang")
        self.tree.heading("prenom", text="Prénom")
        self.tree.heading("prix", text="Prix (€)")
        self.tree.column("rang", width=60, anchor="center")
        self.tree.column("prenom", width=180, anchor="center")
        self.tree.column("prix", width=100, anchor="center")
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Ajouter un menu contextuel pour supprimer une ligne
        self.menu_contextuel = tk.Menu(self.root, tearoff=0)
        self.menu_contextuel.add_command(label="Supprimer", command=self.supprimer_element)

        # Lier le clic droit au menu contextuel
        self.tree.bind("<Button-3>", self.afficher_menu_contextuel)

        # Bouton pour démarrer une nouvelle manche
        self.bouton_nouvelle_manche = tk.Button(self.root, text="Nouvelle manche", font=("Helvetica", 14), command=self.nouvelle_manche)
        self.bouton_nouvelle_manche.pack(padx=10, pady=10, fill=tk.X)

        # Bouton pour enregistrer les données
        self.bouton_enregistrer = tk.Button(self.root, text="Enregistrer", font=("Helvetica", 14), command=self.enregistrer_donnees)
        self.bouton_enregistrer.pack(padx=10, pady=10, fill=tk.X)

        # Liste pour stocker les prénoms et valeurs
        self.utilisateurs = []

    def afficher_menu_contextuel(self, event):
        # Obtenir l'élément sélectionné sous le curseur
        item_id = self.tree.identify_row(event.y)
        if item_id:
            self.tree.selection_set(item_id)
            self.menu_contextuel.post(event.x_root, event.y_root)

    def supprimer_element(self):
        # Obtenir l'élément sélectionné
        selected_item = self.tree.selection()
        if not selected_item:
            return

        item_id = selected_item[0]
        values = self.tree.item(item_id, 'values')
        prenom = values[1]

        # Confirmer la suppression
        if messagebox.askokcancel("Confirmer la suppression", f"Êtes-vous sûr de vouloir supprimer {prenom}?"):
            # Supprimer l'élément de la liste et du tableau
            self.utilisateurs = [u for u in self.utilisateurs if u[0] != prenom]
            self.tree.delete(item_id)
            self.mettre_a_jour_classement()

    def calculer_valeur(self, event=None):
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

    def enregistrer_donnees(self):
        # Demander à l'utilisateur où enregistrer le fichier
        fichier = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichiers CSV", "*.csv")])
        if not fichier:
            return

        # Écrire les données dans le fichier CSV
        try:
            with open(fichier, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Rang", "Prénom", "Prix (€)"])  # En-têtes de colonnes
                for idx, (prenom, valeur) in enumerate(self.utilisateurs, start=1):
                    writer.writerow([idx, prenom, f"{valeur:,} €"])
            messagebox.showinfo("Succès", "Les données ont été enregistrées avec succès.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue lors de l'enregistrement des données : {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
