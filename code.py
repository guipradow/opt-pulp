import pulp as pl

# Create model
model = pl.LpProblem('Example', pl.LpMaximize)

# Define variables
x = pl.LpVariable('x', 0, 10)
y = pl.LpVariable('y', 0, 10)

# Define constraints
model += -x + 2*y <= 8
model += 2*x + y <= 14
model += 2*x - y <= 10

# Define objective function
model += x + y

# Define the solver
status = model.solve()

# Print results
x_value = pl.value(x)
y_value = pl.value(y)
print(f'x = {x_value}')
print(f'y = {y_value}')
