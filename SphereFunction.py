from Algorithm import minimize


def sphere(x):  # defines the cost function
    total = 0
    for i in range(len(x)):
        total += x[i]**2
    return total


initial_position = [-1.35, 2.59]  # [x1, x2]
constraints = [(-10, 10), (-10, 10)]  # [(x1_min, x1_max), (x2_min, x2_max)]
pso_simple_test = minimize(sphere, initial_position, constraints,
                           num_particles=50, maxiter=100, verbose=True)    # call the PSO algorithm
# print(pso_simple_test)
