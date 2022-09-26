#Question 1a & 1b
#Load the data in R and assign as data;
data <- read.table("https://www.stat.ncsu.edu/people/maity/courses/st537-S2019/data/T4-3.DAT",header = F)
#Remove the twi two outliers #9 and #16 rows;
new_data <- data[-c(9,16),]
#Attach the new data;
attach(new_data)
#Perform the Shapiro-Wilk tests;
apply(new_data[, 1:4], 2, shapiro.test)
#Load the MVN library;
library(MVN)
#Perform Roystpn's tests on new data and create a chi-square plot;
mvn(new_data[, 1:4], mvnTest = "royston", multivariatePlot = "qq")
# Question 1c
# Shaprio-Wilk test shows that all test p-value is far larger than the significance level, 
# which represents all follow normal distribution without rejecting hypothesis test.

# Royston's test also show that the p-value is higher than the significane level, 
# which proves that all 4 variables follow normal distribution.

# As the most (above 95%) points are located in the eclipses pattern, it suggest that the distribution
# of normality.

#Question 2a
#Load the library of HSAUR3;
library(HSAUR3)
#attach the data;
attach(skulls)
#Extract the c4000BC epoch from the data;
c4000BC <- skulls[epoch=="c4000BC",2:5]
c4000BC
#Create the pairs-plot;
library(ggplot2)
library(GGally)
ggpairs(c4000BC)

# mb has positive correlations to the other variables, however, bl has a negative correlation
# to the nh. Besides, the mb and nh has a strong positive linear relationship here. 

#Question 2b
#x: data matrix;
x <- c4000BC
#number of variables;
p <- ncol(x)
#sample size;
n <- nrow(x)
# xbar and s;
xbar <- colMeans(x)
s <- cov(x)
#Mahalanobis distance;
x.cen <- scale(x, center=T, scale =F)
d2 <- diag(x.cen %*% solve(s) %*% t(x.cen))
#chi-square quantiles
qchi <- qchisq((1:n - 0.5)/n, df=p)
#sorted d^2 value;
sortd <- sort(d2)
#plot the chi-square;
plot(qchi, sortd, pch=19, xlab="Chi-square quantiles", ylab = "Mahalanobis squared
distances", main="Chi-square QQ plot")
#Add the line;
abline(0,1)

# As we draw the line of 45 degree, we found that almost all points are laid closely to
# the line, except the point in the right corner. As that point is not very influencial 
# to the whole trendline, so we can still think the variables are normally distributed.

#Question 2c
#Calculate the z scores for each variable;
z1 <- scale(c4000BC[,1],scale=T)
z2 <- scale(c4000BC[,2],scale=T)
z3 <- scale(c4000BC[,3],scale=T)
z4 <- scale(c4000BC[,4],scale=T)
#Attach the Mahalanobis distances to the z score table;
c4000BC_1 <- cbind(z1,z2,z3,z4,d2)
colnames(c4000BC_1) <- c("z1","z2","z3","z4","d2")
#Sort by d2;
c4000BC_sort <- c4000BC_1[order(d2 ,decreasing=TRUE), ]
#Look for the first two rows of data;
head(c4000BC_sort,2)

#For this sorting data, the first two data are 29 and 12. For data 29, z1 and z2 are good, z3 is a 
# bit of far but z4 is extremely far from the original point. For data 12, z1, z3 and z4 are good,
# but the z2 is relatively far from the original point.

#Question 2d
#Perform the univariate Shapiro-Wilk test;
apply(c4000BC[,1:4], 2, shapiro.test)
#Perform the Royston tests;
mvn(c4000BC[,1:4], mvnTest = "royston")

# Question 3a
#Load the library;
library(mnormt)
#Generate 100 points and named as z_1;
data3 <- rmnorm(100, mean=rep(1,2), varcov=cbind(c(1,1),c(1,2)))
data3

# Question 3b
#Load the library;
library(car)
#Assign the value as x1 and x2;
x1 <- data3[,1]
x2 <- data3[,2]
#Make a scatter plot of x1 and x2;
plot(x1,x2)
#Overlay data ellipse (50%, 95%);
dataEllipse(x1,x2,xlim=c(-2,5), ylim=c(-3,8), pch=20, col=c("red", "green"), 
            ellipse.label = c(0.5,0.95), levels=c(0.5,0.95), fill=TRUE, fill.aplpha=0.1)

# It is an ellipse pattern;

# Question 3c
cor(x1,x2)
#Y = X1 + X2
# The mean of Y is the sum of expect value of X1 and X2
miu_Y <- 1 + 2
miu_Y
# The variance of Y is the sum of variance of X1, X2 and the double covariance;
Var_Y <- 1 + 2 + 1*2
Var_Y
# Y is follows the normal distribution with mean of 3 and variance of 5, Y ~ N(3,5)

#Question 3d
#As the sample used on part a, the sample y is;
y <- x1 + x2
# Sample mean and standard deviation of y;
xbar <- mean(y)
std <- sd(y)
# Plot a hist and overlay by a normal dis;
xx <- seq(xbar-3*std, xbar+3*std, len = 101)
yy <- dnorm(xx, mean = 3, sd = sqrt(5))
hist(y, probability = TRUE, xlim = range(xx), main="Histogram and fitted normal pdf")
lines(xx, yy, lwd=3)

# Estimated density vs normal dist pdf
den.est <- density(y, bw=1)
lines(den.est, lwd=3, col="red")
legend(x=4.5, y=0.19, legend=c("Estimated pdf", "Fitted normal pdf"),col=c("black","red"),
       lwd=3, lty=2, cex=0.70)

# I am expecting to see a normal distribution with a bell shape, and the curve matches my 
# expectation. The estimated pdf is close to the fitted curve. As X1 and X2 are joint random
# variables, the sum of them should also be a normal distribution with mean of the sum of the 
# X1 and X2 and variance of the sum of their variance plus double covariance. 

# Question 4a 
# See attachment;
# Question 4b
#Generate 100 random points;
data4 <- rmnorm(100, mean=c(1,2,3), varcov=cbind(c(2,1,1),c(1,1,1),c(1,1,3)))
# Compute the sample correlation matrix
cor1 <- cor(data4)
cor1

# Find the Z_1, Z_2 and Z_3;
Z_1 <- sapply(data4[,1], function(x) (x-1)/sqrt(2))
Z_2 <- sapply(data4[,2], function(x) (x-2)/sqrt(1))
Z_3 <- sapply(data4[,3], function(x) (x-3)/sqrt(3))
# Compute the covariance matrix;
cov2 <- cov(cbind(Z_1,Z_2,Z_3))
cov2
# Compare the covriance and correlation;
identical(cor1, cov2)
# They are close but different, as the samples are picked from the population randomly, 
# random samples give different data cannot be idealy exact match the thorey. However, 
# as the simulation times increased, the result of them should be closer and closer.