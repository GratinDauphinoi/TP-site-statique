# TP-site-statique

### Differents fichiers:

##### le fichier script

C'est dans ce fichier qu'est contenu le code python permettant la conversion du Markdown en HTML

##### le fichier markdown

C'est dans ce fichier que le texte Markdown devra être écrit avant d'être converti en HTML

##### le fichier html

C'est le fichier qui contient le code HTML converti du markdown.

##### l'énoncé se trouve au lien suivant 

`https://github.com/vpoulailleau/site_statique`

### Fonctionnement

Le script se lance tout d'abord en entrant le nom du fichier ( ici `script.py`), suivis de `-i` "nom du fichier md ou est inscrit le code marckdown" et enfin `-o` "nom du fichier html si il existe ou le programme le créera, qui acceuillera le rendu md sous forme HTML".

#### Bonus 

Pour finir une option est rajoutée qui permet d'utiliser l'achtung: pour aider les allemands à lire nos blogs français.
Pour plus de reseignement, cliquez ici : `https://linuxfr.org/nodes/108129/comments/1642666`

Cette option se traduit par un `-a` écrit en fin de ligne de commande.

#### Exemple 

On peut utiliser ce programme par exemple de la maniere suivante : 
`py .\script.py -i D:\Ynov\Python\TP-site-statique\markdown.md -o D:\Ynov\Python\TP-site-statique\html.html -a`

Pour plus d'information utilisez la commande `-h` ou `--help`.