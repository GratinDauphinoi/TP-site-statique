import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Le chemin du dossier de fichiers source (contenant les fichiers markdown)")
parser.add_argument("-o", help="le chemin du dossier où seront mis les fichiers générés pour le site statique")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")