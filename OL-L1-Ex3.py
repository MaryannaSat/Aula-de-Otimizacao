import gurobipy as gp

m = gp.Model("Lista 1 Ex3")

x11 = m.addVar()
x12 = m.addVar()
'''x21 = m.addVar()
x22 = m.addVar()'''

m.setObjective( 5 * x11  + 4 * x12 , sense=gp.GRB.MAXIMIZE)


c1 = m.addConstr(x12 <= x11 + 1)
c2 = m.addConstr(x12 <= 2)

c3 = m.addConstr(6 * x11 + 4 * x12 <= 24)
c4 = m.addConstr(x11 + 2 * x12 <= 6)

c5 = m.addConstr( 0 <= x12)
c6 = m.addConstr( 0 <= x11)

m.optimize()