import random


def pendu():
    mots = ["python", "ordinateur", "programmation", "jeu", "algorithme"]
    mot_secret = random.choice(mots).upper()
    lettres_devinees = set()
    tentatives_restantes = 6

    print("Bienvenue au jeu du Pendu !")

    while tentatives_restantes > 0:
        affichage = [lettre if lettre in lettres_devinees else "_" for lettre in mot_secret]
        print(" ".join(affichage))

        if "_" not in affichage:
            print("Félicitations ! Vous avez deviné le mot.")
            return

        lettre = input("Devinez une lettre : ").upper()

        if lettre in lettres_devinees:
            print("Vous avez déjà deviné cette lettre.")
            continue

        lettres_devinees.add(lettre)

        if lettre not in mot_secret:
            tentatives_restantes -= 1
            print(f"Lettre incorrecte. Tentatives restantes : {tentatives_restantes}")

    print(f"Désolé, vous avez perdu. Le mot secret était '{mot_secret}'.")


if __name__ == "__main__":
    pendu()
