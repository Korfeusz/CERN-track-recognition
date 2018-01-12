import numpy as np
import math
import operator
from copy import deepcopy
import matplotlib.pyplot as plt
import random

pop = 20
elements = 22
iteration = 100
x_range = [-1, 2]


def fun_to_maximize(fu_number):
    return fu_number * math.sin(10 * math.pi * fu_number) + 1


class Chromosome:
    def __init__(self, genotype2=None, fitness=-1, recursive_sum=-1):
        if genotype2 is None:
            self.genotype2 = []
            for _ in range(0, elements):
                self.genotype2.append(random.randint(0, 1))
        else:
            self.genotype2 = genotype2
        self.genotype10 = 0
        self.fenotype = 0
        self.calc_fenotype()
        self.fitness = fitness
        self.recursive_sum = recursive_sum

    def bin2num(self):
        self.genotype10 = int("".join(map(str, self.genotype2)), base=2)

    def calc_fenotype(self):
        self.bin2num()
        _genotype10_ranged = \
            float(self.genotype10 * (x_range[1] - x_range[0]))\
            / (2 ** elements - 1) + x_range[0]
        self.fenotype = fun_to_maximize(_genotype10_ranged)

    def mutate(self):
        _ra_ind = random.randint(0, elements-1)
        self.genotype2[_ra_ind] = int(not(self.genotype2[_ra_ind]))

    def __str__(self):
        self.bin2num()
        return str(self.genotype10)

    __repr__ = __str__


class Populus:
    def __init__(self, p_mut_range, p_cross):
        self.p_mut_low = p_mut_range[0]
        self.p_mut_high = p_mut_range[1]
        self.p_mut = self.p_mut_low
        self.p_cross = p_cross
        self.agent = []
        for _ in range(0, pop):
            self.agent.append(Chromosome())
        self.best = []
        self.total_best = -1e3
        self.mean = []
        self.stddev = []
        self.calc_fitness()

    def calc_fitness(self):
        _fenotypes = []
        for _i in range(0, pop):
            self.agent[_i].calc_fenotype()
            _fenotypes.append(self.agent[_i].fenotype)
        _offset = 0
        if min(_fenotypes) < 0:
            _offset = abs(min(_fenotypes))
        _fitness = [x + _offset for x in _fenotypes]
        total_area = sum(_fitness)
        _fitness = [x / total_area for x in _fitness]
        for _i in range(0, pop):
            self.agent[_i].fitness = _fitness[_i]
        # Finding current and total best
        self.best.append(max(_fenotypes))
        _mean = sum(_fenotypes)/pop
        self.mean.append(_mean)
        _subsum = [(x - _mean) ** 2 for x in _fenotypes]
        self.stddev.append(math.sqrt(sum(_subsum) / pop))
        self.agent.sort(key=operator.attrgetter('fitness'))
        _recursive_sum = 0
        _agent = deepcopy(self.agent)
        del self.agent
        self.agent = []
        for _i in range(0, pop):
            _recursive_sum = _agent[_i].fitness + _recursive_sum
            self.agent.append(Chromosome(_agent[_i].genotype2,
                                         _agent[_i].fitness,
                                         _recursive_sum))

    def generate_generation(self):
        _selected = self.selection()
        _selected = self.cross(_selected)
        _selected = self.mutate(_selected)
        self.agent = _selected
        self.calc_fitness()
        self.dynamic_p_mutate()
        self.total_best = max(self.best)

    def selection(self):
        _selected = []
        for _ in range(0, pop):
            _shot = random.random()
            for _j in range(0, pop):
                if _j == 0:
                    _bottom = 0
                else:
                    _bottom = self.agent[_j-1].recursive_sum
                if _bottom < _shot <= self.agent[_j].recursive_sum:
                    x = deepcopy(self.agent[_j])
                    _selected.append(x)
        return _selected

    def cross(self, _selected):
        _new_generation = []
        for _ in range(0, int(math.ceil(pop * self.p_cross / 2))):
            _sample = random.sample(_selected, 2)
            _selected.remove(_sample[0])
            _selected.remove(_sample[1])
            _new_generation.extend((self.cross_single(_sample)))
        _new_generation.extend(_selected)
        return _new_generation

    @staticmethod
    def cross_single(_sample):
        _chro_1 = _sample[0]
        _chro_2 = _sample[1]
        _ra_index = random.randint(0, elements - 1)
        _temp = _chro_1.genotype2[_ra_index:]
        _chro_1.genotype2[_ra_index:] = _chro_2.genotype2[_ra_index:]
        _chro_2.genotype2[_ra_index:] = _temp
        return [_chro_1, _chro_2]

    def mutate(self, _selected):
        for _ in range(0, int(math.ceil(pop * elements * self.p_mut))):
            _ra_index = random.randint(0, pop - 1)
            _selected[_ra_index].mutate()
        return _selected

    def dynamic_p_mutate(self):
        if self.stddev[-1] < 0.2:
            self.p_mut = self.p_mut_high
        else:
            self.p_mut = self.p_mut_low


# Zmienne p_mut
q = []
table_q = []
for i in range(0, 10):
    q.append(Populus([0.001, 0.1], 0.8))
    for j in range(0, iteration):
        q[i].generate_generation()
    table_q.append(q[i].total_best)


#TODO Move plotting to another file and make it plot data from mongoDB
def plot_demo(_p, name):
    for i in range(0, 4):
        plt.plot(_p[i].best, label="Best")
        plt.plot(_p[i].mean, label="Mean")
        plt.yticks(np.linspace(min(min(_p[i].best), min(_p[i].mean)),
                               max(max(_p[i].best), max(_p[i].mean)), num=10))
        plt.legend(loc='lower right')
        plt.savefig("".join([name, "rys", str(i), ".pdf"]), dpi=72)
        plt.clf()

plot_demo(q, "q")