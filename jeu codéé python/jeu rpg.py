import random


class Personnage:
    def __init__(self, nom, vie, force, défense, expérience=0, niveau=1):
        self.nom = nom
        self.vie = vie
        self.force = force
        self.défense = défense
        self.expérience = expérience
        self.niveau = niveau

    def attaquer(self, ennemi):
        dégâts = max(0, self.force - ennemi.défense)
        ennemi.vie -= dégâts
        print(f"{self.nom} attaque {ennemi.nom} et inflige {dégâts} dégâts.")

    def gagner_experience(self, xp):
        self.expérience += xp
        print(f"{self.nom} gagne {xp} points d'expérience.")
        if self.expérience >= 100:
            self.niveau += 1
            self.force += 2
            self.défense += 2
            self.vie += 10
            self.expérience -= 100
            print(f"{self.nom} monte au niveau {self.niveau} !")

    def est_vivant(self):
        return self.vie > 0


class Ennemi:
    def __init__(self, nom, vie, force, défense, expérience_donnée):
        self.nom = nom
        self.vie = vie
        self.force = force
        self.défense = défense
        self.expérience_donnée = expérience_donnée

    def attaquer(self, joueur):
        dégâts = max(0, self.force - joueur.défense)
        joueur.vie -= dégâts
        print(f"{self.nom} attaque {joueur.nom} et inflige {dégâts} dégâts.")

    def est_vivant(self):
        return self.vie > 0


def générer_ennemi():
    types_ennemis = [
        Ennemi("Gobelin", 30, 5, 2, 20),
        Ennemi("Orc", 50, 7, 5, 30),
        Ennemi("Troll", 80, 10, 8, 50)
    ]
    return random.choice(types_ennemis)


def combat(joueur, ennemi):
    print(f"Un {ennemi.nom} apparaît !")
    while joueur.est_vivant() and ennemi.est_vivant():
        action = input("Voulez-vous attaquer ou fuir ? ").lower()
        if action == "attaquer":
            joueur.attaquer(ennemi)
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)
        elif action == "fuir":
            print(f"{joueur.nom} prend la fuite !")
            return False
        else:
            print("Action non reconnue.")

    if joueur.est_vivant():
        print(f"{joueur.nom} a vaincu {ennemi.nom} !")
        joueur.gagner_experience(ennemi.expérience_donnée)
    else:
        print(f"{joueur.nom} a été vaincu par {ennemi.nom}...")

    return joueur.est_vivant()


def explorer(joueur):
    print("Vous partez explorer...")
    événement = random.choice(["combat", "rien", "trésor"])
    if événement == "combat":
        ennemi = générer_ennemi()
        combat(joueur, ennemi)
    elif événement == "rien":
        print("Rien d'intéressant ne se passe.")
    elif événement == "trésor":
        print("Vous trouvez un trésor et gagnez 20 points d'expérience !")
        joueur.gagner_experience(20)


def rpg_textuel():
    nom = input("Entrez le nom de votre personnage : ")
    joueur = Personnage(nom, 100, 10, 5)

    print(f"Bienvenue dans le monde de l'aventure, {joueur.nom} !")

    while joueur.est_vivant():
        print(
            f"\n{joueur.nom} - Vie : {joueur.vie} | Force : {joueur.force} | Défense : {joueur.défense} | Niveau : {joueur.niveau}")
        action = input("Que voulez-vous faire ? (explorer/consulter vos stats/quitter) : ").lower()
        if action == "explorer":
            explorer(joueur)
        elif action == "consulter vos stats":
            print(
                f"Nom : {joueur.nom}, Vie : {joueur.vie}, Force : {joueur.force}, Défense : {joueur.défense}, Niveau : {joueur.niveau}, Expérience : {joueur.expérience}")
        elif action == "quitter":
            print("Merci d'avoir joué !")
            break
        else:
            print("Action non reconnue.")


if __name__ == "__main__":
    rpg_textuel()