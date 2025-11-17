## Replicability

### Variability Factors (Essential)

---

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

### How to Run Variants (Docker)

General syntax:

```bash
docker run --rm rep-study \
    --outcome <logit|poisson> \
    --skin <continuous|binary> \
    --cov <none|performance|full> \
    --missing <dropna|mean>
```
Examples (dans la racine du projet):
```bash
docker build -t rep-study -f replicability/Dockerfile .
docker run --rm rep-study \
    --outcome logit --skin continuous --cov performance
```
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
