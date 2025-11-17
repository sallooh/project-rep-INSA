# project-rep-INSA
# Many Analysts

## Introduction

Ce dépôt présente une synthèse sur la reproductibilité et la réplicabilité de l’étude « Many Analysts ». L’analyse originale mobilisait 29 équipes chargées d’examiner le même jeu de données pour déterminer si les joueurs à la peau foncée reçoivent plus de cartons rouges que ceux à la peau claire.
Pour la reproductibilité, nous avons reproduit le travail des équipes 7, 25 et ... sélectionnées.
Pour la réplicabilité, nous intervenons comme une 30ᵉ équipe en proposant une nouvelle analyse du même jeu de données.

## Reproducibility

### How to Reproduce the Results
1. **Requirements**  
   - List dependencies and their versions (e.g., Python, R, libraries, etc.).
   - Specify any system requirements.

2. **Setting Up the Environment**  
   - Provide instructions for using the Dockerfile to create a reproducible environment:  
     ```bash
     docker build -t reproducible-project .
     docker run -it reproducible-project
     ```

3. **Reproducing Results**  
   - Describe how to run the automated scripts or notebooks to reproduce data and analyze results:
     ```bash
     bash scripts/run_analysis.sh
     ```
   - Mention Jupyter notebooks (if applicable):  
     Open `notebooks/reproduce_results.ipynb` to execute the analysis step-by-step.

4. **Automation (Bonus)**  
   - Explain the included GitHub Action that produces or analyzes data automatically.  
    
### Encountered Issues and Improvements
- Report any challenges, errors, or deviations from the original study.
- Describe how these issues were resolved or improved, if applicable.

### Is the Original Study Reproducible?
- Summarize the success or failure of reproducing the study.
- Include supporting evidence, such as comparison tables, plots, or metrics.

## Replicability

### Variability Factors
### Key Variability Factors

| Variability Factor | Possible Values | Why it Matters |
|--------------------|-----------------|----------------|
| **Skin Tone Operationalization** | `continuous`, `binary` | Teams used either raw ratings (continuous) or a categorical “dark vs light” variable, leading to different effect sizes. |
| **Outcome Definition / Model Type** | `logit` (red_dummy), `poisson` (redCards) | Red cards are rare events; logistic vs Poisson modeling can reverse effect signs or significance. |
| **Covariate Set** | `none`, `performance`, `full` | The biggest source of variability. Including or excluding performance/discipline controls drastically changes the estimated effect. |
| **Missing Data Strategy** | `dropna`, `mean` | Different teams handle missing player attributes differently, changing sample size and estimates. |

These four factors capture the essential "degrees of freedom" highlighted by Silberzahn et al. (2018).

---

### Constraints Across Factors

- **Logistic regression requires a binary outcome** → `if outcome = logit → use red_dummy`.
- **Poisson regression expects a count** → `if outcome = poisson → use redCards`.
- **Binary skin tone requires a threshold** (we use ≥ 0.5).
- **Covariates must exist in the dataset** → if `cov = none`, model becomes unadjusted.

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


### Does It Confirm the Original Study?
- Summarize the extent to which the replication supports the original study’s conclusions.
- Highlight similarities and differences, if any.

## Conclusion
- Recap findings from the reproducibility and replicability sections.
- Discuss limitations of your

