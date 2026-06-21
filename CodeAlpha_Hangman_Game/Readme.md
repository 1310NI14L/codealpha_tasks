# 🚀 Stage en Ligne chez CodeAlpha — Programmation Python

**Stagiaire :** AHOUANSOU Mahutin Daniel Dieudonné  
**Projet :** Tâche 1 — Conception d'un Jeu du Pendu en Mode Console

---

## 📝 Description du Projet
Dans le cadre de ma première tâche de stage chez **CodeAlpha**, j'ai développé un **Jeu du Pendu** classique s'exécutant entièrement dans le terminal. 
L'objectif est de permettre à l'utilisateur de deviner un mot secret choisi aléatoirement, lettre par lettre, avec un nombre d'essais limité à **6 vies**.
Conformément aux contraintes strictes du cahier des charges, ce programme a été conçu de manière purement séquentielle et linéaire. 
Il n'utilise **aucune fonction personnalisée (`def`) ni boucle `for`**, s'appuyant exclusivement sur des structures de contrôle fondamentales.

---

## ⚙️ Logique Fonctionnelle & Règles Implémentées

Le script intègre une gestion rigoureuse du flux de jeu à chaque tentative de l'utilisateur :

* **Validation des Saisies (Sécurité) :** Le programme vérifie instantanément chaque entrée. Si l'utilisateur saisit plus d'un caractère, un chiffre ou un symbole spécial, le jeu bloque la tentative et affiche un message d'erreur clair sans pénaliser ses vies.
* **Gestion des Doublons :** Si le joueur propose une lettre qu'il a déjà testée précédemment (qu'elle soit bonne ou mauvaise), le système affiche un message d'avertissement et ne décompte aucune vie.
* **Analyse Dynamique :** * **Bonne pioche :** Si la lettre appartient au mot secret, elle est révélée à sa position exacte et le mot masqué se met à jour (ex: `_ O N S O L _`).
* **Mauvaise lettre :** Si la lettre est absente, un message d'erreur s'affiche et le compteur de vies diminue de 1.
* **Vérification de Victoire Immédiate :** Après **chaque** lettre validée, le programme inspecte l'état du mot. Dès que toutes les lettres sont découvertes, le jeu s'arrête instantanément et affiche le message de succès, évitant ainsi tout tour inutile ou bug d'affichage.

---

## 🛠️ Concepts Clés Utilisés & Respectés

Pour structurer ce code sans utiliser de fonctions, les concepts fondamentaux suivants ont été mobilisés :
1. **Module `random`** : Pour assurer le tirage aléatoire et équitable du mot secret au lancement de la partie.
2. **Boucles `while` exclusives** : Utilisées pour maintenir le jeu actif, mais aussi pour parcourir les index des chaînes de caractères lors de la construction de l'affichage masqué et lors de la vérification des lettres.
3. **Structures Conditionnelles Imbriquées (`if-elif-else`)** : Pour aiguiller le comportement du programme selon les choix de l'utilisateur.
4. **Listes (`list`) & Méthodes associées** : Pour stocker le dictionnaire de mots techniques et accumuler l'historique des lettres proposées (`.append()`).
5. **Chaînes de caractères (`string`)** : Manipulation des indexations et utilisation de la méthode `.upper()` pour rendre le jeu insensible à la casse (majuscules/minuscules).

---

## 🎮 Comment Exécuter le Jeu

Assurez-vous de disposer de Python installé sur votre environnement local, puis lancez le script depuis votre terminal :

```bash
python hangman.py