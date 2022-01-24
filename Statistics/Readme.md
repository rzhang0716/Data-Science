## Basic Concepts
1. Population: The collection of all subjects of interest.
2. Sample: A subgroup of population from what we collect information.<br>
3. Sample Size: The number of subjects in a sample.<br>
4. Sample space: A list of all possible outcomes. <br>
5. Parameter: Any summaries obtained from population.<br>
6. Statistics: Any summaries obtained from sample. <br>
7. Outlier: Extreme data which are not in the main body of the distribution.<br>
8. Leverage: Measure how far away the independent variable values of an observation from other observations. If deleting the leverage point can change the estimate a lot, then this is called influential point.<br>
9. Deviation: The difference between the observation and the mean. <br>
10. Degrees of freedom: Numbers of observations that can be freely changed in a sample.<br>
11. Standard deviation: A measure of the amount of variation or dispersion of a set of values. Only used as a measrue of spread when mean is used as the measure of center. <br>
12. Event: Any combinations of outcomes.<br>
13. Central Limit Theorem: When sample size is sufficiently large, the sample distribution of the sample mean always follows normal distribution.<br>
14. Law of large numbers: When sample size tends to infinitely, sample mean equals the population mean. <br>
15. If repeated samples were taken and the 95% confidence interval was computed for each sample, then 95% of these confidence intervals cover the true mean.
16. Power: related to the effect size (positive), sample size (positive), within group variance (negative). 


## Hypothesis Test
1. Definition: Hypothesis test is an inference tool that examines if the hypotheses are supported by the sample data.
2. Hypothesis types: (1) Equality: Not too much difference on two treatments. (2) Non-inferiority: Aim to show the experiment is not worse than standards. (3) Superiority: Experiment is better than the standard. <br>
3. Statistical Hypothesis procedures: (1) State the null hypothesis and the alternative hypothesis; (2) Specify the significance level; (3) Calculate the test statistics; (4) Calculate the p-value and reject region; (5) State the conclustion. <br>
4. Hypothesis requirements: Must be specified in terms of parameters; (2) Must be in pair.<br>
5. Test statistics: The numerical summary of the data, which aims to measure the distance between what is observed in the sample data and what is expected under H0. <br>
6. p-value: Probability of the observed data if H0 is ture, which used to quantify the statistical significance. <br>
7. Steps for calculating the power: (1) Obtain the value for mean under H0 and Ha; (2) Superimpose the distribution of the sample mean under H0 and Ha; (3) Identify the reject region with respect to sample mean under H0; (4) Identify the region corresponding to power with respect to sample mean distribution under Ha and compute the corresponding area. <br>


## ANOVA 
1. Assumptions: (1) All samples means are normally distributed; (2) K samples are independent to each other; (3) Variance of all populations are equal.
2. Implement ANOVA: (1) Specify H0 and Ha; (2) Specify the significance level; (3) Compute test statistics; (4) Compute p-value and draw conclusion. <br>
3. Idea of ANOVA: Interest in test the euqality for K means but carry the analysis of variance. Because if all means are equal, the variance among all populations should be small. We use the within-group variance as a reference as ANOVA assumes equally between group variance.<br>
4. Disadvantage of ANOVA: It cannot tell which one is different. Therefore, we need further pair-wise comparison to find the different one.<br>
5. Two-way ANOVA: If a quantitative outcome and two categorical variables.
6. Simple Effect: Describe the difference among cell means associated with that factor at a single level of the other factors.
7. Main Effect: Describe the difference among the marginal means associated with each levvel of an experimental factor. 
8. Interaction Effect: Difference of differences, a measure of how one factor affects the simple effects of other factors. 
9. MANOVA: ANOVA with several dependent variables (multiple y). <br>
10. Multiple comparisos:(1) Bonferroni procedure; (b) Tukey Procedure; (c) Scheffe Procedure. <br>
11. ANCOVA: Including covariates in ANOVA models, using a covariate that accounts for heterogeneity among EUs to reduce experiemental error and hence increasing precision. 

## Linear Regression
### Simple Linear Regression
1. Simple Linear Regression (SLR): (1) Intercept: Expected value of y when X = 0; (2) Slope: Expected change in Y relative to one unit change of X; (3) Random Error: The difference between observed and expected y values.
2. SLR assumptions: (1) Linearity; (2) Equal Variance; (3) Independent; (4) Normally distributed; (5) Predictors w/t error. 
3. Procedures of SLR: (1) Make a scatter plot of the data; (2) Fit the linear regression line; (3) Aceess the fitness of the regression line and verity model assumptions; (4) Perform inference.
4. Estimating method of SLR: Leaset squrare error.
5. R^2 (Coefficient of determinatio): Proportion of the total variance in Y that can be explained by the regression model. 
6. Assumptions check: (1) Constant variance: Residuals vs. fitted values; (2) Linearity: Residuals vs. Predictors; (3) Independence: Residuals vs variables not in the model; (4) Normally distributed: QQ plot.
7. Consequence of violation: (1) Linear: Model Garbage; (2) Independece/Constant variance: Inference not trust (Try transformation log or square root); (3) Normally distributed: Minimal.

### Multiple Linear Regression
1. Coefficients explanation: The coefficients associated with the predictor xj is the slope of the linear association between y and xj while accounting for the effects of other predictors in the model.
2. Interaction interpretation: The partial coefficient associated with an interaction between two predictors quantifies the effect that predictor A has on the  linear association between predictor B and the response. 
3. Procedures: (1) Fit the full model (all variables included); (2) Fit the reduced model (set some variables coefficients as 0); (3) Calculatet F-test; (4) Draw conclusion, H0 is no difference between full and reduced model. 
4. Steps build regression: (1) Examine univariate summaries of the data and identify unusual values; (2) Examine scatterplots with all variables to find correlated variables; (3) Identify a model that includes relavent varibales based on domain knowledge; (4) Check the assumptions about the model; (5) Examine the collinearity using VIF (variance inflation factor), it indicates strong collinearity if VIF > 10; (6) Based the model to predict and test after stepwise selection. 
5. Model evaluation metrics: (1) Adjusted R^2: A penalized version of R^2 that imposes a penalty for each additional parameter added to the model; (2) PRESS statistics (Predicted Sum of Squares): Each time remove a data point, then train the model based on the rest of data points to predict the removed points; (3) AIC: A penalized goodness of fit measure, smaller is better.


## Logistic Regression
1. Odds and log odds: odds = p/(1-p); log odds = logit = ln[p/(1-p)], converting probabilites to log odds.
2. Explanation: For given variable one, increasing variable 2 by on unit will increase/decrease the log odds of survival by XX. 
3. Coefficient explanation: Hold all other predictors constant and increase the predictor xi by 1, then the predicted odds of success are multipled by the factor e^beta.
4. Cost Function: Logit. 


## Longditudinal Analysis
### Introduction
1. Basic Concepts:(1) **Response** is the outcome of interest; (2) **Unit** is the object on which repeated measurements are taken, typically are individuals; (3) **Time** is the generic term for the condition of measurement, consider as an important covariate in longitudinal data. 
2. Balanced design vs. Unbalance design: If all units have same number of repeated measurements. (Each unit has same measurements at each time point)
3. Regular design vs. Irregular design: The times of measurements are the same for all units. (Each unit has same time points measurements).
4. For unbalance and irregular design, we should use pivot-longer for long-format table. 
5. Auto-correlation: The correlation between the repeated measurements when the 'lag', or distance between the time, is constant. Measures the variable's current value to the past value. 

### Models for mean and covariance
1. Mean describes how the response changes on average over time. Overall, the mean can be thought of as a function of time: µj = µ(tj).
2. Three main steps in modeling longitudinal data: (1) Modeling the mean; (2) Modeling the covariance; (3) Select the distribution of the data Y. 


## Clinical Trials
### Phase I 
1. Definition: The first studies in which a new drug is administered to a small number of human subjects with increasing does of drug. To explore tolerance does for further experimentation. 
2. Objectives: (1) Determine a 'safe', 'tolearance' does; (2) Develop an appropriate schedule of administration; (3) Gain understanding of the pharmacology of the drug; (4) Need to examine interaction effects for safety profile and proper labeling. 
3. Features: (1) Do this in a timely manner, using a small number of subjects (10~15); (2) Most are not comparative but rather are informational; (3) Interaction studies are comparative but not aimed for efficiency. 

### Phase II
1. Objectives: To determine whether the new treatment should be used in a large-scale comparative study.  (1) Feasibility of treatment; (2) Side effects and toxicity; (3) Logistics of administration and cost. 
2. Major issues to address: Is there eneough evidence of efficiency of the new drug?
3. Surrogate markers: An outcome that can be measured quickly and is believed to be related to the clinical outcome. Eg: Lung cancer drug effect on tumor shrinkage. 
4. Goal: To estimate the effect of the new drug on some endpoint with enough precision to decide whether we investigate the new drug in Phase III.

##### Gehan's Two Stage Design
1. Goal: To discard ineffective treatment early.
2. Stages:(1) Give the new treatment to number of n0 patients. If no patient responds, declare the treatment is ineffective. (2): If at least one patient  responds in Stage I, add n- n0 patients and count the total number of patients responding to the new treatment. Calculate the point estimate of pi and construct the confidence interval. 
3. Determine n0 and n. (1) 𝞹0 denotes as the minimal efficacy, ɑ0 denotes as tolerance; (2) First if (1-𝞹)no <= ɑ0 we need n0 >= log(ɑ0)/log(1-ɑ0) to find n0; (3) Determine n based on confidence interval z(p*(1-p)/n)= interval. 

#### Simon's Two Stage Design
1. Stages: (1) N1 patients are given treatment in the first stage. (1a) If r1 or less respond, then decalre the treatment is a failure and stop. (1b) If more than r1 respond, then add (n-n1) additional patients for a total of n patients. (2) If the total number that respond among all n patients is greater than r, then declare the treatment a success; otherwise, declare the treatment is fail. 
2. Declare the treatment is failure if (X1 <= r1) or {(X1>r1) and (X1 + X2 <= r); Declare the treatment is sucess if {(X1 > r1) and (X1+X2 > r)}.
3. Design contains: Type I and Type II error. 

### Phase III
Definition: Comparison of new intervention to the current standard of treatment with respect to efficacy and toxicity. 

## Survival Analysis
1. 

## Multivariate Analysis
1.

