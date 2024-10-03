def quiz():
    questions = [
        {
            "question": "Quelle est la capitale de la France ?",
            "options": ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
            "réponse": "c"
        },
        {
            "question": "Quel est le plus grand océan ?",
            "options": ["a) Atlantique", "b) Indien", "c) Arctique", "d) Pacifique"],
            "réponse": "d"
        },
        {
            "question": "Quel est le langage de programmation utilisé pour ce jeu ?",
            "options": ["a) Java", "b) C++", "c) Python", "d) JavaScript"],
            "réponse": "c"
        }
    ]

    score = 0

    print("Bienvenue au Quiz !")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        réponse_utilisateur = input("Votre réponse (a, b, c, d) : ").lower()

        if réponse_utilisateur == q["réponse"]:
            print("Bonne réponse !")
            score += 1
        else:
            print("Mauvaise réponse.")

    print(f"Votre score final est {score}/{len(questions)}.")


if __name__ == "__main__":
    quiz()
