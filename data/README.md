# Data — Mastery

> *"Models are only as good as the data they see. Data collection, quality, labeling, and feature design are where most production ML is actually won or lost."*

**Total time:** ~7–10 weeks
**Visual companion:** [The Map → Data Mastery](https://siddhant-rajhans.github.io/ml-roadmap/roadmap.html)

## What this unlocks

The most under-taught skill in ML. Most curricula bury data inside other modules and graduates can't ship because they've never built a dataset, diagnosed a distribution shift, or fixed mislabeled examples. This category fixes that.

## Topics

### Data Collection & Labeling · 2–3 weeks
*Build datasets from scratch. Design labeling pipelines. Understand where model failures come from — almost always the data.*

- Web scraping & APIs
- Labeling tools (Label Studio, Scale)
- Active learning for labeling
- Human-in-the-loop
- Synthetic data generation
- Crowdsourcing & quality control
- Data cards & documentation

### Data Quality & Distributions · 2 weeks
*Diagnose data problems before they become model problems. Understand distribution shift — the #1 reason deployed models degrade.*

- Data cleaning & imputation
- Class imbalance — SMOTE, class weights
- Outlier detection
- Train/val/test split — the right way
- Distribution shift types
- Covariate shift vs label shift
- Dataset versioning

### Feature Engineering · 2–3 weeks
*Make simple models perform like complex ones. Where domain expertise meets ML — and where Kaggle grandmasters live.*

- Encoding categoricals — target, ordinal, hash
- Scaling — StandardScaler vs RobustScaler
- Feature crosses & interactions
- Time-based features
- Embeddings for tabular
- Target encoding with regularization
- Automated FE (Featuretools)

### Data-Centric AI · 1–2 weeks
*Improving data > improving models. Confident learning, dataset debugging, slice-based evaluation.*

- Confident Learning
- Label error detection
- Cleanlab
- Data slicing & slice-based eval
- DataComp benchmark
- Curriculum Learning
- Data pruning & deduplication

## Where to go next

Pair `data` with `classical` first — the algorithms are simple, so data quality dominates outcomes. Then `dl` once you trust your pipeline.
