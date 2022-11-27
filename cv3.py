import picos as pc

x = pc.RealVariable("x", 1) # Real variable x
y = pc.RealVariable("y", 1) # Real variable y

problem = pc.Problem()

problem.minimize = x**2 + y**2 # Objective
problem += x >= 0
problem += y >= 0
problem += x + y == 1

problem.solve(solver="cvxopt")

opt = problem.value

print("Optimal solution: %f (x = %f, y = %f)" % (opt, x, y))