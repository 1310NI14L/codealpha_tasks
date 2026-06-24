#  Stage chez CodeAlpha — Programmation Python

**Stagiaire :** AHOUANSOU Mahutin Daniel Dieudonné  
**Projet :** Tâche 3 — Extraction Automatisée d'E-mails

---

##  Description du Projet
Développement d'un script d'automatisation séquentiel et linéaire (sans aucune fonction `def`) pour isoler et 
extraire toutes les adresses e-mail valides d'un texte brut. Le programme lit le fichier source, filtre les 
données et génère automatiquement un rapport propre.

---

##  Concepts Clés Appliqués
* **Scripts I/O :** Automatisation de la lecture et de l'écriture de fichiers textes avec `with open()`.
* **Expressions Régulières (Regex) :** Utilisation du module `re` pour scanner et valider les motifs textuels.

---

##  Architecture & Flux Logique
1. **Initialisation :** Importation des modules (`os`, `re`) et définition des chemins de fichiers.
2. **Lecture Source :** Chargement du fichier `input_textEmail.txt` en mémoire.
3. **Filtrage (Regex) :** Extraction des e-mails conformes et rejet des formats invalides via `re.findall()`.
4. **Export :** Écriture séquentielle des résultats dans le fichier cible `extracted_emails.txt`.

---

##  Analyse de la Formule de Détection (Regex)
```python
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

[a-zA-Z0-9._%+-]+ : Identifiant utilisateur (lettres, chiffres et symboles autorisés).

@ : Symbole arobase obligatoire.

[a-zA-Z0-9.-]+ : Nom de domaine (lettres, chiffres, tirets et points).

\. : Point physique obligatoire avant l'extension.

[a-zA-Z]{2,} : Extension finale (uniquement des lettres, minimum 2 caractères).

❌ Exemple de rejet : okanlahon01>@store.bj
Le caractère > n'étant pas autorisé dans l'identifiant utilisateur, la Regex stoppe immédiatement son analyse. 
L'adresse étant malformée, elle est ignorée de manière transparente.

