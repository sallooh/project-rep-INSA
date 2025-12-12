# project-rep-INSA
# Many Analysts

## Introduction

Ce dépôt présente une synthèse sur la reproductibilité et la réplicabilité de l’étude « Many Analysts ». L’analyse originale mobilisait 29 équipes chargées d’examiner le même jeu de données pour déterminer si les joueurs à la peau foncée reçoivent plus de cartons rouges que ceux à la peau claire.
Pour la reproductibilité, nous avons reproduit le travail des équipes comme 7, 25.
Pour la réplicabilité, nous intervenons comme une 30ᵉ équipe en proposant une nouvelle analyse du même jeu de données.

## Reproductibilité

### How to Reproduce the Results
1. **Requirements**  
   Nous avons utilisés principalement Python 2.7 et R pour reproduire les analyses. Les dépendances spécifiques sont listées dans le fichier `requirements.txt` (pour l'équipe 27).
   
   Etant donné que la version 2.7 de Python est obsolète, nous avons utilisé un debian Buster pour garantir la compatibilité. Le Dockerfile inclus dans le répertoire de l'équipe 27 permet de recréer l'environnement exact utilisé.

2. **Configuration de l’environnement**  
   Pour chaque équipe, un Dockerfile est fourni pour configurer l'environnement nécessaire. Pour construire et exécuter le conteneur Docker, utilisez les commandes suivantes dans chauque répertoire d'équipe `teams/teamXX` :
     ```bash
     docker build -t reproducible-project .
     docker run -it reproducible-project
     ```

3. **Reproduction des résultats**  
   Vous pouvez simplement exécuter ce script pour lancer la reproduction de l'analyse de la team27 (nous n'avons pas réussi à reproduire les analyses des équipes 7 et 25 à cause dee l'incompatibilité des versions de bibliothèques et de R) :
     ```bash
     bash scripts/reproducibility_team27.sh
     ```

### Is the Original Study Reproducible?
- Summarize the success or failure of reproducing the study.
- Include supporting evidence, such as comparison tables, plots, or metrics.

## Réplicabilité

### Variability Factors
### Key Variability Factors

| Variability Factor | Possible Values | Why it Matters |
|--------------------|-----------------|----------------|
| **Skin Tone Operationalization** | `continuous`, `binary` | Teams used either raw ratings (continuous) or a categorical “dark vs light” variable, leading to different effect sizes. |
| **Outcome Definition / Model Type** | `logit` (red_dummy), `poisson` (redCards) | Red cards are rare events; logistic vs Poisson modeling can reverse effect signs or significance. |
| **Covariate Set** | `none`, `performance`, `full` | The biggest source of variability. Including or excluding performance/discipline controls drastically changes the estimated effect. |
| **Missing Data Strategy** | `dropna`, `mean` | Different teams handle missing player attributes differently, changing sample size and estimates. |

---


### Replication Execution
1. **Instructions**  
     ```bash
     bash scripts/replicate_experiment.sh
     ```

2. **Presentation and Analysis of Results**  
### Replication Results Table

| ID | Outcome Model | Skin Variable | Covariates | Missing | Coef(skin) | p-value | Interpretation |
|----|----------------|---------------|-------------|----------|-------------|---------|----------------|
| 1  | logit          | continuous    | performance | dropna   | 0.3059      | 0.000   | Strong positive, highly significant |
| 2  | logit          | binary        | performance | dropna   | 0.1516      | 0.011   | Positive effect, significant |
| 3  | poisson        | continuous    | full        | dropna   | 0.3153      | 0.000   | Strong positive effect with full controls |
| 4  | logit          | continuous    | none        | dropna   | 0.2417      | 0.005   | Positive, significant even without covariates |
| 5  | logit          | binary        | full        | mean     | 0.1451      | 0.013   | Positive, significant; robust to imputation |
| 6  | poisson        | binary        | performance | dropna   | 0.1426      | 0.015   | Positive, significant under Poisson |
| 7  | logit          | continuous    | full        | mean     | 0.3236      | 0.000   | Strongest effect; full controls + imputation |
| 8  | poisson        | continuous    | none        | dropna   | 0.2374      | 0.005   | Positive, significant effect without covariates |

## Conclusion
- L’étude originale est partiellement reproductible, avec succès pour l’équipe 27 mais limitations dues aux versions logicielles pour d’autres équipes. La réplication menée par notre 30ᵉ équipe confirme les résultats principaux : les joueurs à la peau foncée reçoivent plus de cartons rouges. L’étude est donc réplicable, et ses conclusions restent robustes malgré la variation des méthodes analytiques.

