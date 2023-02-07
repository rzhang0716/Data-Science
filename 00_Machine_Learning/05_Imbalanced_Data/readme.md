# Imbalanced Data Handling
Most machine learning algorithms work best when the number of samples in each class is about equal as most algorithms are designed to maximize accuracy and reduce errors (loss functions). Class imbalance appears in many domains: fraud detection, spam filtering, disease screening, SaaS subscription churn, and advertising click-throughs. 


## I. Threshold-Moving for Imbalanced Classification
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
•	4. Use Adopted Threshold When Making Class Predictions on New Data. <br/>
    - 3a. Convert probabilities to Class Labels using the threshold.<br/>
    - 3b. Evaluate Class Labels.<br/>
    - 3c. If Score is Better than Best Score.<br/>
    - 3ci. Adopt Threshold. <br/> 


3. Optimal Threshold for ROC Curve
A ROC curve is a diagnostic plot that evaluates a set of probability predictions made by a model on a test dataset. The ROC curve is a useful diagnostic tool for understanding the trade-off for different thresholds and the ROC AUC provides a useful number for comparing models based on their general capabilities. 
The G-mean is a metric for imbalanced classification that, if optimized, will seek a balance between sensitivity and specificity. G-mean = sqrt(Sensitivity*Specificity).
4. Optimal Threshold for Precision-Recall Curve
Unlike the ROC curve, a precision-recall curve focuses on the performance of a classifier on the positive (minority class) only. Use F-measure to evaluate. 
F-measure = (2*Precision*Recall)/(Precision + Recall). 
5. Optimal Threshold Tuning
We can define a set of thresholds and then evaluate predicted probabilities under each in order to find and select the optimal threshold.  


## II. Under-sampling
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


## III. Over-sampling
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

## IV. Combining Random Oversampling and Undersampling
Oversampling can be applied to the minority class to improve the bias towards these examples, whilst also applying a modest amount of undersampling to the majority class to reduce the bias on that class. 


## V. Weighted columns
Weighting in predictive modeling may take multiple forms and occur at different steps in the model-building process. (1) When selecting observations to be used in model training; (2) During model training; (3) After model training, during model evaluation. \
Weighting can be applied in the last stage model evaluation: (1) Weighting by classification outcomes; (2) Weighting by observations. Specifically with the aim of identifying ideal cut-points for making class predictions. 
In spark, we could handle this by using column weights as extra columns to set different weights for the different classes in y. (c = # classes). 


## VI. Penalize Algorithms (Cost-Sensitive Training)
Use penalized learning algorithms that increase the cost of classification mistakes in the minority class. During training, we can use the argument class_weight = ‘balanced’ to penalize mistakes in the minority class by an amount proportional to how under-represent it is. Modify the probability=True if want to enable probability estimates for SVM algorithms.

Cost-sensitive learning is a subfield of machine learning that takes the costs of prediction errors into account when training a machine learning model. 
Most machine learning algorithms designed for classification assume that there is an equal number of examples for each observed class. Also, most machine learning algorithms assume that the prediction errors made by a classifier are the same, so-called miss-classifications. In cost-sensitive learning instead of each instance being either correctly or incorrectly classified, each class/instance is given a misclassification cost. Thus, instead of trying to optimize the accuracy, the problem is then to minimize the total misclassification cost. 
Majority class: negative or no-event assigned the class label 1. 
Minority class: Positive or event assigned the class label 0.

Cancer Diagnosis Problem: Consider a problem where a doctor wants to determine whether a patient has cancer or not. It is better to diagnose a healthy patient with cancer and follow up with more medical tests than it is to discharge a patient that has cancer. (False negative is related to the recall, which means increasing the recall (decrease the false negative), recall = TP/(TP+FN). Conversely, for marking values, we want to improve the precision if we want to decrease the false positive, make your model as correct as possible. Precision =  TP/(TP+FP).

In cost-sensitive learning, a penalty is associated with an incorrect prediction and is referred to as a “cost”. We could alternately refer to the inverse of the penalty as the “benefit”. 
Cost: The penalty associated with an incorrect prediction. 
The goal of cost-sensitive learning is to minimize the cost of a model on the training dataset, where it is assumed that different types of prediction errors have different and known associated costs. 
## VII. Cost-Sensitive Imbalanced Classification
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


## VII. Propensity Score Matching
Porpensity score matching (PSM) is a statistical matching technique (used on prospective data) that attempts to estimate the effect of a treatment, policy, or other intervention by accounting for the covariates that predict receiving the treatment. It is the probability of treatment assignment conditional on observed baseline covariates.
