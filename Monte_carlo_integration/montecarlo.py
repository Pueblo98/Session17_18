import numpy as np
import matplotlib.pyplot as plt

class MonteCarlo:
    def __init__(self,f,a,b):
        self.a = a
        self.b = b
        self.f = np.vectorize(f)
        
    def integrate(self,N):
        a = self.a
        b = self.b
        nums = np.random.uniform(a,b,N)
        total = np.sum(self.f(nums))
        I = ((b-a) / N) * total
        print(I)
        return I, nums
    
    def plot(self,N=100):
        a, b = self.a, self.b
        x = np.linspace(a, b, 1000)
        y = self.f(x)
        I, nums = self.integrate(N)
        sample_y = self.f(nums)

        plt.plot(x, y, label=r"$f(x) = x^2$")
        plt.scatter(nums, sample_y, s=10, label="Random Samples")
        plt.fill_between(x, y, alpha=0.3, label="Integration Area")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Monte Carlo Integration Visualization")
        plt.legend()
        plt.grid()
        plt.show()
    