# Machine Learning

## Linear Discriminant Analysis
1. Linear Discriminant Analysis is a linear model for cclassification and dimensionality reduction. LDA mostly used for feature extraction in pattern classification problems. LDA projects data from a D dimensional features space down to a D' (D>D') dimensional space in a way to **maximize the variability between the classes and  and reducing the variablity within the classes**. 
2. Pros: (1) Handle the multiple classfication (>2 which is good for logistic regression); (2) Reduce the dimenstion as PCA; (3) Use on face detection algortihms.
3. Cons: (1) Not good on non-linear separate; (2) Not work well on number of features > number of observations.
4. Assumptions: (1) Normally distributed; (2) Each class has identical covariance matrix. LDA works well even assumptions violated.
5. Fisher's Linear Discriminant (FLD): LDA is a generialized form of FLD. The basic idea of FLD is to project data points onto a line to maximize the between-class scatter and minimize the within-class scatter. 

Note: LDA in R and Python are in the [LDA folder](https://github.com/rzhang0716/Data-Science/tree/master/Machine-Learning/Linear_Discriminant_Analysis)


## Imbalanced Data Handling
Most machine learning algorithms work best when the number of samples in each class is about equal as most algorithms are designed to maximize accuracy and reduce errors (loss functions). Class imbalance appears in many domains: fraud detection, spam filtering, disease screening, SaaS subscription churn, and advertising click-throughs. 

### Under-sampling
Advantages: It can help improve run time and storage problems by reducing the number of training data samples when the training data set is huge.
Disadvantages: (1) It can discard potentially useful information which could be important for building rule classifiers; (2) The sample chosen by random under-sampling may be a biased sample and it will not be an accurate representation of the population to cause the inaccurate results on the actual test data.

Remove random records from the majority classes, which can cause a loss of information. 
1.	Random Under-Sampling
Under-sampling can be a good choice when you have a ton of data – millions of rows. The drawback to under-sampling is that we are removing information that may be valuable. 
2.	Random under-sampling with imblearn
RandomUnderSampler is a fast and easy way to balance the data by randomly selecting a subset of data for the targeted classes. Under-sample the majority class(es) by randomly picking samples with or without replacement. 
3.	Under-sampling: Tomek links
Tomek links are pairs of very close instances but of opposite classes. Removing the instances of the majority class of each pair increases the space between the two classes, facilitating the classification process. Tomek’s link exists if the two samples are the nearest neighbors of each other. 
![image](https://user-images.githubusercontent.com/61474051/191805519-629bfa24-d71e-494a-b3a6-ec150af3cfa7.png)


