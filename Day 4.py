# Today I started with scipy library
# i justt learnt optimization part of it only so,
# i started with one of the easiest topic of class 12 maths, .....

# Objective:
# Minimize the function f(x, y) = (x - 1)^2 + (y - 2.5)^2
# With the following constraints:
# x - 2y + 2 ≥ 0
# -x - 2y + 6 ≥ 0
# -x + 2y + 2 ≥ 0
# x ≥ 0
# y ≥ 0

import scipy.optimize as opt

f = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2

cons = ({'type': 'ineq','fun': lambda x: x[0] - 2 * x[1] + 2},
        {'type': 'ineq','fun': lambda x: -x[0] - 2 * x[1] + 6},
        {'type': 'ineq','fun': lambda x: -x[0] + 2 * x[1] + 2})

bnds = ((0, None), (0, None))

res = opt.minimize(f, (2, 0), method='SLSQP', bounds=bnds, constraints=cons)
print(res)