import random
import string

def generate_password(length=12):
    """Génère un mot de passe aléatoire de la longueur spécifiée."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

try:
    password_length = int(input("Entrez la longueur du mot de passe : "))
    if password_length < 6:
        print("La longueur du mot de passe doit être d'au moins 6 caractères pour plus de sécurité.")
    else:
        generated_password = generate_password(password_length)
        print(f"Votre mot de passe généré est : {generated_password}")
except ValueError:
    print("Veuillez entrer un nombre valide pour la longueur du mot de passe.")

# Attendre que l'utilisateur appuie sur une touche avant de fermer
input("Appuyez sur Entrée pour fermer le programme...")
