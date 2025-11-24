- Le script a été testé sur une machine Kali Linux équipée de R 4.5.2. 
  L’exécution s’est révélée impossible en raison de l’incompatibilité des deux 
  packages indispensables : DataCombine et PReMiuM. DataCombine n’est plus 
  disponible pour les versions récentes de R et ne possède plus d’archives 
  installables, tandis que PReMiuM dépend de packages spatiaux (sf, s2, spdep) 
  qui ne compilent pas sous Kali Linux et ne sont plus compatibles avec R ≥ 4.3.

- Nous avons essayé des solutions comme  : installation via CRAN, 
  utilisation des archives CRAN, installation depuis GitHub, compilation manuelle 
  des sources, ajout des dépendances système (libgdal, libgeos, libproj, udunits2, 
  gsl, etc.). Toutes ces tentatives ont échoué, soit à cause de packages retirés 
  du CRAN, soit à cause d’incompatibilités avec R 4.5.2.

- nous avons tenté d'exécuter le script dans un 
  environnement isolé via Docker et Podman. Nous avons testé plusieurs images 
  R différentes (r-base, tidyverse, rocker/r-base:4.1.2, r-base:4.1.x, r-base:3.6.x). 
  Cependant, même dans ces environnements, les mêmes erreurs apparaissent : 
  impossibilité de compiler les dépendances spatiales et échecs d'installation 
  des versions anciennes de DataCombine et PReMiuM.

- malgré de nombreuses tentatives, il n’a pas été possible d’exécuter 
  correctement le script R dans notre configuration actuelle.