

fichier_markdown = open("markdown.txt", "r")
markdown = fichier_markdown.read()
print (markdown)

fichier_html = open("html.txt", "w")
fichier_html.write(markdown)










fichier_markdown.close()
fichier_html.close()