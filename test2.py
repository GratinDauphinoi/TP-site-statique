fichier_markdown = open("markdown.md", "r")
markdown = fichier_markdown.read()
#print (markdown)

fichier_html = open("html.html", "w")

'''
liste = {"#" : "<h1>", "##" : "<h2>", "###" : "<h3>", "*" : "<em>"}

cle = liste.keys()
print(cle)

valeurs = liste.values()
print(valeurs)


Remplacement = markdown.replace(str(cle),str(valeurs))
fichier_html.write(Remplacement)
'''

if "#" in markdown:
    Remplacement_h1 = markdown.replace("#", "<h1>")
    fichier_html.write(Remplacement_h1)

if "##" in markdown:
    Remplacement_h2 = markdown.replace("##", "<h2>")
    fichier_html.write(Remplacement_h2)

if "###" in markdown:
    Remplacement_h3 = markdown.replace("###", "<h3>")
    fichier_html.write(Remplacement_h3)

if "*" in markdown:
    Remplacement_important = markdown.replace("*", "<em>")
    fichier_html.write(Remplacement_important)


fichier_markdown.close()
fichier_html.close()