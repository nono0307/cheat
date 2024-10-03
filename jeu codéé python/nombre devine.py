import random


def jeu_devine_nombre():
    print("Bienvenue au jeu de Devine le Nombre !")
    print("Je pense à un nombre entre 1 et 100.")

    # L'ordinateur choisit un nombre aléatoire entre 1 et 100
    nombre_secret = random.randint(1, 100)
    nombre_essais = 0
    trouve = False

    while not trouve:
        # Demande au joueur de faire une supposition
        try:
            supposition = int(input("Faites une supposition : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        nombre_essais += 1

        # Vérifie la supposition du joueur
        if supposition < nombre_secret:
            print("Trop bas ! Essayez encore.")
        elif supposition > nombre_secret:
            print("Trop haut ! Essayez encore.")
        else:
            trouve = True
            print(f"Félicitations ! Vous avez trouvé le nombre {nombre_secret} en {nombre_essais} essais.")


if __name__ == "__main__":
    jeu_devine_nombre()
