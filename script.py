
fichier_markdown = open("markdown.md", "r")
markdown = fichier_markdown.read()
print (markdown)

fichier_html = open("html.html", "w")

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