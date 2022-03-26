# Question 5
x<-NULL   #x is Acc
y<-NULL   #y is L
rate<-200 
hr0<-log(2)/5
hr1<-log(2)/5.92
hr2<-log(2)/7

f<-function(a,l){
  (1/3)*rate*(a-exp(-hr0*l)*(exp(hr0*a)-1)/hr0)+(1/3)*rate*(a-exp(-hr1*l)*(exp(hr1*a)-1)/hr1)+
    (1/3)*rate*(a-exp(-hr2*l)*(exp(hr2*a)-1)/hr2)-672
}

#min length of study
f1<-function(x){
  f(x,x)
}
z<-uniroot(f1,c(1,100))
upper<-z$root  
upper

#max accrual
f2<-function(y){f(5,y)}
uniroot(f2,c(0,15))$root

#minimum accrual
lower<-672/rate

n<-100  
for (i in 1:n){
  x[i]<-lower+i*(upper-lower)/n
  f3<-function(y){f(x[i],y)}
  v<-uniroot(f3,c(1,50))
  y[i]<-v$root
}
plot(x,y,type='l',xlab='accrual in years',ylab='length of study in years',col='red')


# Question 6 
library("survival")

# Part a
x <- read.table("calrisk.dat",header=TRUE) 
setwd("~/Downloads")
# x$V1: days on study
# x$V2: failure indicator   (1=d,0=c)
# x$V3: treatment indicator (1=trt3,0=trt2)
# risk: risk indicator
head(x)
km <- survfit(Surv(x$V1/365.25,x$V2)~x$risk)
plot(km,xlab="years",ylab="probability",lty=1:2,col=1:2)
legend(1,.3,c("(risk=0)",
              "(risk=1)"),
       lty=1:2,col=1:2)
lr <- survdiff(Surv(x$V1/365.25,x$V2)~x$risk)
lr
# Explanation: As p-value is smaller than 0.05 so that we reject Ho, the survival
# time on these two indicators are different. 


# Part b
# Sepearate data into 2 groups
x0 <- x[x$risk == 0,]
x1 <- x[x$risk == 1,]
# Plot 
km0 <- survfit(Surv(x0$V1/365.25,x0$V2)~x0$V3)
km1 <- survfit(Surv(x1$V1/365.25,x1$V2)~x1$V3)
par(mfrow=c(1,2))
plot(km0,xlab="years",ylab="probability",main='risk indicator 0',lty=1:2,col=1:2)
legend(1,.3,c("(trt2=0)",
              "(trt3=1)"),
       lty=1:2,col=1:2)
plot(km1,xlab="years",ylab="probability",main='risk indicator 1',lty=1:2,col=1:2)
legend(1,.3,c("(trt2=0)",
              "(trt3=1)"),
       lty=1:2,col=1:2)
par(mfrow=c(1,1))

lr0 <- survdiff(Surv(x0$V1/365.25,x0$V2)~x0$V3)
lr0
lr1 <- survdiff(Surv(x1$V1/365.25,x1$V2)~x1$V3)
lr1
# Explanation: As p-value 0.7 is greater than 0.05, so we fail to reject Ho when risk indicator is 0.
# As p-value is much smaller than 0.05, so we reject Ho when risk indicator is 1. 
# So for different groups of risk indicator, the survival is diffferent on risk indicaor is 1 
# not different on risk indicator is 0. 

