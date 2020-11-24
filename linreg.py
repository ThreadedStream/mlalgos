import numpy as np
import threading

'''
    Linear regression model

    First, define a linear function of the form:
    
    h(x) = t0 + t1*x + t2*x + t3*x 
    
    GOAL: Predict abovementioned function by computing parameters t

    HOW: By minimizing an error outputted by cost function

    J(t) = 1/2 * sum([(h(x[i]) - y[i]))**2 for i in range(n)])

    WHERE:
        n is a number of features
        t is a target parameter(to be more precise, the vector of parameters)

    For the sake of simplicity, i have concluded that 2 parameters would suffice

    FUNCTION TO COMPUTE PARAMETERS:

    t[j] = t[j] - alpha * d/dt[j](J(t))

    WHERE:
        j is an index for j-th parameter
        alpha is a learning rate
        d/dt[j] is a partial derivative with respect to j-th parameter

    COMPUTING DERIVATIVES:
    tx = t

    with respect to t0: (h(x[i]) - y[i])
    with respect to t1: (h(x[i]) - y[i]) * x 
'''

def h(x, t0, t1):
    return t0 + t1 * x


def J(x,y,t0,t1):
    return 1/2 * np.sum([(h(x[i],t0,t1) - y[i]) for i in range(3)])


def gradient_step(x,y,t0,t1,n, alpha):
    wt_resp_to_t0 = (t0 + t1 * x - y)
    wt_resp_to_t1 = (t0 + t1 * x - y) * x   
    
    for i in range(n):
        t0 = t0 - alpha * wt_resp_to_t0
        t1 = t1 - alpha * wt_resp_to_t1
    
    return (t0, t1)


def batch_gradient(points,t0,t1,iters,alpha):
    X = points[:, 0]
    Y = points[:, 1]

    for i in range(iters + 1):
        for j in range(X.size):
            t0, t1 = gradient_step(X[j], Y[j], t0,t1, X.size, 0.01)
        print(f't0: {t0}\nt1: {t1}\niter: {i + 1}')

    return (t0, t1)

if __name__ == '__main__':
    #Initializing points
    points = np.array([[1,2],
                       [3,4],
                       [5,6]])

    X = points[:, 0]

    #Initial guesses
    t0 = 0
    t1 = 0

    t0,t1 = batch_gradient(points,t0,t1,100000,0.01)

    new_ys = []
    for i in range(3):
        y = h(X[i], t0,t1)
        new_ys.append(y)

    print(f'Real ys:{points[:,1]}')
    print(f'Approximated ys: {new_ys}')

