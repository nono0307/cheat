import tkinter as tk
from tkinter import messagebox
import os
import subprocess
from datetime import datetime


def open_subject(subject):
    # Définir les chemins des répertoires en fonction de la matière
    base_path = r"C:\Users\dewez\Documents\Matiére"
    directories = {
        "Mathématiques": os.path.join(base_path, "Mathématiques"),
        "Physique": os.path.join(base_path, "Physique"),
        "Histoire": os.path.join(base_path, "Histoire Géo"),
        "Anglais": os.path.join(base_path, "Anglais"),
        "Français": os.path.join(base_path, "Français"),
        "Sciences": os.path.join(base_path, "Sciences"),
        "Musique": os.path.join(base_path, "Musique"),
        "Arts": os.path.join(base_path, "Arts"),
        "Informatique": os.path.join(base_path, "Informatique")
    }

    directory = directories.get(subject)

    if directory and os.path.isdir(directory):
        try:
            # Ouvrir le répertoire avec l'explorateur de fichiers
            if os.name == 'nt':  # Pour Windows
                os.startfile(directory)
            elif os.name == 'posix':  # Pour Linux/Mac
                subprocess.run(['xdg-open', directory], check=True)
            else:
                messagebox.showerror("Erreur", "Système d'exploitation non supporté pour l'ouverture de répertoires.")
        except PermissionError:
            messagebox.showerror("Erreur", f"Permission refusée pour accéder au répertoire : {directory}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")
    else:
        messagebox.showerror("Erreur", "Le répertoire pour la matière sélectionnée n'existe pas.")


def update_date_label():
    # Mettre à jour le label avec la date actuelle
    current_date = datetime.now().strftime("%d/%m/%Y")
    date_label.config(text=f"Nous sommes le {current_date}")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Remember")
root.geometry("400x600")  # Augmenter la taille pour plus de boutons

# Titre principal
title_frame = tk.Frame(root)
title_frame.pack(pady=10)

title_label = tk.Label(title_frame, text="Remember", font=("Arial", 24, "bold"))
title_label.pack()

subtitle_label = tk.Label(title_frame, text="Rewritten by @plokzy", font=("Arial", 10))
subtitle_label.pack()

# Date actuelle
date_label = tk.Label(root, text="", font=("Arial", 10))
date_label.pack(pady=10)
update_date_label()  # Initialiser le label de date

# Boutons pour les matières
buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=10)

# Liste des matières et icônes
subjects = ["Mathématiques", "Physique", "Histoire", "Anglais", "Français", "Sciences", "Musique", "Arts",
            "Informatique"]
icons = ["📊", "🔬", "📚", "🇬🇧", "📖", "🔬", "🎵", "🎨", "💻"]

for i, subject in enumerate(subjects):
    button = tk.Button(
        buttons_frame,
        text=f"{icons[i]} {subject}",
        font=("Arial", 14),
        width=20,
        command=lambda s=subject: open_subject(s)
    )
    button.pack(pady=5)

# Boucle principale
root.mainloop()
