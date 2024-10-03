import random
import time


def simon():
    couleurs = ["Rouge", "Vert", "Bleu", "Jaune"]
    séquence = []

    print("Bienvenue au jeu de Simon !")

    while True:
        séquence.append(random.choice(couleurs))
        print("Séquence : ", " ".join(séquence))
        time.sleep(2)
        print("\033c", end="")  # Efface l'écran

        for couleur in séquence:
            réponse = input(f"Quelle couleur était après {couleur} ? ").capitalize()
            if réponse != couleur:
                print("Mauvaise réponse. Vous avez perdu.")
                return
        print("Bonne réponse ! Continuez.")


if __name__ == "__main__":
    simon()
