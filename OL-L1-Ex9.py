import gurobipy as gp

m = gp.Model("Lista 1 Ex9")

x1 = m.addVar(vtype=gp.GRB.INTEGER)
x2 = m.addVar(vtype=gp.GRB.INTEGER)
x3 = m.addVar(vtype=gp.GRB.INTEGER)


m.setObjective(600 * x1 + 1400 * x2 + 1300 * x3, sense=gp.GRB.MAXIMIZE)


c1 = m.addConstr(0.5 * x1 + 2 * x2 + x3 <= 24)
c2 = m.addConstr(x1 + 2 * x2 + 4 * x3 <= 60)

'''c3 = m.addConstr(2 * x11 + 4 * x12 <= 80)
c4 = m.addConstr(3 * x21 + 3 * x22 <= 60)
'''

m.optimize()

print('X1 =', x1.X)
print('X2 =', x2.X)
print('X3 =', x3.X)
