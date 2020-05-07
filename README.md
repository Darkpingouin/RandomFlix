![logo](https://raw.githubusercontent.com/Darkpingouin/RandomFlix/master/logo.png)
# :tv: RandomFlix

_Random Netflix movie chooser - Alexa Skill_

:question: RandomFlix est une skill alexa dispo [ici](https://www.amazon.fr/dp/B0888TDHDR/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=randomflix&qid=1588863961&s=digital-skills&sr=1-1) basée sur les données de [Flixable FR](https://fr.flixable.com/)

:clipboard: Le fichier [RandomFlix.py](https://github.com/Darkpingouin/RandomFlix/blob/master/lambda/RandomFlix.py) contient la classe movie et randomflix qui permettent de parser le site et de chercher un film au hasard parmi les catégories disponibles.

:pushpin: Le reste sers à gérer la skill alexa et l'affichage en utilisant de l'APL. Le tout est basé sur le repo officiel [ici](https://github.com/alexa/skill-sample-python-sauce-boss)

## :bulb: Pour la suite

- Ajouter d'autres langues (se baser sur la locale de l'utilisateur pour le catalogue)
- Ajouter les series TV
- Ajouter un systeme premium (in skill purchases) pour acceder a plus de categories ou aux series TV
- Ajouter la recherche par date de sortie / rating minimum.
