from numpy import*

def sigm(x):
    return (1+exp(-x))**(-1);

def layer(W,f,x):
    Y=dot(W,x);
    return f(Y);

a=arange(15).reshape(3,5);
x=arange(5);
y=layer(a,sigm,x);

    
