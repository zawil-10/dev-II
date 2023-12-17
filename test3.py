"""
utilisation d'argparse pour un script Python qui
manipule des fichiers texte en fonction d'options spécifiées en ligne de commande.
 Ce script permet de lire, écrire ou concaténer des fichiers texte
"""

import argparse


def lire_fichier(racine):
    try:
        with open(racine, 'r') as file:
            contenu = file.read()
            return contenu  # Renvoie le contenu du fichier
    except FileNotFoundError:
        print(f"Le fichier '{racine}' n'existe pas")


def ecrire_fichier(chemin_fichier, contenu):
    try:
        with open(chemin_fichier, 'a') as file:
            file.write(contenu)
            return f"Le contenu a bien été écrit dans '{chemin_fichier}'"
    except FileNotFoundError:
        return f"Le fichier '{chemin_fichier}' n'existe pas"


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


def main():
    parser = argparse.ArgumentParser(description='Gestionnaire de fichiers texte')

    parser.add_argument('action', choices=['lire', 'ecrire', 'concatener'], help='Action à effectuer')
    parser.add_argument('fichiers', nargs='*', help='Fichier(s) à utiliser')
    parser.add_argument('--destination', help='Chemin du fichier de destination (pour concatener)')

    args = parser.parse_args()

    if args.action == 'lire':
        for fichier in args.fichiers:
            print(lire_fichier(fichier))
    elif args.action == 'ecrire':
        if len(args.fichiers) != 1:
            print("Veuillez fournir un seul fichier pour écrire")
        else:
            contenu = input("Entrez le contenu à écrire : ")
            print(ecrire_fichier(args.fichiers[0], contenu))
    elif args.action == 'concatener':
        if not args.destination:
            print("Veuillez spécifier un fichier de destination pour la concaténation")
        else:
            print(concatener_fichiers(args.fichiers, args.destination))


if __name__ == '__main__':
    main()


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

