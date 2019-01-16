import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Le chemin du dossier de fichiers source (contenant les fichiers markdown)", action="store_true")
parser.add_argument("-o", help="le chemin du dossier où seront mis les fichiers générés pour le site statique", action="store_true")
args = parser.parse_args()

if args.i:
    print("chemin fichier source ")
if args.o:
    print("chemin fichier générés ")