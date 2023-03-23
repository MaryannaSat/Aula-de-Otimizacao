import gurobipy as gp

m = gp.Model("Lista 1 Ex2")

x1 = m.addVar(vtype=gp.GRB.INTEGER)
x2 = m.addVar(vtype=gp.GRB.INTEGER)


m.setObjective(20 * x1 + 25 * x2, sense=gp.GRB.MAXIMIZE)


c1 = m.addConstr(2 * x1 + 3 * x2 <= 200)
c2 = m.addConstr(4 * x1 + 3 * x2 <= 240)

c3 = m.addConstr(x1 <= 80)
c4 = m.addConstr(x2 <= 60)



m.optimize()
#Imprime o plano de produção
print("Produto 1:", x1.X)
print("Produto 2:", x2.X)
print("Lucro Total:", m.objVal)