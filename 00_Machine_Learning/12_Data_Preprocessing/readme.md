# Data Preprocessing

## Feature Selection
### 1. Feature Selection Methods
**Feature Selection** methods are intended to reduce the number of input variables to those that are believed to be most useful to a model in order to predict the target variable. Mainly focused on removing non-informative or redundant predictors from the model. 


***
1. Most algorithms (linear regression, logistic regression, neural network, support vector machine, etc.) require some sort of the encoding on categorical variables. This is because most algorithms only take numerical values as inputs.

2. Algorithms that do not require an encoding are algorithms that can directly deal with joint discrete distributions such as Markov chain / Naive Bayes / Bayesian network, tree based, etc.

3. R is doing dummy coding for factors, which is almost one-hot encoding, but one class is used as a reference class. This means that for 𝑛 classes there will be 𝑛−1 binary indicator variables. For the reference class all these are 0. For any other class a single indicator will be 1 and the rest 0.

4. LabelEncoder in scikit-learn is for y only, as OneHotEncoder in scikit-learn now is supported for string input, no need labelencoder to convert strings to numbers.
