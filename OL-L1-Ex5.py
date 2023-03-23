import gurobipy as gp

m = gp.Model("Lista 1 Ex5")

x11 = m.addVar(vtype=gp.GRB.INTEGER)
x12 = m.addVar(vtype=gp.GRB.INTEGER)
x21 = m.addVar(vtype=gp.GRB.INTEGER)
x22 = m.addVar(vtype=gp.GRB.INTEGER)
x31 = m.addVar(vtype=gp.GRB.INTEGER)
x32 = m.addVar(vtype=gp.GRB.INTEGER)


m.setObjective(50 * x11 + 90 * x21 + 120 * x31 + 65 * x12 + 92 * x22 + 140 * x32, sense=gp.GRB.MINIMIZE)

c1 = m.addConstr(x11 + 2 * x21 + 0.5 * x31 <= 6000)
c2 = m.addConstr(2.5 * x11 + x21 + 4 * x31 <= 10000)

c3 = m.addConstr(x11 + x12 == 3000)
c4 = m.addConstr(x21 + x22 == 2500)
c5 = m.addConstr(x31 + x32 == 500)

m.optimize()

print('X11 =', x11.X)
print('X21 =', x21.X)
print('X31 =', x31.X)
print('X12 =', x12.X)
print('X22 =', x22.X)
print('X32 =', x32.X)
