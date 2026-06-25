import re

print("         ___ Task Automation with Python Scripts ___")
print("The goal is of automate a small, real-life repetitive task.")
print("                   ==============                  \n")

print("        ___ Automated Email Extractor ___")
print("Goal: Automatically find and extract all email addresses from a text file.\n")

#Chemin du fichier texte
input_filename = "fileTXT/input_textEmail.txt"

#Lecture du contenu du fichier texte
print(f"reading data from '{input_filename}'...")
with open(input_filename, "r", encoding="utf-8") as file:
    content = file.read() #stockage du contenu du fichier texte

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