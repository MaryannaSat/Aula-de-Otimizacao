import gurobipy as gp

m = gp.Model("Lista 1 Ex8")

x1 = m.addVar()
x2 = m.addVar()


m.setObjective(0.05 * x1 + 0.08 * x2, sense=gp.GRB.MAXIMIZE)


c1 = m.addConstr(x1 + x2 <= 5000)
c2 = m.addConstr(0.25 * (x1 + x2) <= x1)

c3 = m.addConstr(x2 <= 0.5 * (x1 + x2))
c4 = m.addConstr(0.5 * x2 <= x1)


m.optimize()