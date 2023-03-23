import gurobipy as gp

m = gp.Model("Lista 1 Ex1")

x11 = m.addVar()
x12 = m.addVar()
x21 = m.addVar()
x22 = m.addVar()

m.setObjective(0.15 * 24 * x11 + 0.15 * 20.5 * x12 + 0.15 * 17.2 * x21 + 0.15 * 18 * x22, sense=gp.GRB.MINIMIZE)


c1 = m.addConstr(x11 + x21 <= 200)
c2 = m.addConstr(x12 + x22 <= 200)

c3 = m.addConstr(x11 + x12 <= 240)
c4 = m.addConstr(x21 + x22 <= 300)

c5 = m.addConstr(300 <= x11 + x12 + x21 + x22)

m.optimize()

'''
print('X1 =', x1.X)
print('X2 =', x2.X)'''