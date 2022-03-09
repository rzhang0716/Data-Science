#Question 1d
#Find the length of x;
sqrt(sum(5*5+1*1+3*3))
#Find the length of y;
sqrt(sum((-1)*(-1)+ 3*3 +1*1))
#Find xTy;
c1 <- c(5,1,3)
x <- matrix(c1,3,1)
c2 <- c(-1,3,1)
y <- matrix(c2,3,1)
t(x) %*% y

#Question 3a
#Extract the setosa species from iris data;
attach(iris)
SE <- iris[Species == "setosa", 1:4]
#Build the boxplot of setosa;
boxplot(SE, boxwex = 0.5, las=1, names=c("SL","SW","PL","PW"), main="setosa", 
        xlab="variables",ylab="y values")

#Extract the versicolor species from iris data;
VER <- iris[Species == "versicolor", 1:4]
#Build the boxplot of versicolor;
boxplot(VER, boxwex = 0.5, las=1, names=c("SL","SW","PL","PW"), main="versicolor", 
        xlab="variables",ylab="y values")

#Extract the virginica species from iris data;
VIR <- iris[Species == "virginica", 1:4]
#Build the boxplot of virginica;
boxplot(VIR, boxwex = 0.5, las=1, names=c("SL","SW","PL","PW"), main="virginica", 
        xlab="variables",ylab="y values")

#Question 3b
#load the library of ggplot2 and GGally;
library(ggplot2)
library(GGally)
#Make the pairs-plot of setosa;
ggpairs(SE)
#Make the pairs-plot of versicolor;
ggpairs(VER)
#Make the pairs-plot of virginica;
ggpairs(VIR)

#Question 3c
#Estimate the µ of setosa;
SE_means <- colMeans(SE)
SE_means
#Compute the sample covariance matrix;
SE_S <- cov(SE)
round(SE_S, 4)
#Compute the sample correlation matrix;
cor(SE)
#Sample size of setosa flowers;
SE_n <- nrow(SE)
#Estimate covariance of setosa;
round(SE_S/SE_n, 5)

#Estimate the µ of versicolor;
VER_means <- colMeans(VER)
VER_means
#Compute the sample covariance matrix;
VER_S <- cov(VER)
round(VER_S, 4)
#Compute the sample correlation matrix;
cor(VER)
#Sample size of versicolor flowers;
VER_n <- nrow(VER)
#Estimate the covariance of versicolor;
round(VER_S/VER_n, 5)

#Estimate the µ of virginica;
VIR_means <- colMeans(VIR)
VIR_means
#Compute the sample covariance matrix;
VIR_S <- cov(VIR)
round(VIR_S,4)
#Compute the sample correlation matrix;
cor(VIR)
#Sample size of virginica flowers;
VIR_n <- nrow(VIR)
#Estimate the covariance of virginica;
round(VIR_S/VIR_n, 5)

#Question 3d
#Yes, for all three species, there are positive correlation between any variables (lenth, width of
# Speal or Petal). But when we compare the pattern of them, the virginica has more corelated between
# variables, the setosa has the least correlation between variables.

#Question 4a
#Population: population consist of all skulls with epoch c4000BC;
#Parameter: true mean of mb, bh, bl, nh of all skulls with epoch c4000BC;
#Sample: sample consists of 30 epoch c4000BC for which data collected;
#Statistic: estimate the mean of mb, bh, bl, nh of all skulls with epoch c4000BC by sample mean.

#Question 4b
#Extract all data of c4000BC;
library(HSAUR3)
attach(skulls)
epoch_c4000 <- skulls[epoch == "c4000BC", 2:5]
#Estimate of the true mean of all skulls with epoch c4000BC;
epoch_c4000_mean <- colMeans(epoch_c4000)
epoch_c4000_mean 

#Question 4c
#Sample variance-covariance was used to estimate 
S_eopch_c4000 <- cov(epoch_c4000)
S_eopch_c4000

#Question 4d
#Sample size of c4000BC;
n_c4000 <- nrow(epoch_c4000)
#Estimate the population variance covariance of the population mean;
E <- S_eopch_c4000/n_c4000
E

#Question 4e
#According to the calculation, the matrix of A can be written as;
A <- matrix(c(1,0,0,-1,0,1,0,-1), nrow=2, ncol=4, byrow=TRUE)
A
#The covariacne of the estimator is:
A %*% E %*% t(A)

#Question 5a
# The basic difference between multivariate and longitudinal data is that 
# the order of the repeated measurements is essential in the analysis of 
# longitudial data, whereas permuting the order of the variables in multi
# -variate analysis yields same results. 

#Question 5b
# Because we want to know how variable and quantify how variablily between 
# two variables.

#Question 5c
# No, that only proves X and Y doesn't have linear realtionship, they may 
# have non-liner relationship.

#Question 5d
# No, as we know, the longitude data should be meausred as the same unit 
# at different time spots, however in problem 4 they did at the different
# spots, but the testing targets are different from each time tests.
