from zoopt.dimension import Dimension
from zoopt.parameter import Parameter
from zoopt.objective import Objective
from zoopt.solution import Solution
import random
import time
from zoopt.utils.tool_function import ToolFunction


class Naive:

    def __init__(self):
        self._parameter = None
        self._objective = None
        self._best_solution = None

    def clear(self):
        self._parameter = None
        self._objective = None
        self._best_solution = None

    def opt(self, objective, parameter):
        self.clear()
        self.set_objective(objective)
        self.set_parameters(parameter)
        time_log1 = time.time()
        dim: Dimension = self._objective.get_dim()
        self._best_solution = self._objective.construct_solution(dim.rand_sample())
        delta = 1
        previous_value = self._objective.eval(self._best_solution)
        count = 0
        while True:
            count += 1
            if self._parameter.get_time_budget() is not None:
                if (time.time() - time_log1) >= self._parameter.get_time_budget():
                    ToolFunction.log('naive-algorithm runs out of time_budget')
                    return self._best_solution
            x_t: Solution = self._objective.construct_solution(self.generate_vector(delta))
            new_value = self._objective.eval(x_t)
            if new_value < previous_value:
                delta *= 1.2
                self._best_solution = x_t
            else:
                delta *= 0.8

    def generate_vector(self, times=1):
        dim: Dimension = self._objective.get_dim()
        dimsize = dim.get_size()
        region = dim.get_regions()
        random.seed()
        v = [random.random() for _ in range(dimsize)]
        for i in range(dimsize):
            v[i] *= (region[i][1] - region[i][0])*0.01*times
            v[i] += self._best_solution.get_x()[i]
        return v

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
