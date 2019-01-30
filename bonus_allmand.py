import random


fichier_markdown = open("text_normal.txt", "r")
markdown = fichier_markdown.read()
print (markdown)

fichier_html = open("text_modifie.txt", "w")

Remplacement_important = markdown.replace("h", "").replace("ss", "z").replace("ai", "é").replace("s", "z").replace("qu", "k").replace("ce", "ze").replace("c", "k").replace("ç", "z").replace("ph", "f").replace("pp", "p").replace("gu", "ch").replace("g", "ch").replace("j", "k").replace("v", "f").replace("s", "")
print(Remplacement_important)

fichier_html.write(Remplacement_important)

fichier_markdown.close()
fichier_html.close()