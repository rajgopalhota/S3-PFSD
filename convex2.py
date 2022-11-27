import cvxpy as cp

x = cp.Variable(1) # Real variable x
y = cp.Variable(1) # Real variable y

objective = cp.Minimize(x**2 + y**2) # Objective
constraints = []
constraints.append(x >= 0)
constraints.append(y >= 0)
constraints.append(x + y == 1)

problem = cp.Problem(objective, constraints)

opt = problem.solve()

print("Optimal solution: %f (x = %f, y = %f)" % (opt, x.value, y.value))