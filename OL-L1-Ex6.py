import gurobipy as gp

m = gp.Model("Lista 1 Ex5")

x11 = m.addVar(vtype=gp.GRB.INTEGER)
x12 = m.addVar(vtype=gp.GRB.INTEGER)
x21 = m.addVar(vtype=gp.GRB.INTEGER)
x22 = m.addVar(vtype=gp.GRB.INTEGER)



m.setObjective(50 * (30 * x11 + 36 * x21) + 120 * (30 * x12 + 36 * x22), sense=gp.GRB.MAXIMIZE)

c1 = m.addConstr(0.6 * x11 + 0.8 * x21 <= 20000)
c2 = m.addConstr(0.4 * x12 + 0.2 * x22 <= 10000)

c3 = m.addConstr(x11 + x12 <= 23000)
c4 = m.addConstr(x21 + x22 <= 30000)

c5 = m.addConstr(0 <= x11 + x12)
c6 = m.addConstr(0 <= x21 + x22)





m.optimize()