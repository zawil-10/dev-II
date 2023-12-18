"""
utilisation d'argparse pour un script Python qui
manipule des fichiers texte en fonction d'options spécifiées en ligne de commande.
 Ce script permet de lire, écrire ou concaténer des fichiers texte et les vider
"""

import argparse


def lire_fichier(racine_un):
    try:
        with open(racine_un, 'r') as file:
            contenu = file.read()
            return contenu  # Renvoie le contenu du fichier
    except FileNotFoundError:
        return f"Le fichier '{racine_un}' n'existe pas"


def ecrire_fichier(racine_deux, contenu):
    try:
        with open(racine_deux, 'a') as file:
            file.write(contenu)
            return f"Le contenu a bien été écrit dans '{racine_deux}'"
    except FileNotFoundError:
        return f"Le fichier '{racine_deux}' n'existe pas"


def concatener_fichiers(racine_trois, fichier_destination):
    try:
        with open(fichier_destination, 'a') as destination:
            for fichier in racine_trois:
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


def vider_fichier(racine_quatre):
    try:
        with open(racine_quatre, 'w') as file:
            file.write('')
        return f"Contenu du fichier '{racine_quatre}' vidé."
    except FileNotFoundError:
        return f"Le fichier '{racine_quatre}' n'existe pas."


def main():
    parser = argparse.ArgumentParser(description='manipulation de fichier')

    parser.add_argument('action', choices=['lire', 'ecrire', 'concatener', 'vider'], help='Action à effectuer')
    parser.add_argument('fichiers', nargs='*', help='Fichier(s) à utiliser')
    parser.add_argument('--destination', help='Chemin du fichier de destination (pour concatener)')

    args = parser.parse_args()

    if args.action == 'lire':
        for fichier in args.fichiers:
            print(lire_fichier(fichier))
    elif args.action == 'ecrire':
        # Votre code pour l'écriture dans un fichier
        pass
    elif args.action == 'concatener':
        # Votre code pour concaténer des fichiers
        pass
    elif args.action == 'vider':
        for fichier in args.fichiers:
            vider_fichier(fichier)


if __name__ == '__main__':
    main()
