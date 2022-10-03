# Boosting

## Gradient Boosting
### 1. The origin of Boosting
A weak hypothesis or weak learner is defined as one whose performance is at least slightly better than random chance. The idea is to use the weak learning method several times to get a succession of hypotheses, each one refocused on the examples that the previous ones found difficult and misclassified. 

### 2. AdaBoost the First Boosting Algorithm
The weak learners in AdaBoost are decision trees with a single split, called decision stumps for their shortness. AdaBoost works by weighting the observations, putting more weight on difficult-to-classify instances and less on those already handled well. New weak learners are added sequentially that focus their training on more difficult patterns. This means that samples that are difficult to classify receive increasingly larger weights until the algorithm identifies a model that correctly classifies these samples. 
Predictions are made by the majority vote of the weak learners’ predictions, weighted by their individual accuracy. 

### 3. How Gradient Boosting Works
(1) Loss Function
The loss function used depends on the type of problem being solved. A benefit of the gradient boosting framework is that a new boosting algorithm does not have to be derived for each loss function that may want to be used, it is a generic enough framework that any differentiable loss function can be used. 
(2) Weak Learner
Decision trees are used as the weak learner in gradient boosting. Initially, such as in the case of AdaBoost, very short decision trees were used that only had a single split, called a decision stump. Larger trees can be used generally with 4-to-8 levels. It is common to constrain weak learners in specific ways, such as a maximum number of layers, nodes, splits, or leaf nodes. This is used to keep learners remain weak but can still be constructed in a greedy manner.


(3) Additive Model
Trees are added one at a time, and existing trees in the model are not changed. Like the gradient descent, the additional tree is added to the model to reduce the loss. This procedure is called functional gradient descent or gradient descent with functions. The output for the new tree is then added to the output of the existing sequence of trees to correct or improve the final output of the model. A fixed number of trees are added, or training stops once loss reaches an acceptable level or no longer improves on an external validation dataset. 

### 4. Improvements to Basic Gradient Boosting
(1) Tree Constraints </br>
It is important that the weak learners have the skill but remain weak. A good general heuristic is that the more constrained tree creation is, the more trees you will need in the model, and the reverse, where less constrained individual trees, the fewer trees that will be required. 
•	Tree depth, deeper trees are more complex trees, and shorter trees are preferred. Generally, better results are seen with 4-8 levels. </br>
•	Number of nodes or number of leaves, like depth, this can constrain the size of the tree but is not constrained to a symmetrical structure if other constraints are used. </br>
•	Number of observations per split imposes a minimum constraint on the amount of training data at a training node before a split can be constrained.</br>
•	Minimum improvement to loss is a constraint on the improvement of any split added to a tree. </br>
•	Number of trees, generally adding more trees to the model can be very slow to overfit. The advice is to keep adding trees until no further improvement is observed, _n_estimators_ in python. </br>
• Number of samples: Tree is fitted on the random subset of the samples. _sub_sample_ </br>
• Number of Features: Number of features used by each tree and specified by _max_features_ </br>
• Learning Rate" Controls the amount of contribution that each model has on the ensemble prediction. Smaller rate requires more decision trees while large rate require small value. _learning_rate_ </br>

(2) Weight Updates
The predictions to each tree are added together sequentially. The contribution of each tree to this sum can be weighted to slow down the learning by the algorithm. This weighting is called a shrinkage or a learning rate. The effect is that learning is slowed down, in turn, requires more trees to be added to the model, in turn taking longer to train, providing a configuration trade-off between the number of trees and learning rate. 
It is common to have small values in the range of 0.1 to 0.3, as well as values less than 0.1. 


(3) Stochastic Gradient Boosting
A big insight into bagging ensembles and the random forest was allowing trees to be greedily created from subsamples of the training dataset. This can also be used to reduce the correlation between the trees in the sequence in gradient boosting models. 
At each iteration, a subsample of the training data is drawn at random (w/t replacement) from the full training dataset. The randomly selected subsample is then used, instead of the full sample to fit the base learner. 
Generally, aggressive sub-sampling such as selecting only 50% of the data has shown to be beneficial. 

(4) Penalized Gradient Boosting
The leaf weight values of the trees can be regularized using popular regularization functions, such as L1 and L2. 

***
## XGBoost


***
## LightGBM


***
## CatBoost



***
## Reference: https://machinelearningmastery.com/gradient-boosting-machine-ensemble-in-python/
