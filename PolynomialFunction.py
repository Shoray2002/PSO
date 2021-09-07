from Algorithm import minimize

def poly(x):
    x=x[0]
    return x**2 + 2*x + 1

initial_position = [-1.35] 
constraints = [(-10, 10)]
pso_simple_test = minimize(poly, initial_position, constraints,
                           num_particles=50, maxiter=100, verbose=True)  