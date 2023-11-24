# 我在学习和魔改ZOOpt项目。

原始项目是MIT许可的，https://github.com/polixir/ZOOpt .

ZOOpt这个框架的设计其实本身不复杂，也没有太多精彩之处（甚至有个别不优雅之处）。它主要是实现了一些很好的算法，可以直接调用。

我目前已经在ZOOpt的框架下实现了一个naive的优化算法（见zoopt\algos\opt_algorithms\fyzalgorithm）。调用方式与默认算法类似，只需要在构造parameter的时候设定algorithm="fyz_algorithm" 以及给定一个time_budget，表示算法运行的时间（秒）.注意“budget”参数是默认的racos算法需要的参数，我的naive算法不需要“budget”但是需要“time_budget”.



```python
def ackley(solution):
    x = solution.get_x()
    bias = 0.2
    value = -20 * np.exp(-0.2 * np.sqrt(sum([(i - bias) * (i - bias) for i in x]) / len(x))) - \
            np.exp(sum([np.cos(2.0*np.pi*(i-bias)) for i in x]) / len(x)) + 20.0 + np.e
    return value

dim_size = 50  # dimension size
dim = Dimension(dim_size, [[-5, 5]]*dim_size, [True]*dim_size)
obj = Objective(ackley, dim)

solution = Opt.min(obj, Parameter(time_budget=3, algorithm="fyz_algorithm"))
#solution = Opt.min(obj, Parameter(budget=300))

# print the solution
print(solution.get_x(), solution.get_value())

plt.plot(obj.get_history_bestsofar())
plt.savefig('figure.png')
```





# ZOOpt

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/eyounx/ZOOpt/blob/master/LICENSE.txt) [![Build Status](https://www.travis-ci.org/eyounx/ZOOpt.svg?branch=master)](https://www.travis-ci.org/eyounx/ZOOpt) [![Documentation Status](https://readthedocs.org/projects/zoopt/badge/?version=latest)](https://zoopt.readthedocs.io/en/latest/?badge=latest) [![codecov](https://codecov.io/gh/AlexLiuyuren/ZOOpt/branch/master/graph/badge.svg)](https://codecov.io/gh/AlexLiuyuren/ZOOpt)

ZOOpt is a python package for Zeroth-Order Optimization. 

See https://github.com/polixir/ZOOpt .
