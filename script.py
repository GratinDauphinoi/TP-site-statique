import markdown
import codecs
import argparse


def convertion(input_directory, output_directory):

    #conversion MD -> HTML
    input_directory = codecs.open(input_directory, mode="r", encoding="utf-8")
    text = input_directory.read()
    html = markdown.markdown(text)

    output_directory = codecs.open(output_directory, "w",encoding="utf-8", errors="xmlcharrefreplace")
    output_directory.write(html)

def artung(input_directory, output_directory):

    input_directory = codecs.open("markdown.md", mode="r", encoding="utf-8")
    text = input_directory.read()
    html = markdown.markdown(text)

    #Code bonus allemand 

    Remplacement_important = text.replace("h", "").replace("ss", "z").replace("s", "z").replace("qu", "k").replace("ce", "ze").replace("c", "k").replace("ç", "z").replace("ph", "f").replace("pp", "p").replace("gu", "ch").replace("g", "ch").replace("j", "k").replace("v", "f").replace("s", "")


    html.write(Remplacement_important)

    output_directory = codecs.open(output_directory, "w", encoding="utf-8", errors="xmlcharrefreplace")
    output_directory.write(html)


#Utilisation arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", '--input_directory', type = str, help='Le chemin du dossier de fichiers source (contenant les fichiers markdown)')
parser.add_argument("-o", '--output_directory', type = str, help='le chemin du dossier où seront mis les fichiers générés pour le site statique')
parser.add_argument("-t", help="le dossier contenant des modèles de pages web à compléter", action="store_true")
# parser.add_argument("-a", '--artung', type = str, help='Texte en allemand', action='store_true')
args = parser.parse_args()


# if args.artung is True:
#   artung(args.input_directory, args.output_directory)
# else:
convertion(args.input_directory, args.output_directory)
