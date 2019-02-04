import markdown
import codecs
import argparse

#conversion MD -> HTML
input_file = codecs.open("markdown.md", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)

output_file = codecs.open("html.html", "w",encoding="utf-8", errors="xmlcharrefreplace")
output_file.write(html)

#Utilisation arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Le chemin du dossier de fichiers source (contenant les fichiers markdown)", action="store_true")
parser.add_argument("-o", help="le chemin du dossier où seront mis les fichiers générés pour le site statique", action="store_true")
parser.add_argument("-t", help="le dossier contenant des modèles de pages web à compléter", action="store_true")
args = parser.parse_args()

if args.i:
    print(args.i)
    print("Fichier source contenant le markdown : https://github.com/GratinDauphinoi/TP-site-statique/blob/master/markdown.txt")
if args.o:
    print("Fichier généré pour le site statique : https://github.com/GratinDauphinoi/TP-site-statique/blob/master/html.txt")
if args.t:
    print("Dossier modèles")

#Code bonus allemand 
avant = open("bonus/text_normal.txt", "r")
normal = avant.read()
print (normal)

apres = open("bonus/text_modifie.txt", "w")

Remplacement_important = normal.replace("h", "").replace("ss", "z").replace("s", "z").replace("qu", "k").replace("ce", "ze").replace("c", "k").replace("ç", "z").replace("ph", "f").replace("pp", "p").replace("gu", "ch").replace("g", "ch").replace("j", "k").replace("v", "f").replace("s", "")
print(Remplacement_important)

apres.write(Remplacement_important)

avant.close()
apres.close()