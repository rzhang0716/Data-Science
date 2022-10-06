# Tuning the hyperparameters of an estimator

## Scikit-Learn
### 1. Exhaustive Grid Search
The grid search provided by GridSearchCV exhaustively generates candidates from a grid of paramter values specified with the *param_grid* parameter. The 
GridSearchCV instance implements the usual estimator API when 'fitting' it on a dataset all the possible combinations of parameter values are evaluated and
the best combination is retained. 

### 2. Randomized Parameter Optimization
Randomized Parameter Optimization implements a randomized serach over parameters, where each setting is sampled from a distribution over possible parameter values. There are two benefits over an exhausive search: </br>
(1) A budget can be chosen independent of the number of parameters and possible values. </br>
(2) Adding parameters that don't influence the performance does not decrease efficientcy. 

### 3. Successive Halving
Successive halving (SH) is like a tournament among candidate parameter combinations. SH is an iterative selection process where all candidates (all combinations) are evaluated with a small amount of resources at the first iteration. Only some of these candidates are selected for the next iteration, which will be allocated more resrouces. </br>

![image](https://user-images.githubusercontent.com/61474051/194384473-71aa2940-385f-4c1d-b600-0aa1b7ff2040.png)

(1) *factor* controls the rate at which the resource grow, and the rate at which the number of candidates decreases. Factor is used to control number of samples increase ratio compared to each one before. </br>
(2) *min_resources* is the amount of resources allocated at the first iteration for each candidate. Number of samples starts from the first iteration. </br>
(3) *n_resources_i*: Amount of resources. n_resources_i = factor * min_resources, n_resources_{i+1} = n_resources_i * factor. 
(4) *resource*: Choose the reseource, default is number of samples. 

### 4. Notes
#### (1) Specifying an objective metric
By default, accuracy score is for classification and r2 is for regression. Score function can be defined based on different targets of the problem. 

#### (2) 





***
## Reference:
1. https://scikit-learn.org/stable/modules/grid_search.html
