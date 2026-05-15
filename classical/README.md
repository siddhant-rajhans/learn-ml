# Classical ML

> *"Before you run, walk. These algorithms power most of production ML. XGBoost wins structured-data competitions. SVMs are still in healthcare. This is not legacy — this is the foundation."*

**Total time:** ~20–28 weeks
**Visual companion:** [The Map → Classical ML](https://siddhant-rajhans.github.io/ml-roadmap/roadmap.html)

## What this unlocks

A solid mental model for what an ML model actually *is* before complexity hides it. Most production ML still leans on these techniques. Gradient boosting wins Kaggle. Probabilistic graphical models power speech and NER. Skipping classical is a common mistake — don't make it.

## Topics

### Supervised Learning · 4–6 weeks
*Solves 80% of real-world ML problems. Gradient boosting alone wins most structured-data competitions.*

- Linear Regression — as optimization
- Logistic Regression — derivation
- Decision Trees — information gain
- Random Forests — bias-variance decomposition
- Gradient Boosting — XGBoost, LightGBM, CatBoost
- SVM — margin maximization
- k-NN — curse of dimensionality
- Naive Bayes — why it works despite the assumption

### Kernel Methods · 2–3 weeks
*The mathematical bridge between linear methods and deep learning. Gaussian Processes are the Bayesian generalization of SVMs — and they're making a comeback.*

- Kernel trick — why it works
- Mercer's theorem
- RKHS — Reproducing Kernel Hilbert Spaces
- SVM — dual formulation
- Gaussian Processes
- Kernel PCA
- Radial Basis Functions
- Kernel approximations (Nyström, Random Fourier)

### Unsupervised Learning · 3 weeks
*Find hidden structure without labels. Understand how t-SNE and UMAP work — and when to distrust them.*

- K-Means — EM derivation
- Gaussian Mixture Models
- DBSCAN — density connectivity
- Hierarchical clustering
- PCA — as SVD
- t-SNE — gradient of KL divergence
- UMAP — Riemannian manifolds
- ICA — independent components
- Spectral clustering

### Probabilistic Graphical Models · 3–4 weeks
*Reason about uncertainty over structured outputs. HMMs and CRFs power speech recognition and NER.*

- Directed graphical models (Bayesian Networks)
- Undirected models (Markov Random Fields)
- d-separation & conditional independence
- Hidden Markov Models
- Conditional Random Fields
- Belief Propagation
- Variational Inference
- Expectation Maximization — derivation

### Reinforcement Learning · 4–6 weeks
*Build agents that learn from interaction. RL underlies RLHF, game-playing AI, robotics, and recommendation systems.*

- Markov Decision Processes
- Bellman equations
- Dynamic programming
- Q-Learning & DQN
- Policy Gradient theorem
- Actor-Critic methods
- PPO & TRPO
- Model-based RL
- Reward shaping
- Multi-armed bandits

### Time Series · 2–3 weeks
*Forecast anything temporal: stock prices, energy demand, user behavior, sensor data.*

- Stationarity & differencing
- ARIMA family
- Exponential smoothing
- State Space Models
- Kalman Filters
- Prophet
- Neural forecasting — N-BEATS, PatchTST
- Anomaly detection in time series

### Model Evaluation & Selection · 2 weeks
*Know when your model is actually good vs just memorized the training set. The most underrated skill in ML.*

- Cross-validation — stratified, time-series aware
- Bias-variance tradeoff
- Calibration — Platt scaling, isotonic
- ROC/AUC — what it actually means
- Precision/recall tradeoffs
- Statistical tests for model comparison
- Hyperparameter optimization — Bayesian search
- AutoML

## Where to go next

**[dl/](../dl/)**. Most deep learning concepts are direct generalizations of what lives here (linear regression → linear layers, logistic regression → softmax head, decision boundaries → manifolds).
