# Machine Learning


## Imbalanced Data Handling
Most machine learning algorithms work best when the number of samples in each class is about equal as most algorithms are designed to maximize accuracy and reduce errors (loss functions). Class imbalance appears in many domains: fraud detection, spam filtering, disease screening, SaaS subscription churn, and advertising click-throughs. 


### I. Threshold-Moving for Imbalanced Classification
1. Converting Probabilities to Class Labels
The problem is that the default threshold may not represent an optimal interpretation of the predicted probabilities. 
(1) The predicted probabilities are not calibrated.
(2) The metrics used to train the model is different from the metric used to evaluate a final model.
(3) The class distribution is severely skewed. 
(4) The cost of one type of misclassification is more important than another type of misclassification. 
2. Threshold-Moving for Imbalanced Classification
The bottom line is that when studying problems with imbalanced data, using the classifiers produced by standard machine learning algorithms without adjusting the output threshold may well be a critical mistake. 
It has been stated that trying other methods, such as sampling, without trying by simply setting the threshold may be misleading.<br/>
•	1. Fit Model on the Training Dataset. <br/>
•	2. Predict Probabilities on the Test Dataset.<br/>
•	3. For each threshold in Thresholds:<br/>
    - 3a. Convert probabilities to Class Labels using the threshold.<br/>
    - 3b. Evaluate Class Labels.<br/>
    - 3c. If Score is Better than Best Score.<br/>
    - 3ci. Adopt Threshold.
•	4. Use Adopted Threshold When Making Class Predictions on New Data. <br/>

3. Optimal Threshold for ROC Curve
A ROC curve is a diagnostic plot that evaluates a set of probability predictions made by a model on a test dataset. The ROC curve is a useful diagnostic tool for understanding the trade-off for different thresholds and the ROC AUC provides a useful number for comparing models based on their general capabilities. 
The G-mean is a metric for imbalanced classification that, if optimized, will seek a balance between sensitivity and specificity. G-mean = sqrt(Sensitivity*Specificity).
4. Optimal Threshold for Precision-Recall Curve
Unlike the ROC curve, a precision-recall curve focuses on the performance of a classifier on the positive (minority class) only. Use F-measure to evaluate. 
F-measure = (2*Precision*Recall)/(Precision + Recall). 
5. Optimal Threshold Tuning
We can define a set of thresholds and then evaluate predicted probabilities under each in order to find and select the optimal threshold.  


### II. Under-sampling
Advantages: It can help improve run time and storage problems by reducing the number of training data samples when the training data set is huge.
Disadvantages: (1) It can discard potentially useful information which could be important for building rule classifiers; (2) The sample chosen by random under-sampling may be a biased sample and it will not be an accurate representation of the population to cause the inaccurate results on the actual test data.

Remove random records from the majority classes, which can cause a loss of information. 
1.	Random Under-Sampling
Under-sampling can be a good choice when you have a ton of data – millions of rows. The drawback to under-sampling is that we are removing information that may be valuable. 
2.	Random under-sampling with imblearn
RandomUnderSampler is a fast and easy way to balance the data by randomly selecting a subset of data for the targeted classes. Under-sample the majority class(es) by randomly picking samples with or without replacement. 
3.	Under-sampling: Tomek links
Tomek links are pairs of very close instances but of opposite classes. Removing the instances of the majority class of each pair increases the space between the two classes, facilitating the classification process. Tomek’s link exists if the two samples are the nearest neighbors of each other. 
4.	NearMiss
Instead of resampling the minority class, using distance, will make the majority class equal to the minority class. Compute the average distance to the minority point samples. 
Three versions:
(1)	Select samples from the majority class for which the average distance of the k nearest samples of the minority class is the smallest. (Close to the minority class)
(2)	Select samples from the majority class for which the average distance to the farthest samples of the negative class is the smallest.
(3)	2-step algorithm, First, for each negative sample, their m nearest neighbors will be kept. Then, the positive samples selected are the ones for which the average distance to the k nearest neighbors is the largest. 


### III. Over-sampling
Duplicate random records from the minority class can cause overfitting. 
Advantages: No information loss and outperforms under-sampling.
Disadvantages: Increase the likelihood of overfitting since it replicates the minority class events. 
1.	Random Over-sampling
The drawback of over-sampling is that can cause overfitting and poor generalization to the test data.  
2.	Random over-sampling with imblearn
Generate new samples by random sampling with replacement of the currently available samples.
3.	Synthetic Minority Oversampling Technique (SMOTE)
SMOTE works by randomly picking a point from the minority class and computing the k-nearest neighbors for this point. The synthetic points are added between the chosen point and its neighbors. SMOTE algorithm works in 4 simple steps:
(1)	Choose a minority class as the input vector
(2)	Find its k nearest neighbors (k_neighbors is specified as an argument in the SMOTE() function)
(3)	Choose one of these neighbors and place a synthetic point anywhere on the line joining the point under consideration and its chosen neighbor
(4)	Repeat the steps until the data is balanced

### IV. Combining Random Oversampling and Undersampling
Oversampling can be applied to the minority class to improve the bias towards these examples, whilst also applying a modest amount of undersampling to the majority class to reduce the bias on that class. 


### V. Weighted columns
Weighting in predictive modeling may take multiple forms and occur at different steps in the model-building process. (1) When selecting observations to be used in model training; (2) During model training; (3) After model training, during model evaluation. \
Weighting can be applied in the last stage model evaluation: (1) Weighting by classification outcomes; (2) Weighting by observations. Specifically with the aim of identifying ideal cut-points for making class predictions. 
In spark, we could handle this by using column weights as extra columns to set different weights for the different classes in y. (c = # classes). 


### VI. Penalize Algorithms (Cost-Sensitive Training)
Use penalized learning algorithms that increase the cost of classification mistakes in the minority class. During training, we can use the argument class_weight = ‘balanced’ to penalize mistakes in the minority class by an amount proportional to how under-represent it is. Modify the probability=True if want to enable probability estimates for SVM algorithms.

Cost-sensitive learning is a subfield of machine learning that takes the costs of prediction errors into account when training a machine learning model. 
Most machine learning algorithms designed for classification assume that there is an equal number of examples for each observed class. Also, most machine learning algorithms assume that the prediction errors made by a classifier are the same, so-called miss-classifications. In cost-sensitive learning instead of each instance being either correctly or incorrectly classified, each class/instance is given a misclassification cost. Thus, instead of trying to optimize the accuracy, the problem is then to minimize the total misclassification cost. 
Majority class: negative or no-event assigned the class label 1. 
Minority class: Positive or event assigned the class label 0.

Cancer Diagnosis Problem: Consider a problem where a doctor wants to determine whether a patient has cancer or not. It is better to diagnose a healthy patient with cancer and follow up with more medical tests than it is to discharge a patient that has cancer. (False negative is related to the recall, which means increasing the recall (decrease the false negative), recall = TP/(TP+FN). Conversely, for marking values, we want to improve the precision if we want to decrease the false positive, make your model as correct as possible. Precision =  TP/(TP+FP).

In cost-sensitive learning, a penalty is associated with an incorrect prediction and is referred to as a “cost”. We could alternately refer to the inverse of the penalty as the “benefit”. 
Cost: The penalty associated with an incorrect prediction. 
The goal of cost-sensitive learning is to minimize the cost of a model on the training dataset, where it is assumed that different types of prediction errors have different and known associated costs. 
#### VII. Cost-Sensitive Imbalanced Classification
Cost-sensitive learning for imbalanced classification is focused on first assigning different costs to the types of misclassification errors, then using specialized methods to take costs into account.
We can define the total cost of a classifier using Total Cost = C(0,1) * False Negatives + C(1,0) * False positives 
Cost-Sensitive Methods
1. Cost-Sensitive Resampling
In imbalanced classification, data resampling refers to techniques that transform the training dataset to better balance the class distribution, which include under-sampling and over-sampling. 
2. Cost-Sensitive Algorithms
Modified the class_weight parameters in the specified algorithms in scikit-learn and TensorFlow. 
3. Cost-Sensitive Ensembles
The simplest approach is the use of a machine learning model to predict the probability of class membership, then using a line search on the threshold at which examples are assigned to each crisp class label that minimizes the cost of misclassification. This is often referred to as “thresholding” or threshold optimization and is used more generally for binary classification tasks. 
MetaCost is a data preprocessing technique that relabels examples in the training dataset in order to minimize cost.  In MetaCost, first, a bagged ensemble of classifiers is fit on the training dataset in order to identify those examples that need to be relabeled, a transformed version of the dataset with relabeled examples is created, then the ensemble is discarded and the transformed dataset is used to train a classifier model. 
****


## Linear Discriminant Analysis
Linear Discriminant Analysis is a linear model for cclassification and dimensionality reduction. LDA mostly used for feature extraction in pattern classification problems. LDA projects data from a D dimensional features space down to a D' (D>D') dimensional space in a way to **maximize the variability between the classes and  and reducing the variablity within the classes**. 
Pros: (1) Handle the multiple classfication (>2 which is good for logistic regression); (2) Reduce the dimenstion as PCA; (3) Use on face detection algortihms.
Cons: (1) Not good on non-linear separate; (2) Not work well on number of features > number of observations.
Assumptions: (1) Normally distributed; (2) Each class has identical covariance matrix. LDA works well even assumptions violated.
Fisher's Linear Discriminant (FLD): LDA is a generialized form of FLD. The basic idea of FLD is to project data points onto a line to maximize the between-class scatter and minimize the within-class scatter. 

Note: LDA in R and Python are in the [LDA folder](https://github.com/rzhang0716/Data-Science/tree/master/Machine-Learning/Linear_Discriminant_Analysis)
****


## Random Forest

### Random Forest Concept
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


### Random Forest in Spark (PySpark)
1.	Imbalanced data could be implemented with weighted columns, with the weight_col in the random forest in Spark. See more in handle in imbalanced data for more details.
2.	Boolean data and categorical data should be converted into a string and then applied to the string index and one-hot encoding to prepare the data. Codes see reference 5. 
3.	We could use AUC to evaluate the performance of our prediction after weighted columns. Other metrics may not perform well due to imbalanced data. 
4.	We can run multiple times to average the results of feature importance from the random forest model at different seeds to decrease the influence of the random seeds. 


### Random Forest in Scikit-Learn
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
****



## Boosting
### The origin of Boosting
A weak hypothesis or weak learner is defined as one whose performance is at least slightly better than random chance. The idea is to use the weak learning method several times to get a succession of hypotheses, each one refocused on the examples that the previous ones found difficult and misclassified. 

### AdaBoost the First Boosting Algorithm
The weak learners in AdaBoost are decision trees with a single split, called decision stumps for their shortness. AdaBoost works by weighting the observations, putting more weight on difficult-to-classify instances and less on those already handled well. New weak learners are added sequentially that focus their training on more difficult patterns. This means that samples that are difficult to classify receive increasingly larger weights until the algorithm identifies a model that correctly classifies these samples. 
Predictions are made by the majority vote of the weak learners’ predictions, weighted by their individual accuracy. 

### How Gradient Boosting Works
1. Loss Function
The loss function used depends on the type of problem being solved. A benefit of the gradient boosting framework is that a new boosting algorithm does not have to be derived for each loss function that may want to be used, it is a generic enough framework that any differentiable loss function can be used. 
2. Weak Learner
Decision trees are used as the weak learner in gradient boosting. Initially, such as in the case of AdaBoost, very short decision trees were used that only had a single split, called a decision stump. Larger trees can be used generally with 4-to-8 levels. It is common to constrain weak learners in specific ways, such as a maximum number of layers, nodes, splits, or leaf nodes. This is used to keep learners remain weak but can still be constructed in a greedy manner.


3. Additive Model
Trees are added one at a time, and existing trees in the model are not changed. Like the gradient descent, the additional tree is added to the model to reduce the loss. This procedure is called functional gradient descent or gradient descent with functions. The output for the new tree is then added to the output of the existing sequence of trees to correct or improve the final output of the model. A fixed number of trees are added, or training stops once loss reaches an acceptable level or no longer improves on an external validation dataset. 

### Improvements to Basic Gradient Boosting
1. Tree Constraints
It is important that the weak learners have the skill but remain weak. A good general heuristic is that the more constrained tree creation is, the more trees you will need in the model, and the reverse, where less constrained individual trees, the fewer trees that will be required. 
•	Number of trees, generally adding more trees to the model can be very slow to overfit. The advice is to keep adding trees until no further improvement is observed. </br>
•	Tree depth, deeper trees are more complex trees, and shorter trees are preferred. Generally, better results are seen with 4-8 levels. </br>
•	Number of nodes or number of leaves, like depth, this can constrain the size of the tree but is not constrained to a symmetrical structure if other constraints are used. </br>
•	Number of observations per split imposes a minimum constraint on the amount of training data at a training node before a split can be constrained.</br>
•	Minimum improvement to loss is a constraint on the improvement of any split added to a tree. </br>
2. Weight Updates
The predictions to each tree are added together sequentially. The contribution of each tree to this sum can be weighted to slow down the learning by the algorithm. This weighting is called a shrinkage or a learning rate. The effect is that learning is slowed down, in turn, requires more trees to be added to the model, in turn taking longer to train, providing a configuration trade-off between the number of trees and learning rate. 
It is common to have small values in the range of 0.1 to 0.3, as well as values less than 0.1. 


3. Stochastic Gradient Boosting
A big insight into bagging ensembles and the random forest was allowing trees to be greedily created from subsamples of the training dataset. This can also be used to reduce the correlation between the trees in the sequence in gradient boosting models. 
At each iteration, a subsample of the training data is drawn at random (w/t replacement) from the full training dataset. The randomly selected subsample is then used, instead of the full sample to fit the base learner. 
Generally, aggressive sub-sampling such as selecting only 50% of the data has shown to be beneficial. 
4. Penalized Gradient Boosting
The leaf weight values of the trees can be regularized using popular regularization functions, such as L1 and L2. 


****



## Reference:
1.	https://www.datatrigger.org/post/spark_3_weighted_random_forest/
2.	https://www.bryanshalloway.com/2020/12/08/weighting-classification-outcomes/#weighted-classification-metrics
3.	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3912194/
4.	https://hersanyagci.medium.com/under-sampling-methods-for-imbalanced-data-clustercentroids-randomundersampler-nearmiss-eae0eadcc145
5.	https://machinelearningmastery.com/cost-sensitive-learning-for-imbalanced-classification/
6.	https://machinelearningmastery.com/framework-for-imbalanced-classification-projects/
7.	https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/
8.	https://stats.stackexchange.com/questions/242833/is-random-forest-a-good-option-for-unbalanced-data-classification
9.	https://stackoverflow.com/questions/8704681/random-forest-with-classes-that-are-very-unbalanced/8704882#8704882
10.	https://stackoverflow.com/questions/8961586/do-i-need-to-normalize-or-scale-data-for-randomforest-r-package
11.	https://datascience.stackexchange.com/questions/62031/normalize-standardize-in-a-random-forest
12.	https://github.com/rzhang0716/Data-Science/blob/master/Big_Data/Spark/PySpark/Random%20Forest/random_forest_pipeline.py
13.	https://stackoverflow.com/questions/34997134/random-forest-tuning-tree-depth-and-number-of-trees
14.	https://towardsdatascience.com/mastering-random-forests-a-comprehensive-guide-51307c129cb1
15.	https://medium.com/all-things-ai/in-depth-parameter-tuning-for-random-forest-d67bb7e920d#:~:text=the%20test%20performance.-,max_depth,the%20training%20and%20test%20errors.
16.	https://www.analyticsvidhya.com/blog/2020/03/beginners-guide-random-forest-hyperparameter-tuning/
17. https://machinelearningmastery.com/threshold-moving-for-imbalanced-classification/
18. https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/
