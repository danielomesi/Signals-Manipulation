import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def main():
    func = lambda t: abs(t)
    x=PeriodicExtension(func,-1,2)
    DisplaySignalAndNthSignal(x,3,10)


def DisplaySignalAndNthSignal(x,T,N):
    Nthformula = lambda t: NthFourierSum(x,T,N,t)
    t=np.arange(-2,2,0.001)
    plt.plot(t,x(t),linewidth=2)
    plt.grid(True)
    plt.plot(t,Nthformula(t),linewidth=2,color="r")
    plt.show()
    res=Nthformula(283/140)
    print("Value of SN (t0+T/2N) when N=70, t0=2, T=3 is "+ str(res))


def PrintCoefficients(coefficients):
    print("Fourier Series Coefficients:")
    print("a0:", coefficients['a0'])

    for i, (a, b) in enumerate(zip(coefficients['a'], coefficients['b']), start=1):
        print("a{}: {}".format(i, a))
        print("b{}: {}".format(i, b))


def NthFourierSum(x,T,N,t):
    w0=2*np.pi/T
    coefficients=FourierRealCoeffList(x,T,N)
    sumRes=coefficients['a0']/2
    for index, item in enumerate(coefficients['a']):
        sumRes+=(item*np.sin((index+1)*w0*t))
    for index, item in enumerate(coefficients['b']):
        sumRes+=(item*np.cos((index+1)*w0*t))
    return sumRes

def PeriodicExtension(x,a,b):
    T=b-a
    x_=lambda t: x(a+(t-b)%T)
    return x_

def FourierRealCoeffList(x,T,N):

    w0=2*np.pi/T
    coefficients = {'a0': (0.0), 'a': [], 'b': []}
    
    # Calculate a0 coefficient
    integralResultForA0, _ = quad(x, (0), T)
    coefficients['a0'] = ((2) / T) * integralResultForA0

    # Calculate a and b coefficients
    for n in range(1, N + 1):
        integralResult, _ = quad(lambda t: x(t) * np.sin(w0*n* t), (0), T)
        an = ((2) / T) * integralResult
        integralResult, _ = quad(lambda t: x(t) * np.cos(w0*n* t), (0),T)
        bn = ((2) / T) * integralResult

        coefficients['a'].append(an)
        coefficients['b'].append(bn)

    return coefficients



def DisplaySignal(signal_func, N):
    x = np.linspace(-N, N, 10000)  # Generate x values from -N to N
    y = np.zeros_like(x)               # Initialize y values array

    for i, val in enumerate(x):
        if isinstance(val, np.ndarray):
            y[i] = signal_func(val)
        else:
            y[i] = signal_func(np.array([val]))

    plt.scatter(x, y)            # Scatter the signal
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('Signal Graph')
    plt.grid(True)

    # Set the y-axis limits
    y_extreme = np.max(np.abs(y))
    plt.ylim(-1.25 * y_extreme, 2 * y_extreme)

    plt.show()


if __name__ == "__main__":
    main()