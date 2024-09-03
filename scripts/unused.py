print('a')
' Implementación utilizando métodos predefinidos de pymoo como parámetros '

# from pymoo.operators.sampling.rnd import IntegerRandomSampling
# from pymoo.operators.crossover.sbx import SBX
# from pymoo.operators.mutation.pm import PM
# from pymoo.operators.repair.rounding import RoundingRepair
#
# algorithm = GA(
#     # pop_size=200,
#     sampling=IntegerRandomSampling(),
#     crossover=SBX(prob=1.0, eta=3.0, vtype=float, repair=RoundingRepair()),
#     mutation=PM(prob=1.0, eta=3.0, vtype=float, repair=RoundingRepair()),
#     eliminate_duplicates=True
# )
#
# res = minimize(model,
#                algorithm,
#                seed=1,
#                verbose=False)
#
# print(f'F: {res.F}, \nX: {res.X}')

' Última implementación de scipy '
# c = tuple(idx for (_, idx) in bounds)
# Aeq = np.ones((1, len(c)))
# beq = 1

# from scipy.optimize import linprog
# from scipy.optimize import differential_evolution

# result = linprog(
#     c,
#     A_ub=Aeq,
#     b_ub=beq,
#     bounds=bounds,
#     method='highs',
#     integrality=1
# )
# print(result)