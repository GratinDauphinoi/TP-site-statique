fichier = open("markdown.txt", "r")
markdown = fichier.read
print (markdown)

fichier = open("html.txt", "w")
fichier.write(markdown)
fichier.close()