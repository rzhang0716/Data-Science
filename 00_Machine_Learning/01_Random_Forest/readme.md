<h1 align="center">Random Forest</h1>

## Random Forest Concept
1.	Is Random Forest performing well for imbalanced data?
The Random Forest model is built on decision trees and decision trees are sensitive to class imbalance. Each tree is built on a “bag” and each bag is a uniform random sample from the data (with replacement). Therefore, each tree will be biased in the same direction and magnitude by class imbalance. 
We could use over/under-sampling and add weights to the tree splitting criterion to solve this problem. In Python, we could use class_weight from the RandomForestClassifier in scikit-learn. In R, we could use the Ranger library, to set the class.weights. 
2.	Does Random Forest require normalization?
No, scaling is not necessary for the random forest. 
The nature of RF is such that convergence and numerical precision issues, can sometimes trip up the algorithms used in logistic and linear regression, as well as neural networks, which aren’t so important. Because of this, we don’t need to transform variables to a common scale as we did in neural networks.
Tree-based models do not care about the absolute value that a feature takes. They only care about the order of the values. Hence, normalization is used mainly in linear models/knn/neural networks because they are affected by the absolute values taken by feature(4).
3.	Is there any relation between the number of trees and the tree depth? Is it necessary that the tree depth should be smaller than the number of trees?
There is no thumb ratio between the number of trees and tree depth. Generally, increasing the number of trees will improve the performance of the model, also with computational cost. Sometimes, after a certain amount of trees, the performance not increasing much.
The depth of the tree means the length of the tree you desire. A larger tree helps you to convey more info whereas a smaller tree gives less precise. So depth should large enough to split each node to your desired number of observations(6).


## Random Forest in Spark (PySpark)
1.	Imbalanced data could be implemented with weighted columns, with the weight_col in the random forest in Spark. See more in handle in imbalanced data for more details.
2.	Boolean data and categorical data should be converted into a string and then applied to the string index and one-hot encoding to prepare the data. Codes see reference 5. 
3.	We could use AUC to evaluate the performance of our prediction after weighted columns. Other metrics may not perform well due to imbalanced data. 
4.	We can run multiple times to average the results of feature importance from the random forest model at different seeds to decrease the influence of the random seeds. 


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
