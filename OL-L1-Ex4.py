import gurobipy as gp

m = gp.Model("Lista 1 Ex4")

x11 = m.addVar()
x21 = m.addVar()
x22 = m.addVar()
x31 = m.addVar()
x32 = m.addVar()
x41 = m.addVar()
x42 = m.addVar()


m.setObjective(27 * x11 + 27 * x12 + 35 * x21 + 35 * x22 + 51 * x31 + 51 * x32 + 41 * x41 + 41 * x42, sense=gp.GRB.MINIMIZE)

c1 = m.addConstr(0.2 * x11 + 0.4 * x21 + 0.5 * x31 + 0.8 * x41 <= 9.5)
c2 = m.addConstr(7.6 <= 0.2 * x11 + 0.4 * x21 + 0.5 * x31 + 0.8 * x41)
c3 = m.addConstr(0.6 * x11 + 0.4 * x21 + 0.4 * x31 + 0.1 * x41 <= 11.4)
c4 = m.addConstr(5.7 <= 0.6 * x11 + 0.4 * x21 + 0.4 * x31 + 0.1 * x41)

c5 = m.addConstr(0.2 * x11 + 0.4 * x21 + 0.5 * x31 + 0.8 * x41 <= 6)
c6 = m.addConstr(3.6 <= 0.2 * x11 + 0.4 * x21 + 0.5 * x31 + 0.8 * x41)
c7 = m.addConstr(0.6 * x11 + 0.4 * x21 + 0.4 * x31 + 0.1 * x41 <= 9.6)
c8 = m.addConstr(6 <= 0.6 * x11 + 0.4 * x21 + 0.4 * x31 + 0.1 * x41)


c9 = m.addConstr(x11 + x12 <= 10)
c11 = m.addConstr(x21 + x22 <= 10)
c13 = m.addConstr(x31 + x32 <= 14)
c15 = m.addConstr(x41 + x42 <= 12)

c17 = m.addConstr(x11 + x21 + x31 + x41 == 19)
c18 = m.addConstr(x11 + x21 + x31 + x41 == 12)





m.optimize()