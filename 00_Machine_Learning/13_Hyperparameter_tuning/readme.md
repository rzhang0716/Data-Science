# Tuning the hyperparameters of an estimator

## Scikit-Learn
### 1. Exhaustive Grid Search
The grid search provided by GridSearchCV exhaustively generates candidates from a grid of paramter values specified with the *param_grid* parameter. The 
GridSearchCV instance implements the usual estimator API when 'fitting' it on a dataset all the possible combinations of parameter values are evaluated and
the best combination is retained. 
