# Linear Discriminant Analysis
Linear Discriminant Analysis is a linear model for cclassification and dimensionality reduction. LDA mostly used for feature extraction in pattern classification problems. LDA projects data from a D dimensional features space down to a D' (D>D') dimensional space in a way to **maximize the variability between the classes and  and reducing the variablity within the classes**. 

### Pros: </br>(1) Handle the multiple classfication (>2 which is good for logistic regression); </br>
(2) Reduce the dimenstion as PCA; </br> 
(3) Use on face detection algortihms.
### Cons: </br>(1) Not good on non-linear separate; </br>
(2) Not work well on number of features > number of observations.</br>
### Assumptions: </br>(1) Normally distributed; </br>(2) Each class has identical covariance matrix. LDA works well even assumptions violated.
## Fisher's Linear Discriminant (FLD)
LDA is a generialized form of FLD. The basic idea of FLD is to project data points onto a line to maximize the between-class scatter and minimize the within-class scatter. 
