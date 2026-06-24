#  Stage chez CodeAlpha — Programmation Python

**Stagiaire :** AHOUANSOU Mahutin Daniel Dieudonné  
**Projet :** Tâche 2 — Suivi de Portefeuille Boursier

---

##  Description du Projet
Dans le cadre de mon stage chez **CodeAlpha**, j'ai développé un script de suivi de portefeuille boursier. L'objectif principal est de calculer la valeur totale d'un investissement à partir de prix d'actions prédéfinis. 

L'utilisateur saisit le nom et la quantité de ses actions directement dans le terminal. Le programme valide chaque saisie par rapport aux actifs disponibles et gère automatiquement les cumuls. En fin d'exécution, le bilan complet est automatiquement exporté dans un fichier CSV.

Pour respecter scrupuleusement les contraintes du cahier des charges, l'application adopte une structure purement séquentielle et linéaire. Elle n'utilise **aucune fonction personnalisée (`def`)**, reposant exclusivement sur les structures de contrôle natives de Python.

---

##  Concepts Clés Appliqués
* **Dictionnaires :** Un dictionnaire fixe (`stock_prices`) sert de base de référence pour les prix, tandis qu'un second dictionnaire dynamique (`portfolio`) centralise les actifs saisis et leurs quantités.
* **Entrées/Sorties (I/O) :** Gestion des interactions utilisateur dans le terminal via `input()` et `print()`.
* **Arithmétique de base :** Calcul des sous-totaux par ligne d'actifs et accumulation de la valeur totale du portefeuille.
* **Gestion de fichiers :** Utilisation du gestionnaire de contexte `with open()` et du module `csv` pour générer un rapport structuré sans solliciter d'action supplémentaire de l'utilisateur.

---

##  Architecture & Flux Logique
Le programme se déroule de manière fluide et linéaire :

1. **Initialisation :** Définition des prix de référence (AAPL, TSLA, AMZN, NVDA, MSFT) et création du portefeuille vide.
2. **Collecte des données (`while`) :** Saisie et normalisation du nom de l'action (mise en majuscules, suppression des espaces). La boucle s'interrompt si l'utilisateur tape `END` ou laisse le champ vide. Elle rejette les actions inconnues et cumule les quantités pour les doublons.
3. **Calcul du bilan :** Parcours du dictionnaire pour évaluer chaque ligne d'actif et mettre à jour l'investissement total.
4. **Export CSV automatique :** Écriture immédiate des en-têtes, du détail des actifs et de la valeur totale dans un fichier persistant.

---

##  Exemple d'Exécution

```text
         ___Stock Portfolio Tracker___

 The Goal is of  Build a simple stock tracker that calculates total investment based on manually defined stock prices.

___ Grab of your portfolio (Enter 'end' for stop writing) ___
Enter the name of action : LKDK
Warning : 'LKDK' is not listed in our stock prices. Please enter a valid stock.

Enter the name of action : AAPL
Enter the quantity for AAPL : 6

Enter the name of action : MSFT
Enter the quantity for MSFT : 7

Enter the name of action : MSFT
Enter the quantity for MSFT : 10

Enter the name of action : NVDA
Enter the quantity for NVDA : 12

Enter the name of action : END

   ___ Report of Portfolio Automatic Tracker ___ 
 AAPL : 6 * 180$ = 1080
 MSFT : 17 * 420$ = 7140
 NVDA : 12 * 120$ = 1440

______________________________________
Total Investment: 9660 $
________________________________________

 Portfolio automatically saved in 'saved_fileCSV/portfolio_CodeAlpha.csv'!

Process finished with exit code 0