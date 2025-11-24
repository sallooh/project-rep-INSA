# le processus de reproductibilité de l'équipe 27 : 

## Code : 
Le code python de l'équipe était fourni dans un notebook Jupyter qu'on a  reconverti en script python pour automatiser l'exécution.

## Dockerfile :
Pour simuler le même environnement que celui utilisé par l'équipe 27, nous avons recherché la version de python dans la documentation de versions qui correspond à la date où l'équipe a soumi son analyse (Aout 2014). C'était la version 2.7
Etant donné que cette version est obsolète, nous avons dû installer un vieux Debian Buster qui inclut le python 2.7

## Résultats : 

La reproduction pour l'équipe 27 a été réalisée avec succès. Les résultats obtenus ont été comparés aux résultats originaux de l'équipe 27, montrant une correspondance étroite dans les statistiques clés.
Cependant, quelques divergences mineures ont été notées, principalement dues à des différences potentielles dans les versions des bibliothèques utilisées. LEs versions exactes des bibliothèques utilisées par l'équipe 27 n'étant pas spécifiées, nous avons fait de notre mieux pour utiliser des versions compatibles avec Python 2.7, qui sont spécifier dans le fichier `requirements.txt`


## Instructions pour la reproduction

    ```bash
     docker build -t reproductibility-project .
     docker run -it reproductibility-project
     ```