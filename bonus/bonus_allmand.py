
avant = open("bonus/text_normal.txt", "r")
normal = avant.read()
print (normal)

apres = open("bonus/text_modifie.txt", "w")

Remplacement_important = normal.replace("h", "").replace("ss", "z").replace("s", "z").replace("qu", "k").replace("ce", "ze").replace("c", "k").replace("ç", "z").replace("ph", "f").replace("pp", "p").replace("gu", "ch").replace("g", "ch").replace("j", "k").replace("v", "f").replace("s", "")
print(Remplacement_important)

apres.write(Remplacement_important)

avant.close()
apres.close()