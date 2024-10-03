import tkinter as tk
from tkinter import colorchooser, filedialog, simpledialog, messagebox, font
import random
from PIL import Image, ImageTk, ImageDraw


class BotDessinateur:
    def __init__(self, root):
        self.root = root
        self.root.title("Bot Dessinateur Avancé")
        self.root.geometry("1200x900")

        # Créer un canvas pour dessiner
        self.canvas = tk.Canvas(self.root, width=900, height=600, bg="white", borderwidth=2, relief="solid")
        self.canvas.pack(pady=20)

        # Cadre pour les boutons et options
        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack(pady=10)

        # Menu
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Fichier", menu=self.file_menu)
        self.file_menu.add_command(label="Enregistrer Dessin", command=self.enregistrer_dessin)
        self.file_menu.add_command(label="Charger Dessin", command=self.charger_dessin)
        self.file_menu.add_command(label="Quitter", command=self.root.quit)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Édition", menu=self.edit_menu)
        self.edit_menu.add_command(label="Annuler Dernière Forme", command=self.annuler_dernier_forme)
        self.edit_menu.add_command(label="Refaire Dernière Forme", command=self.refaire_dernier_forme)

        # Boutons de contrôle
        self.bouton_dessiner = tk.Button(self.controls_frame, text="Démarrer le Dessin",
                                         command=self.dessiner_automatiquement)
        self.bouton_dessiner.grid(row=0, column=0, padx=10)

        self.bouton_arreter = tk.Button(self.controls_frame, text="Arrêter le Dessin", command=self.arreter_dessin)
        self.bouton_arreter.grid(row=0, column=1, padx=10)

        self.bouton_effacer = tk.Button(self.controls_frame, text="Effacer la zone", command=self.effacer_zone)
        self.bouton_effacer.grid(row=0, column=2, padx=10)

        # Choix de la couleur des formes
        self.label_form_color = tk.Label(self.controls_frame, text="Couleur des formes :")
        self.label_form_color.grid(row=1, column=0, padx=10, pady=10)
        self.form_color = "#000000"  # Noir par défaut
        self.color_button = tk.Button(self.controls_frame, text="Choisir Couleur", command=self.choisir_couleur_forme)
        self.color_button.grid(row=1, column=1, padx=10)

        # Case à cocher pour couleurs aléatoires
        self.couleur_aleatoire = tk.BooleanVar(value=False)
        self.checkbox_couleur = tk.Checkbutton(self.controls_frame, text="Couleurs Aléatoires",
                                               variable=self.couleur_aleatoire)
        self.checkbox_couleur.grid(row=1, column=2, padx=10, pady=10)

        # Choix de la taille des formes
        self.label_taille = tk.Label(self.controls_frame, text="Taille des formes :")
        self.label_taille.grid(row=1, column=3, padx=10, pady=10)
        self.taille_slider = tk.Scale(self.controls_frame, from_=10, to_=200, orient=tk.HORIZONTAL, length=200)
        self.taille_slider.set(50)
        self.taille_slider.grid(row=1, column=4, padx=10)

        # Choix de la couleur de fond du canevas
        self.label_bg_color = tk.Label(self.controls_frame, text="Couleur de fond :")
        self.label_bg_color.grid(row=2, column=0, padx=10, pady=10)
        self.bg_color_var = tk.StringVar(value="white")
        self.bg_color_menu = tk.OptionMenu(self.controls_frame, self.bg_color_var, "white", "black", "lightblue",
                                           "lightgreen", "lightyellow", command=self.changer_couleur_fond)
        self.bg_color_menu.grid(row=2, column=1, padx=10)

        # Slider pour ajuster la vitesse de dessin
        self.label_vitesse = tk.Label(self.controls_frame, text="Vitesse du dessin :")
        self.label_vitesse.grid(row=2, column=2, padx=10, pady=10)
        self.vitesse_slider = tk.Scale(self.controls_frame, from_=50, to_=1000, orient=tk.HORIZONTAL, length=200)
        self.vitesse_slider.set(100)
        self.vitesse_slider.grid(row=2, column=3, padx=10)

        # Boutons pour ajouter des formes manuellement
        self.bouton_ajouter_ovale = tk.Button(self.controls_frame, text="Ajouter Cercle",
                                              command=lambda: self.ajouter_forme("cercle"))
        self.bouton_ajouter_ovale.grid(row=3, column=0, padx=10, pady=10)

        self.bouton_ajouter_rectangle = tk.Button(self.controls_frame, text="Ajouter Carré",
                                                  command=lambda: self.ajouter_forme("carre"))
        self.bouton_ajouter_rectangle.grid(row=3, column=1, padx=10, pady=10)

        self.bouton_ajouter_ligne = tk.Button(self.controls_frame, text="Ajouter Ligne Droite",
                                              command=lambda: self.ajouter_forme("ligne_droite"))
        self.bouton_ajouter_ligne.grid(row=3, column=2, padx=10, pady=10)

        self.bouton_ajouter_triangle = tk.Button(self.controls_frame, text="Ajouter Triangle",
                                                 command=lambda: self.ajouter_forme("triangle"))
        self.bouton_ajouter_triangle.grid(row=4, column=0, padx=10, pady=10)

        self.bouton_ajouter_etoile = tk.Button(self.controls_frame, text="Ajouter Étoile",
                                               command=lambda: self.ajouter_forme("etoile"))
        self.bouton_ajouter_etoile.grid(row=4, column=1, padx=10, pady=10)

        # Bouton pour ajouter du texte
        self.bouton_ajouter_texte = tk.Button(self.controls_frame, text="Ajouter Texte", command=self.ajouter_texte)
        self.bouton_ajouter_texte.grid(row=4, column=2, padx=10, pady=10)

        # Options pour la police du texte
        self.label_font = tk.Label(self.controls_frame, text="Police du texte :")
        self.label_font.grid(row=5, column=0, padx=10, pady=10)
        self.font_var = tk.StringVar(value="Helvetica")
        self.font_menu = tk.OptionMenu(self.controls_frame, self.font_var, "Helvetica", "Arial", "Times New Roman",
                                       "Courier New")
        self.font_menu.grid(row=5, column=1, padx=10)

        # Options pour l'épaisseur des lignes
        self.label_line_width = tk.Label(self.controls_frame, text="Épaisseur des lignes :")
        self.label_line_width.grid(row=5, column=2, padx=10, pady=10)
        self.line_width_slider = tk.Scale(self.controls_frame, from_=1, to_=10, orient=tk.HORIZONTAL, length=200)
        self.line_width_slider.set(1)
        self.line_width_slider.grid(row=5, column=3, padx=10)

        # Option pour les motifs de remplissage
        self.label_pattern = tk.Label(self.controls_frame, text="Motif de remplissage :")
        self.label_pattern.grid(row=6, column=0, padx=10, pady=10)
        self.pattern_var = tk.StringVar(value="none")
        self.pattern_menu = tk.OptionMenu(self.controls_frame, self.pattern_var, "none", "diagonal", "cross", "dot")
        self.pattern_menu.grid(row=6, column=1, padx=10)

        # Boutons pour annuler et refaire
        self.bouton_annuler = tk.Button(self.controls_frame, text="Annuler", command=self.annuler_dernier_forme)
        self.bouton_annuler.grid(row=6, column=2, padx=10, pady=10)

        self.bouton_refaire = tk.Button(self.controls_frame, text="Refaire", command=self.refaire_dernier_forme)
        self.bouton_refaire.grid(row=6, column=3, padx=10, pady=10)

        # Activer/Désactiver le mode aléatoire
        self.mode_aleatoire = tk.BooleanVar(value=True)
        self.checkbox_mode = tk.Checkbutton(self.controls_frame, text="Mode Aléatoire", variable=self.mode_aleatoire)
        self.checkbox_mode.grid(row=7, column=0, padx=10, pady=10)

        # Drapeau pour contrôler le dessin
        self.dessin_en_cours = False
        self.historique_formes = []
        self.index_historique = -1

    def dessiner_automatiquement(self):
        self.dessin_en_cours = True
        self.dessiner()

    def dessiner(self):
        if self.dessin_en_cours:
            if self.mode_aleatoire.get():
                forme = random.choice(["cercle", "carre", "ligne_droite", "triangle", "etoile"])
                self.ajouter_forme(forme)
            self.root.after(self.vitesse_slider.get(), self.dessiner)

    def arreter_dessin(self):
        self.dessin_en_cours = False

    def effacer_zone(self):
        self.canvas.delete("all")
        self.historique_formes.clear()
        self.index_historique = -1

    def changer_couleur_fond(self, couleur):
        self.canvas.configure(bg=couleur)

    def choisir_couleur_forme(self):
        couleur = colorchooser.askcolor()[1]
        if couleur:
            self.form_color = couleur

    def ajouter_forme(self, forme):
        # Utiliser une couleur aléatoire si la case est cochée
        couleur = self.form_color if not self.couleur_aleatoire.get() else random.choice(
            ["red", "green", "blue", "yellow", "purple", "orange"])
        taille = self.taille_slider.get()
        epaisseur = self.line_width_slider.get()
        motif = self.pattern_var.get()

        x1 = random.randint(0, 900 - taille)
        y1 = random.randint(0, 600 - taille)
        x2 = x1 + taille
        y2 = y1 + taille

        # Appliquer le motif de remplissage si nécessaire
        if motif != "none":
            fill = self.canvas.create_image(x1, y1, anchor="nw", image=self.create_pattern_image(motif, taille))
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="", stipple=motif)
        else:
            fill = couleur

        if forme == "cercle":
            id_forme = self.canvas.create_oval(x1, y1, x2, y2, fill=fill, outline="", width=epaisseur)
        elif forme == "carre":
            id_forme = self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline="", width=epaisseur)
        elif forme == "ligne_droite":
            id_forme = self.canvas.create_line(x1, y1, x2, y2, fill=couleur, width=epaisseur)
        elif forme == "triangle":
            id_forme = self.canvas.create_polygon(x1, y1, x2, y1, (x1 + x2) / 2, y2, fill=couleur, outline="",
                                                  width=epaisseur)
        elif forme == "etoile":
            points = [x1 + taille / 2, y1, x1 + taille * 0.62, y1 + taille * 0.38, x1 + taille, y1 + taille * 0.38,
                      x1 + taille * 0.69, y1 + taille * 0.62, x1 + taille * 0.81, y1 + taille, x1 + taille / 2,
                      y1 + taille * 0.69, x1 + taille * 0.19, y1 + taille, x1 + taille * 0.31, y1 + taille * 0.62,
                      x1, y1 + taille * 0.38, x1 + taille * 0.38, y1 + taille * 0.38]
            id_forme = self.canvas.create_polygon(points, fill=couleur, outline="", width=epaisseur)

        self.historique_formes.append((forme, id_forme))
        self.index_historique += 1

    def ajouter_texte(self):
        texte = simpledialog.askstring("Texte", "Entrez le texte à ajouter :")
        if texte:
            x = random.randint(0, 900)
            y = random.randint(0, 600)
            couleur = self.form_color if not self.couleur_aleatoire.get() else random.choice(
                ["red", "green", "blue", "yellow", "purple", "orange"])
            selected_font = self.font_var.get()
            self.canvas.create_text(x, y, text=texte, fill=couleur, font=(selected_font, 16))

    def enregistrer_dessin(self):
        fichier = filedialog.asksaveasfilename(defaultextension=".png",
                                               filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),
                                                          ("PostScript files", "*.ps"), ("All files", "*.*")])
        if fichier:
            self.canvas.update()  # Assurez-vous que tout est dessiné avant d'enregistrer
            ps_file = "temp.ps"
            self.canvas.postscript(file=ps_file)
            image = Image.open(ps_file)
            image.save(fichier)

    def charger_dessin(self):
        fichier = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.ps"), ("All files", "*.*")])
        if fichier:
            self.canvas.delete("all")
            image = Image.open(fichier)
            self.canvas.image = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.canvas.image)

    def annuler_dernier_forme(self):
        if self.index_historique >= 0:
            forme, id_forme = self.historique_formes[self.index_historique]
            self.canvas.delete(id_forme)
            del self.historique_formes[self.index_historique]
            self.index_historique -= 1
        else:
            messagebox.showinfo("Annuler", "Aucune forme à annuler.")

    def refaire_dernier_forme(self):
        if self.index_historique + 1 < len(self.historique_formes):
            self.index_historique += 1
            forme, id_forme = self.historique_formes[self.index_historique]
            self.ajouter_forme(forme)
        else:
            messagebox.showinfo("Refaire", "Aucune forme à refaire.")

    def create_pattern_image(self, pattern, size):
        # Create a temporary image with the pattern
        image = Image.new("1", (size, size), 1)
        draw = ImageDraw.Draw(image)
        if pattern == "diagonal":
            draw.line([(0, 0), (size, size)], fill=0)
            draw.line([(0, size), (size, 0)], fill=0)
        elif pattern == "cross":
            draw.line([(0, size / 2), (size, size / 2)], fill=0)
            draw.line([(size / 2, 0), (size / 2, size)], fill=0)
        elif pattern == "dot":
            draw.ellipse([(size / 2 - 5, size / 2 - 5), (size / 2 + 5, size / 2 + 5)], fill=0)
        return ImageTk.PhotoImage(image)


if __name__ == "__main__":
    root = tk.Tk()
    bot = BotDessinateur(root)
    root.mainloop()
