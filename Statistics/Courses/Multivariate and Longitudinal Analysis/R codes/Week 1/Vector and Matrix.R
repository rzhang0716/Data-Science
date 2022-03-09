#Create the vector;
x <- c(0.71, 0.61, 0.72, 0.83, 0.92)
print(x)
#View x in a matrix;
as.matrix(x)
#Take the transpose of x;
t(x)
#Addition and subtraction of two vectors;
a <- c(0.71, 0.61, 0.72, 0.83, 0.92)
b <- c(0.63, 0.69, 0.77, 0.80, 1.00)
a+b
a-b
#Vector multiplication;
# %*% used on matrix multiplication;
t(a) %*% b
#Add the column in a matrix;
M <- cbind(c(0.71, 0.61, 0.72, 0.83, 0.92), c(0.63, 0.69, 0.77, 0.80, 1.00))
M
#Determinants of matrix
D <- matrix(c(5,3,9,6),2,2)
D
det(D)