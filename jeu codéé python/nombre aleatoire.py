import random


def generateur_nombre_aleatoire(minimum, maximum):
    return random.randint(minimum, maximum)


if __name__ == "__main__":
    print("Bienvenue dans le générateur de nombre aléatoire !")
    minimum = int(input("Entrez le nombre minimum : "))
    maximum = int(input("Entrez le nombre maximum : "))

    if minimum > maximum:
        print("Erreur : le minimum ne peut pas être supérieur au maximum.")
    else:
        nombre_aleatoire = generateur_nombre_aleatoire(minimum, maximum)
        print(f"Le nombre aléatoire généré est : {nombre_aleatoire}")

    input("Appuyez sur Entrée pour fermer le programme.")
