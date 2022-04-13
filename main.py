from geneticalgorithm import geneticalgorithm as ga
import numpy as np
import fitnessFunction as fitFunc
import parameters as par


def f(X):
    # inputPos = []
    # for i in X:
    #     inputPos.append(int(i))
    # result = fitFunc.fitnessNumber(inputPos)
    result = fitFunc.fitnessNumber(X)
    return result


chromosomNum = par.varNum
upperBound = par.max_of_variable
lowerBound = par.min_of_variable
varbound = np.array([[lowerBound, upperBound]] * chromosomNum)
# model=ga(function=f,dimension=3,variable_type='real',variable_boundaries=varbound)

model = ga(function=f, dimension=chromosomNum, variable_type='real', variable_boundaries=varbound)

model.run()
