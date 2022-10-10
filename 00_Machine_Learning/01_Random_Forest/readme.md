<h1>Random Forest</h1>

## Random Forest Concept
1.	Is Random Forest performing well for imbalanced data? </br>
The Random Forest model is built on decision trees and decision trees are sensitive to class imbalance. Each tree is built on a “bag” and each bag is a uniform random sample from the data (with replacement). Therefore, each tree will be biased in the same direction and magnitude by class imbalance. 
We could use over/under-sampling and add weights to the tree splitting criterion to solve this problem. In Python, we could use class_weight from the RandomForestClassifier in scikit-learn. In R, we could use the Ranger library, to set the class.weights. 
2.	Does Random Forest require normalization?</br>
No, scaling is not necessary for the random forest. 
The nature of RF is such that convergence and numerical precision issues, can sometimes trip up the algorithms used in logistic and linear regression, as well as neural networks, which aren’t so important. Because of this, we don’t need to transform variables to a common scale as we did in neural networks.
Tree-based models do not care about the absolute value that a feature takes. They only care about the order of the values. Hence, normalization is used mainly in linear models/knn/neural networks because they are affected by the absolute values taken by feature(4).
3.	Is there any relation between the number of trees and the tree depth? Is it necessary that the tree depth should be smaller than the number of trees?</br>
There is no thumb ratio between the number of trees and tree depth. Generally, increasing the number of trees will improve the performance of the model, also with computational cost. Sometimes, after a certain amount of trees, the performance not increasing much.
The depth of the tree means the length of the tree you desire. A larger tree helps you to convey more info whereas a smaller tree gives less precise. So depth should large enough to split each node to your desired number of observations(6).


***
## Random Forest in Spark (PySpark)
1.	Imbalanced data could be implemented with weighted columns, with the weight_col in the random forest in Spark. See more in handle in imbalanced data for more details.
2.	Boolean data and categorical data should be converted into a string and then applied to the string index and one-hot encoding to prepare the data. Codes see reference 5. 
3.	We could use AUC to evaluate the performance of our prediction after weighted columns. Other metrics may not perform well due to imbalanced data. 
4.	We can run multiple times to average the results of feature importance from the random forest model at different seeds to decrease the influence of the random seeds. 


***
## Random Forest in Scikit-Learn
1.	How to improve the performance of random forests?<br/>
**n_estimators:** The number of decision trees in the random forest. <br/>
**max_depth:** The number of splits that each decision tree is allowed to make. If the number of splits is too low, the model underfits the data. If the number of splits is too high, the model overfits. <br/>
**max_features:** The number of features to consider when looking for the best split.  <br/>
**Bootstrap:** A bootstrapped model takes only a select subset of columns and rows to train each decision tree. Thus, the model becomes less prone to overfit the data. <br/>
**min_samples_split:** The minimum number of samples required to split an internal node. This can vary from considering at least one sample at each node to considering all of the samples at each node. When we increase this parameter, each tree in the forest becomes more constrained as it has to consider more samples at each node.<br/>
**min_samples_leaf:** The minimum number of samples required to be at a leaf node. This parameter is similar to min_samples_split, however, this describes the minimum number of samples at the leaves, the base of the tree.  

2.	Advantages of random forest<br/>
**Ease of building:** not having as many model assumptions and no normalization required. <br/>
**Feature importance:** can be obtained from random forests.<br/>
**Feature selection:** an extension of the feature importance. By calculating the feature importance, drop the less important features and decreased the dimensionality of the model to improve the accuracy and reduce training time. Another way of performing feature selection is by shuffling individual features in the data set recursively so that they lose the information provided by the column is destroyed. The model is evaluated on this modified dataset to see how the scores have been impacted. The more important the feature, the more profound its impact on the score(7).


***
## Feature Importance
### 1. Random Forest Built-in Feature Importance
**Gini Importance**: Aka mean decrease impurity, which is computed from the Random Forest structure. We can measure how each feature decrease the impurity of the split (the feature with highest decrease is selected for internal node). For each feature we can collect how on average it decreases the impurity. The average oover all trees in the forest is the measure of the feature importance. The drawbacks of the method is to tendency to prefer numerical featrures and categorical features with high cardinality. In the case of correlated features it can select one of the feature and neglect the importance of the second one. </br>
**Mean Decrease Accuracy**: This is used to compute the feature importance of permuted out-of-bag (OOB) samples based on mean decrease in the accuracy. But this one is ont implemented in the scikit-learn. 

### 2. Permutation Based Feature Importance
The permutation based importance can be used to overcome drawbacks of default feature importance computed with mean impurity decrease. This method will randomly shuffle each feature and compute the change in the model's performance. The features which impact the performance the most are the most important one. </br>
The permutation feature importance is defined to be the decrease in a model score when a single feature value is randomly shuffled. This procedure breaks the realtionship between the feature and the target, thus the drop in the model score is indicative of how much the model depends on the feature. 

### 3. SHAP
SHApley Additive exPlanations is a game theoretic approach to explain the output of any machine learning model. Also for tree ensemble methods, including XGBoost, LightGBM, CatBoost, scikit-learn and pyspark. See reference 5 for more about this method. 

***
## Visualize decision trees & random forest
### 1. Visualize using Matplotlib

### 2. Visualize using Graphviz
We can download the dot file and then install graphviz to read it and we can also using scikit-learn *export_graphviz* library to read it.

### 3. Using *dtreeviz*
This tool has multiple functions include more specific details, including show the prediction path, nodes, high deminsion figures etc. 


***
## Reference:
1. https://towardsdatascience.com/mastering-random-forests-a-comprehensive-guide-51307c129cb1
2. https://mljar.com/blog/feature-importance-in-random-forest/
3. https://scikit-learn.org/stable/modules/permutation_importance.html
4. https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html#sphx-glr-auto-examples-inspection-plot-permutation-importance-py
5. https://github.com/slundberg/shap
6. https://github.com/parrt/dtreeviz

