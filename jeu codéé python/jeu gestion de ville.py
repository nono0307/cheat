import random


class Ville:
    def __init__(self, nom):
        self.nom = nom
        self.population = 100
        self.nourriture = 100
        self.ressources = 100
        self.bâtiments = {
            "fermes": 1,
            "mines": 1,
            "maisons": 10
        }
        self.tour = 0

    def état_de_la_ville(self):
        print(f"\n--- {self.nom} ---")
        print(f"Tour: {self.tour}")
        print(f"Population: {self.population}")
        print(f"Nourriture: {self.nourriture}")
        print(f"Ressources: {self.ressources}")
        print(f"Bâtiments: {self.bâtiments}")

    def construire(self, bâtiment):
        if bâtiment == "ferme":
            coût = 20
            if self.ressources >= coût:
                self.ressources -= coût
                self.bâtiments["fermes"] += 1
                print("Une nouvelle ferme a été construite.")
            else:
                print("Pas assez de ressources pour construire une ferme.")

        elif bâtiment == "mine":
            coût = 30
            if self.ressources >= coût:
                self.ressources -= coût
                self.bâtiments["mines"] += 1
                print("Une nouvelle mine a été construite.")
            else:
                print("Pas assez de ressources pour construire une mine.")

        elif bâtiment == "maison":
            coût = 10
            if self.ressources >= coût:
                self.ressources -= coût
                self.bâtiments["maisons"] += 1
                print("Une nouvelle maison a été construite.")
            else:
                print("Pas assez de ressources pour construire une maison.")
        else:
            print("Bâtiment inconnu.")

    def passer_tour(self):
        self.tour += 1
        # Production de nourriture
        production_nourriture = self.bâtiments["fermes"] * 10
        self.nourriture += production_nourriture
        print(f"Les fermes ont produit {production_nourriture} unités de nourriture.")

        # Production de ressources
        production_ressources = self.bâtiments["mines"] * 15
        self.ressources += production_ressources
        print(f"Les mines ont produit {production_ressources} unités de ressources.")

        # Consommation de nourriture par la population
        consommation_nourriture = self.population * 2
        self.nourriture -= consommation_nourriture
        print(f"La population a consommé {consommation_nourriture} unités de nourriture.")

        # Croissance de la population
        nouvelles_naissances = random.randint(0, 5)
        self.population += nouvelles_naissances
        print(f"{nouvelles_naissances} nouvelles personnes ont rejoint la ville.")

        # Vérification de la faim
        if self.nourriture < 0:
            famine = min(self.population, abs(self.nourriture) // 2)
            self.population -= famine
            self.nourriture = 0
            print(f"Famine! {famine} personnes sont mortes.")

    def jouer(self):
        while True:
            self.état_de_la_ville()
            action = input("Que voulez-vous faire ? (construire/passer/quitter) ").lower()
            if action == "construire":
                bâtiment = input("Quel bâtiment voulez-vous construire ? (ferme/mine/maison) ").lower()
                self.construire(bâtiment)
            elif action == "passer":
                self.passer_tour()
            elif action == "quitter":
                print("Merci d'avoir joué !")
                break
            else:
                print("Action non reconnue.")


if __name__ == "__main__":
    nom_de_ville = input("Entrez le nom de votre ville : ")
    ville = Ville(nom_de_ville)
    ville.jouer()
