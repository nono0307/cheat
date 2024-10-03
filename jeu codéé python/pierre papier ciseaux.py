import random


def pierre_papier_ciseaux():
    options = ["pierre", "papier", "ciseaux"]
    print("Bienvenue au jeu Pierre-Papier-Ciseaux !")

    while True:
        utilisateur = input("Choisissez pierre, papier ou ciseaux (ou 'quitter' pour arrêter) : ").lower()
        if utilisateur == 'quitter':
            print("Merci d'avoir joué !")
            break

        if utilisateur not in options:
            print("Choix invalide, essayez encore.")
            continue

        ordinateur = random.choice(options)
        print(f"L'ordinateur choisit : {ordinateur}")

        if utilisateur == ordinateur:
            print("Égalité !")
        elif (utilisateur == "pierre" and ordinateur == "ciseaux") or \
                (utilisateur == "papier" and ordinateur == "pierre") or \
                (utilisateur == "ciseaux" and ordinateur == "papier"):
            print("Vous gagnez !")
        else:
            print("Vous perdez !")


if __name__ == "__main__":
    pierre_papier_ciseaux()
