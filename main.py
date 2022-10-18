# using https://brilliant.org/wiki/lagrange-interpolation/ 
# https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html
from typing import Any, List
from sympy import *


def generate(X: List[float], Y: List[float]) -> (Any | Add | Order | Mul | Expr):
    # create x symbol for symbolic manipulation 
    x = symbols("x")

    # string manipulation to create the equation
    elems = []
    for id_elem in range(len(X)):
        temp = "("
        for id_elem2 in range(len(X)):
            if id_elem != id_elem2:
                temp += "(x-" + str(X[id_elem2]) + ")"
                if id_elem2 != len(X) - 1:
                    temp += "*"
        if temp[-1] == "*":
            temp = temp[:-1]
        temp += ") / ("
        for id_elem2 in range(len(X)):
            if id_elem != id_elem2:
                temp += "({}-{})*".format(X[id_elem], X[id_elem2])
        if temp[-1] == "*":
            temp = temp[:-1]
        temp += ")*{}".format(Y[id_elem])
        elems.append(temp)
        if id_elem != len(X) - 1:
            elems.append("+")

    # eval the string to obtain the sympy function then factorize to simplify
    func = eval("".join(elems))
    return factor(func)


if __name__ == "__main__":
    from matplotlib import pyplot as plt
    import numpy as np 

    X  = [-4, -1, 7, 3, 9]
    Y  = [5, 2, -2, 9, 4]
    
    func = generate(X, Y)

    # plot target points
    plt.scatter(X, Y)

    # plot function
    plot_xs = np.arange(-5, 10.0, 0.1)
    plot_ys = [func.subs(symbols("x"), val) for val in plot_xs]
    plt.plot(plot_xs, plot_ys)
    plt.savefig("media/interpolated.png")
    plt.show()
    print("Equation: {}".format(func))
