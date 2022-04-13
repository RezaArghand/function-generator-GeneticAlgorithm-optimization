import random

import numpy as np

import functions as func

# parameters of PSO optimization algorithm
population_size: 200
# number_randomize_particles_fullArea = int(np.floor(0.25 * number_of_particles))
# number_randomize_particles_firstBitOfBest = int(np.floor(0.25 * number_of_particles))

funcNum = 5
varNum = funcNum * 2 + 1  # number of parameters in each particle
damping_rate_W = 0.9  # inertia damper
bound_of_realNumber = 1000
satisfaction_fittness_number = 0.5  # satisfaction point
max_num_iteration = 80000
# end parameters of PSO optimization

# function library
# funcLib = ['(', 'np.sin(', 'np.exp(', 'np.sqrt(', 'np.floor(', 'np.floor(x0', 'np.sqrt(x0', 'x0', 'np.cos(x0',
#            'np.tan(', 'np.sqrt(x0', '(x**2)', 'np.exp(', 'np.exp(x0',
#            '1/x0', 'np.sign(', 'np.sign(x0',
#            '(x0 ** 3)', '']
# operators = ['*', '/', '+', '-', '**', ')', '(']

funcLib = ['np.tanh(', 'x0']
operators = ['*', '+', '-', ')', '(', '']

# maxVariable, finalLib = func.normalizeLength(funcLib, operators)
finalLib = 3 * funcLib + operators
max_of_variable = len(finalLib) - 1  # max domain
min_of_variable = -len(finalLib) + 1  # min domain

print(finalLib)

# defining combination tuples:

combinationList = func.combinationGenerator(varNum + 1)
combinationListLength = len(combinationList)
