import random

print("                      === JEU DU PENDU ===            ")
print("Dans ce jeu le joueur devra déviner le mot lettre par lettre")

# déclaration d'une liste de cinq mots
list_of_words = ["PYTHON", "CONSOLE", "HANGMAN", "STAGE", "ALGORITHME"]

# Choix aléatoire du mot secret
secret_word = random.choice(list_of_words)

guessed_letters = []  # lettres trouvés
count_life = 6  # Nombres d'erreurs limités à 6

# Boucle principal


while count_life > 0:  # Tant que l'erreur est toujours limité

    # BLOC AFFICHAGE DU MOT MASQUÉ
    display = ""
    i = 0
    while i < len(secret_word):
        letter = secret_word[i]

        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
        i += 1

    print("\nMot à deviner :", display)
    print("Vies restantes :", count_life)

    # Chaque tentative de lettre du joueur est directement changé en majuscules
    attempt = input("Proposez une lettre : ").upper()

    # Vérifie la longueur du mot ou s'il n'est pas alphanumèrique
    if len(attempt) != 1 or not attempt.isalpha():
        print("⚠️ Attention, vous devez entrer une seule lettre !")
        continue

    # Si tentative d'essaie de lettre se trouve déjà dans les lettres trouvés
    if attempt in guessed_letters:
        print("⚠️ Vous avez déjà essayé cette lettre !")
        continue

    # On ajoute chaque tentative de lettres aux lettres trouvés
    guessed_letters.append(attempt)

    # Si tentative de lettre se trouve dans mot secret
    if attempt in secret_word:
        print("✅ Bonne pioche !")
    else:
        print("❌ Mauvaise lettre !")
        count_life -= 1

# Vérifie si le joueur à déjà trouver tous les lettres du mot secret pour cesser le jeu
    mot_complet = True
    j = 0

    while j < len(secret_word):

        if secret_word[j] not in guessed_letters:
            mot_complet = False
        j += 1

    if mot_complet:
        # On génère un dernier affichage propre pour montrer le mot fini
        display_final = ""
        k = 0

        while k < len(secret_word):
            display_final += secret_word[k] + " "
            k += 1

        print("\nMot à deviner :", display_final)

        # Résultats si le joueur trouve tous les lettres du mots
        print("\n=========================================")
        print(f"🎉 Bravo ! Vous avez gagné avec {count_life} vie(s) restante(s) !")
        print("Le mot était bien :", secret_word)
        print("=========================================")
        break

# Si limite d'essai est atteinte
if count_life == 0:
    print("\n=========================================")
    print(f"💥 Dommage, vous avez perdu ! Le mot secret était : {secret_word}")
    print("=========================================")
