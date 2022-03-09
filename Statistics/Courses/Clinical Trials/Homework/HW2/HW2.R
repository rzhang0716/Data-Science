# ST 520 HW2

# Q1(b)
# install.packages('Hmisc')
library(ggplot2)
library(lattice)
library(survival)
library(Formula)
library(Hmisc)
# Calculate the exact confidence interval
binconf(5,20,0.2,method='exact')

# Q1(c)
# When true probability equals 0.2 with 80% CI
x = 0:20
exact_CI <- binconf(x,20,0.2,method='exact')
exact_CI_upper <- exact_CI[,3]
exact_CI_lower <- exact_CI[,2]
# If consists 0.2, the upper bound should be bigger than 0.2 and lower bound smaller than 0.2
cover_X <- x[exact_CI_upper >= 0.2 & exact_CI_lower <= 0.2]
cover_X
# All probability when cover_X follows this binomial distribution
sum(dbinom(cover_X,20,0.2))

# Second part
# When true probability equals 0.5 with 80% CI
x1 = 0:20
exact_CI1 <- binconf(x1,20,0.2,method='exact')
exact_CI_upper1 <- exact_CI1[,3]
exact_CI_lower1 <- exact_CI1[,2]
# If consists 0.5, the upper bound should be bigger than 0.5 and lower bound smaller than 0.5
cover_X1 <- x[exact_CI_upper1 >= 0.5 & exact_CI_lower1 <= 0.5]
cover_X1
# All probability when cover_X follows this binomial distribution
sum(dbinom(cover_X1,20,0.5))