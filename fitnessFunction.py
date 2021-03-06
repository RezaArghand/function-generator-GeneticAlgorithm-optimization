import math
import random

import numpy as np

import parameters as par
import sympy as sp
import functions as func
from scipy.stats import logistic

mainList = par.finalLib
x0 = sp.symbols("x0")


def mainFitness(position):
    combinations = par.combinationList
    combinationsLength = len(combinations)
    mainLib = par.finalLib
    inputt = []
    theString = []
    inputt.append('')
    l_num_func = int(len(position) - 1)
    l_func = int(l_num_func / 2)
    combinationNumber = int(
        np.floor(func.map_value(1000000 * position[-1], 1000000 * par.min_of_variable, 1000000 * par.max_of_variable, 0,
                                combinationsLength - 1)))
    combinationList = combinations[combinationNumber]
    for i in range(l_func):
        j = int(np.floor(position[i]))
        inputt.append(mainLib[j])
    for i in range(l_func, l_num_func):
        value = func.map_value(position[i], par.min_of_variable, par.max_of_variable, -par.bound_of_realNumber,
                               par.bound_of_realNumber)
        stringValue = '+ ' + str(round(value, 2))
        inputt.append(stringValue)
    inputt.append('')
    for i in combinationList:
        theString.append(inputt[i])
    # print(position)
    # print(inputt)
    # print(combinationList)
    # print(theString)
    # a = input("go?")
    # finalString = "".join(func.makeBalanced(theString))
    primaryString = "".join(theString)
    finalString = func.makeBalanced(primaryString)

    if 'x0' in finalString:
        try:
            # if 'x0' in theString:
            #     theString += ''
            # else:
            #     theString += '-x0*5000'

            mainFunc = finalString  # eval(finalString)
            t = np.linspace(-100, 100, 5000)
            mengaX = []
            resultX = []
            # mengaString = 'np.tanh(np.tanh(np.tanh(np.tanh(x0)*81.6497)*8)*abs(np.sqrt(np.pi)* np.log(6)))*np.pi*81.6497'
            mengaString = '25*x0+12.6'
            # mengaString='3.4 * x0'
            for i in t:
                menga = func.evalFunction(i, mengaString)
                funResult = func.evalFunction(i, finalString)
                mengaX.append(menga)
                resultX.append(funResult)
            finalArray = []
            for i in range(len(t)):
                finalArray.append(abs(mengaX[i] - resultX[i]))
            result = 0
            for i in finalArray:
                result = result + i / len(finalArray)

        except:
            result = 10000
            mainFunc = "error(1) : " + finalString
    else:
        result = 15000
        mainFunc = "error(2) : " + finalString

    return result, mainFunc


def fitnessNumber(positon):
    final, funn = mainFitness(positon)
    return final


def bestFunc(position):
    final, funn = mainFitness(position)
    try:
        result1 = sp.simplify(eval(funn))
    except:
        result1 = str(funn)
    result = str(result1)
    return result

# pp = [1, 19, 11, 9, 24]
#
# print(str(bestFunc(pp)))

# x = sp.symbols("x")
# h = eval('sp.sin(x)')
#
# print(sp.N(h.subs(x, 30)))
# print(func.sigmoid(5.6))
