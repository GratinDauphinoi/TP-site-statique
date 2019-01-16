

fichier_markdown = open("markdown.txt", "r")
markdown = fichier_markdown.read()
print (markdown)

fichier_html = open("html.txt", "w")
fichier_html.write(markdown)

lignes = fichier_markdown.readlines()
for ligne in lignes:
    Remplacement_h1 = ligne.replace("#", "<h1>")
    fichier_html.write(Remplacement_h1)



fichier_markdown.close()
fichier_html.close()