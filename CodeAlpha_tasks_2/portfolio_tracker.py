import  csv

print("         ___Stock Portfolio Tracker___")
print("\n The Goat is of  Build a simple stock tracker that calculates total investment based on manually defined stock prices.\n")

#Dictionnaire codé en dur pour faire références aux données
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 350,
    "NVDA": 120,
    "MSFT": 420
}

#Dictionnaire vide pour enregistrer les données valides de l'utilisateur
portfolio = {}

stop_input = True #Contrôle de la boucle while

# Instructions de saisir
print("___ Grab of your portfolio (Enter 'end' for stop writing) ___")

# Boucle principale pour que le contrôle soit effectué lors de la saisie des données
while stop_input:

    # Récupération du nom de l'action, suppression des espaces et passage en majuscules
    names = input("Enter the name of action : ").strip().upper()

    # Condition d'arrêt
    if names == "END" or names == "":
        break

    # Valide l'action si ça existe dans le dictionnaire de référence
    if names not in stock_prices:
        print(f"Warning : '{names}' is not listed in our stock prices. Please enter a valid stock.\n")
        continue

    #Saisie de la quantité (convertie en entier)
    quantity = int(input(f"Enter the quantity for {names} : "))
    print("")

    # Enregistrement dans le portefeuille
    if names in portfolio:
        portfolio[names] += quantity
    else:
        portfolio[names] = quantity

# Initialisation du cumul de l'investissement total
total_investment = 0

print("\n   ___ Report of Portfolio Automatic Tracker ___ ")

# Parcours du portefeuille pour effectuer les calculs
for names, quantity in portfolio.items():
    price = stock_prices[names]
    subtotal = quantity * price

    # Ajout du sous-total à l'investissement global
    total_investment += subtotal

    print(f" {names} : {quantity} * {price}$ = {subtotal}")

print("\n______________________________________")
print(f"Total Investment: {total_investment} $")
print("________________________________________")

# Configuration du chemin relatif pour la sauvegarde du fichier CSV
filename = "saved_fileCSV/portfolio_CodeAlpha.csv"

# Écriture automatisée des données dans le fichier CSV (mode "w" pour écraser/mettre à jour)
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")

    # Écriture de la ligne d'en-tête du tableau
    writer.writerow(["Action Name", "Quantity Action", "Unit Price ($)", "Total Values ($)"])

    # Écriture des lignes de chaque action présente dans le portefeuille
    for names, quantity in portfolio.items():
        price = stock_prices[names]
        subtotal = quantity * price
        writer.writerow([names, quantity, price, subtotal])

    # Ajout d'une ligne vide de séparation et de la ligne du total général
    writer.writerow([])
    writer.writerow(["Total Investment ($)", "", "", f"{total_investment}"])

print(f"\n Portfolio automatically saved in '{filename}'!")
