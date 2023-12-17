

def lire_fichier(racine):
    try:
        with open(racine, 'r') as file:
            contenu = file.read()
            return contenu  # Renvoie le contenu du fichier
    except FileNotFoundError:
        print(f"Le fichier '{racine}' n'existe pas")


file = "D:/2eme\deveII\TP7/argparse/texte2.txt"
print(lire_fichier(file))

def ecrire_a_la_fin(chemin_fichier, contenu):
    try:
        with open(chemin_fichier, 'a') as file:
            file.write(contenu)
            return f" les lignes ont bien été ajouter"
    except FileNotFoundError:
        return f"Le fichier '{chemin_fichier}' n'existe pas"

chemin = "D:/2eme\deveII\TP7/argparse/texte2.txt"
contenu = "\nContenu à ajouter à la fin du fichier."

print(ecrire_a_la_fin(chemin, contenu))

def concatener_fichiers(chemin_fichiers, fichier_destination):
    try:
        with open(fichier_destination, 'a') as destination:
            for fichier in chemin_fichiers:
                try:
                    with open(fichier, 'r') as source:
                        contenu = source.read()
                        destination.write(contenu)
                        destination.write('\n')  # Ajoute un saut de ligne à la fin de chaque fichier
                except FileNotFoundError:
                    print(f"Le fichier '{fichier}' n'existe pas.")
                except IOError as e:
                    print(f"Erreur d'entrée/sortie lors de la lecture du fichier '{fichier}': {e}")
        return f"Fichiers concaténés dans '{fichier_destination}'"
    except IOError as e:
        return f"Erreur d'entrée/sortie lors de l'ouverture du fichier de destination '{fichier_destination}': {e}"

# Liste des chemins des fichiers à concaténer
chemins = [
    "D:/2eme/deveII/TP7/argparse/texte2.txt",
    # Ajoutez d'autres chemins de fichiers si nécessaire...
]

destination = "D:/2eme/deveII/TP7/argparse/texte1.txt"
print(concatener_fichiers(chemins, destination))

