import re 

fichier_markdown = open("markdown.md", "r")
markdown = fichier_markdown.read()
#print (markdown)

fichier_html = open("html.html", "w")

# liste = {"#" : "<h1>", "##" : "<h2>", "###" : "<h3>", "*" : "<em>"}

# cle = liste.keys()
# print(cle)

# valeurs = liste.values()
# print(valeurs)


# Remplacement = markdown.replace(str(cle),str(valeurs))
# fichier_html.write(Remplacement)

method = 'sghsduighsduighU.Ssdgiurehtdiugeuirghe'
fichier_html.write(re.sub(r'U.S', r'Coucou', method))





# a = markdown.replace("###", "<h3>").replace("##", "<h2>").replace("#", "<h1>")

# a = a.replace("*", "<em>")


# print(a)

# fichier_html.write(a)








fichier_markdown.close()
fichier_html.close()