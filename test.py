import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Le chemin du dossier de fichiers source (contenant les fichiers markdown)", action="store_true")
parser.add_argument("-o", help="le chemin du dossier où seront mis les fichiers générés pour le site statique", action="store_true")
parser.add_argument("-t", help="le dossier contenant des modèles de pages web à compléter", action="store_true")
args = parser.parse_args()

if args.i:
    print("https://github.com/GratinDauphinoi/TP-site-statique/blob/master/markdown.txt")
if args.o:
    print("https://github.com/GratinDauphinoi/TP-site-statique/blob/master/html.txt")
if args.t:
    print("dossier modèles")