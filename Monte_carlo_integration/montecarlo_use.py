from montecarlo import MonteCarlo

test = MonteCarlo(lambda x:x**2,2,3)
result = test.integrate(10)
test.plot()
