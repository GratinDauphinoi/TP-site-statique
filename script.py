import markdown
import codecs
import argparse
import black


debut = "<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset='utf-8'/>\n\t<link rel='stylesheet' type='text/css' href='main.css'/>\n<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet'>\n<style>body {font-family: 'Open Sans', sans-serif;}</style></head>\n<body>\n"
fin = "</body>\n</html>"


def convertion(input_directory, output_directory):

    # conversion MD -> HTML
    input_directory = codecs.open(input_directory, mode="r", encoding="utf-8")
    text = input_directory.read()
    html = markdown.markdown(text)

    output_directory = codecs.open(
        output_directory, "w", encoding="utf-8", errors="xmlcharrefreplace"
    )
    output_directory.write(debut)
    output_directory.write(html)
    output_directory.write(fin)


def achtung(input_directory, output_directory):

    input_directory = codecs.open("markdown.md", mode="r", encoding="utf-8")
    text = input_directory.read()

    # Code bonus allemand
    html = markdown.markdown(
        text.replace("h", "")
        .replace("ss", "z")
        .replace("s", "z")
        .replace("qu", "k")
        .replace("ce", "ze")
        .replace("c", "k")
        .replace("ç", "z")
        .replace("ph", "f")
        .replace("pp", "p")
        .replace("gu", "ch")
        .replace("g", "ch")
        .replace("j", "k")
        .replace("v", "f")
        .replace("s", "")
    )

    output_directory = codecs.open(
        output_directory, "w", encoding="utf-8", errors="xmlcharrefreplace"
    )
    output_directory.write(debut)
    output_directory.write(html)
    output_directory.write(fin)


# Utilisation arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "-i",
    "--input_directory",
    type=str,
    help="Le chemin du dossier de fichiers source (contenant les fichiers markdown)",
)
parser.add_argument(
    "-o",
    "--output_directory",
    type=str,
    help="le chemin du dossier où seront mis les fichiers générés pour le site statique.",
)

parser.add_argument(
    "-a",
    "--achtung",
    help="Aider les allemands à lire nos blogs français.",
    action="store_true",
)

args = parser.parse_args()


if args.achtung is True:
    achtung(args.input_directory, args.output_directory)
else:
    convertion(args.input_directory, args.output_directory)
