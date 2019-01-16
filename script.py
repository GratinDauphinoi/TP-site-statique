

fichier_markdown = open("markdown.txt", "r")
markdown = fichier_markdown.read()
print (markdown)

fichier_html = open("html.txt", "w")


Remplacement_h1 = markdown.replace("#", "<h1>")
fichier_html.write(Remplacement_h1)

Remplacement_h2 = markdown.replace("##", "<h2>")
fichier_html.write(Remplacement_h2)

Remplacement_h3 = markdown.replace("##", "<h3>")
fichier_html.write(Remplacement_h3)

Remplacement_important = markdown.replace("*", "<em>")
fichier_html.write(Remplacement_important)

fichier_markdown.close()
fichier_html.close()