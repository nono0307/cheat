import time
import random


def jeu_reactions():
    print("Bienvenue au Jeu de Réactions !")
    input("Appuyez sur Enter pour commencer.")

    temps_attente = random.randint(1, 5)
    time.sleep(temps_attente)

    start_time = time.time()
    input("Appuyez sur Enter dès que vous voyez ce message !")
    reaction_time = time.time() - start_time

    print(f"Votre temps de réaction est de {reaction_time:.2f} secondes.")


if __name__ == "__main__":
    jeu_reactions()
