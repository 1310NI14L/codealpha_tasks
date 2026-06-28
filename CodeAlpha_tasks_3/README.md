#  Stage chez CodeAlpha — Programmation Python

**Stagiaire :** AHOUANSOU Mahutin Daniel Dieudonné  
**Projet :** Tâche 3 — Extraction Automatisée d'E-mails

---

##  Description du Projet
Développement d'un script d'automatisation séquentiel et linéaire (sans aucune fonction `def`) pour isoler et 
extraire toutes les adresses e-mail valides d'un texte brut. Le programme propose une interface interactive permettant à l'utilisateur d'analyser le fichier de son choix, tout en intégrant une sécurité de repli automatique sur un fichier par défaut en cas de chemin introuvable.

---

##  Concepts Clés Appliqués
* **Gestion du Système de Fichiers :** Utilisation du module `os` pour vérifier dynamiquement la présence des fichiers sur le disque avant traitement.
* **Scripts I/O :** Automatisation de la lecture et de l'écriture de fichiers textes avec `with open()`.
* **Expressions Régulières (Regex) :** Utilisation du module `re` pour scanner et valider les motifs textuels.

---

##  Architecture & Flux Logique
1. **Initialisation :** Importation des modules (`os`, `re`) et configuration du fichier de secours par défaut.
2. **Saisie Interactive & Flexibilité :** Invitation de l'utilisateur à entrer un chemin de fichier. 
   * *Si le fichier existe :* Le script l'analyse directement.
   * *Si le fichier est introuvable :* Le script lève une alerte et bascule de manière transparente sur le fichier par défaut (`fileTXT/input_textEmail.txt`).
3. **Lecture Source :** Chargement en mémoire du contenu du fichier validé.
4. **Filtrage (Regex) :** Extraction des e-mails conformes et rejet des formats invalides via `re.findall()`.
5. **Export :** Écriture séquentielle des résultats et affichage en temps réel dans la console, puis génération du rapport cible `extracted_emails.txt`.

---

##  Analyse de la Formule de Détection (Regex)
```python
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"