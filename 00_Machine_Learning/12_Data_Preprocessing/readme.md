# Data Preprocessing

## Feature Selection
### 1. Feature Selection Methods
**Feature Selection** methods are intended to reduce the number of input variables to those that are believed to be most useful to a model in order to predict the target variable. Mainly focused on removing non-informative or redundant predictors from the model. </br>

Feature selection methods can be divided into supervised and unsupervise. The difference is whether features are selected based on the target variable or not. Unsupervised methods remove redundant variables using correlation. Whereas supervised techniques use the target variable that remove irrelavent variables. Supervised can be further divided iuinto wrapper and filter methods.
(1) **Wrapper feature selection methods** create many models with different subses of input features and select those features that result in the best performing model according to a performance metric, such as recursive feature elimination (RFE). Wrapper methods evaluate multiple models using procedures that add and/or remove predicors to find the optimal combination that maximize model performance. </br>
(2) **Filter feature selection methods** use statistical techniques to evaluate the relationship between each input variable and the target variabe, and these scores are used as the basis to choose (filter) those input variables that will be used in the model. Filter methods evaluate the relevance of the predictors outside of the predictive models and subsequently model only the predictors that pass some criterion. </br>
(3) **Intrinsic featrure selection methods** There are some machine learning algorithms that perform feature selection automatically as part of learning the model. Such as penalized regression models like Lasso and decision trees, random forests etc. 

### 2. Statistics for Filter-Based Feature Selection Methods
It is common to use correlation type statistical measures between input and output variables as the basis for filter feature selection. The statistical measures used in filter-based feature selection are generally calculated one input variable at a time with the target variable.
![image](https://user-images.githubusercontent.com/61474051/194111880-6d35ecdf-de6b-426f-9a4f-27bf7b92effb.png)





***
## Notes
1. Most algorithms (linear regression, logistic regression, neural network, support vector machine, etc.) require some sort of the encoding on categorical variables. This is because most algorithms only take numerical values as inputs.

2. Algorithms that do not require an encoding are algorithms that can directly deal with joint discrete distributions such as Markov chain / Naive Bayes / Bayesian network, tree based, etc.

3. R is doing dummy coding for factors, which is almost one-hot encoding, but one class is used as a reference class. This means that for 𝑛 classes there will be 𝑛−1 binary indicator variables. For the reference class all these are 0. For any other class a single indicator will be 1 and the rest 0.

4. LabelEncoder in scikit-learn is for y only, as OneHotEncoder in scikit-learn now is supported for string input, no need labelencoder to convert strings to numbers.

5. Column Transformer. </br>
![Screen Shot 2022-10-05 at 12 35 26 PM](https://user-images.githubusercontent.com/61474051/194114104-c4d7bdfb-24ee-4e01-ad81-ce90f8ad512c.png)





***
## Reference
1. https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/
2. https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html
3. https://scikit-learn.org/stable/modules/preprocessing.html
