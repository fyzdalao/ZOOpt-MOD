from zoopt.dimension import Dimension
from zoopt.parameter import Parameter
from zoopt.objective import Objective
from zoopt.solution import Solution
import random
import time
from copy import deepcopy
from zoopt.utils.tool_function import ToolFunction


class Naive:

    def __init__(self):
        self._parameter = None
        self._objective = None
        self._best_solution: Solution = None

    def clear(self):
        self._parameter = None
        self._objective = None
        self._best_solution = None

    '''
    This algorithm is a naive "Directional direct-search methods" in 
    Chapter 7, book Introduction to Derivative-Free Optimization by Philippe Toint
    '''
    def opt(self, objective, parameter):
        self.clear()
        self.set_parameters(parameter)
        self.set_objective(objective)
        time_log1 = time.time()
        random.seed(time.time())

        dim: Dimension = self._objective.get_dim()
        dim_size = dim.get_size()
        regions = dim.get_regions()
        dom = []
        for i in range(dim_size):
            dom.append(regions[i][1]-regions[i][0])

        self._best_solution = self._objective.construct_solution(dim.rand_sample())
        history = []
        best_value = self._objective.eval(self._best_solution)
        history.append(best_value)
        delta = 1
        while True:
            if self._parameter.get_time_budget() is not None:
                if (time.time() - time_log1) >= self._parameter.get_time_budget():
                    ToolFunction.log('naive-algorithm runs out of time_budget')
                    objective.set_history(history)
                    return self._best_solution
            else:
                ToolFunction.log('please give naive-algorithm a time_budget parameter')
                objective.set_history(history)
                return self._best_solution

            flag = 0
            best_x = self._best_solution.get_x()
            for i in range(dim_size):
                new_x = deepcopy(best_x)
                new_x[i] += delta*dom[i]*0.1
                new_solution = objective.construct_solution(new_x)
                if objective.eval(new_solution) < best_value:
                    flag = 1
                    self._best_solution = new_solution
                    break
            for i in range(dim_size):
                if flag == 1:
                    break
                new_x = deepcopy(best_x)
                new_x[i] -= delta*dom[i]*0.1
                new_solution = objective.construct_solution(new_x)
                if objective.eval(new_solution) < best_value:
                    flag = 1
                    self._best_solution = new_solution
                    break
            if flag == 1:
                delta *= 1.05
            else:
                delta *= 0.5
            best_value = self._objective.eval(self._best_solution)
            history.append(best_value)

    def set_parameters(self, parameter):
        self._parameter = parameter
        return

    def get_parameters(self):
        return self._parameter

    def set_objective(self, objective):
        self._objective = objective
        return

    def get_objective(self):
        return self._objective
