def guess_the_word(user_guess, secret_word="python"):
    """
    Retourne True si la proposition (user_guess) correspond au mot secret.
    """
    return user_guess.strip().lower() == secret_word.lower()


if __name__ == "__main__":
    print("Bienvenue dans le jeu Guess the Word!")
    # Pour l'instant, nous nous contentons d'afficher un message d'accueil.
