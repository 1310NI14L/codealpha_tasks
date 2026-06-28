import re
import os

print("         ___ Task Automation with Python Scripts ___")
print("The goal is of automate a small, real-life repetitive task.")
print("                   ==============                  \n")

print("        ___ Automated Email Extractor ___")
print("Goal: Automatically find and extract all email addresses from a text file.\n")

#Chemin du fichier texte par défaut
default_filename = "fileTXT/input_textEmail.txt"

#Boucle pour demander à l'utilisateur d'entrez un fichiers à analyser
values = True
while values :
    file_name = input("Enter the path or name of the .txt file to analyze: ")

    #On vérifie si le chemin existe sur le disque
    if os.path.exists(file_name) :
        print(f"\nReading data from custom file: '{file_name}'...")
        break
    else :
        print(f"Warning: The file '{file_name}' was not found. Please try again.\n")
        print(f"Switching to default file: '{default_filename}'...\n")
        file_name = default_filename
        break

# Lecture du contenu du fichier sélectionné
print(f"\nReading data from '{file_name}'...")
with open(file_name, "r", encoding="utf-8") as file:
    content = file.read() # On stocke le contenu du fichier

# Definition du motif pour la recherche d'une adresse email
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

#Extractions de tous les emails correspondant
found_emails = re.findall(email_pattern, content)

#Nombre d'emails trouvés
print(f"Found {len(found_emails)} emails adress(es). \n")

#Chemin du fichier d'enregistrements
output_filename = "fileTXT/extracted_emails.txt"

print(f"Savings results to '{output_filename}'...")

# Ecriture des résultats
with open(output_filename, "w", encoding="utf-8") as file:
    file.write("=== Extracted Email Addresses List ===\n\n")

    for email in found_emails:
        file.write(f"- {email}\n")
        print(f"    -> Extracted : {email}\n")

print(f" Automation complete ! Result successfully saved to '{output_filename}'.")