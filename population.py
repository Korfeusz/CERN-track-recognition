from chromosome import Chromosome
import math
import operator
from copy import deepcopy
import random


class Population:
    def __init__(self, parameter_options, fun_to_maximize, p_mut_range, p_cross, pop):
        self.pop = pop #wielkosc populacji
        self.parameter_options = parameter_options
        self.fun_to_maximize = fun_to_maximize
        self.p_mut_low = p_mut_range[0]
        self.p_mut_high = p_mut_range[1]
        self.p_mut = self.p_mut_low
        self.p_cross = p_cross
        self.agent = []
        for _ in range(0, pop):
            self.agent.append(Chromosome(self.parameter_options, self.fun_to_maximize))
        self.best = []
        self.total_best = -1e3
        self.mean = []
        self.stddev = []
        self.calc_fitness()

    def calc_fitness(self):
        _fenotypes = []
        for _i in range(0, self.pop):
            self.agent[_i].calc_fenotype()
            _fenotypes.append(self.agent[_i].fenotype)
        _offset = 0
        if min(_fenotypes) < 0:
            _offset = abs(min(_fenotypes))
        _fitness = [x + _offset for x in _fenotypes]
        total_area = sum(_fitness)
        _fitness = [x / total_area for x in _fitness]
        for _i in range(0, self.pop):
            self.agent[_i].fitness = _fitness[_i]
        # Finding current and total best
        self.best.append(max(_fenotypes))
        _mean = sum(_fenotypes) / self.pop
        self.mean.append(_mean)
        _subsum = [(x - _mean) ** 2 for x in _fenotypes]
        self.stddev.append(math.sqrt(sum(_subsum) / self.pop))
        self.agent.sort(key=operator.attrgetter('fitness'))
        _recursive_sum = 0
        _agent = deepcopy(self.agent)
        del self.agent
        self.agent = []
        for _i in range(0, self.pop):
            _recursive_sum = _agent[_i].fitness + _recursive_sum
            self.agent.append(Chromosome(self.parameter_options,
                                         self.fun_to_maximize,
                                         _agent[_i].genotype,
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
        for _ in range(0, self.pop):
            _shot = random.random()
            for _j in range(0, self.pop):
                if _j == 0:
                    _bottom = 0
                else:
                    _bottom = self.agent[_j - 1].recursive_sum
                if _bottom < _shot <= self.agent[_j].recursive_sum:
                    x = deepcopy(self.agent[_j])
                    _selected.append(x)
        print("len: ", len(_selected))

        return _selected

    def cross(self, _selected):
        _new_generation = []
        for _ in range(0, int(math.ceil(self.pop * self.p_cross / 2))):
            _sample = random.sample(_selected, 2)
            _selected.remove(_sample[0])
            _selected.remove(_sample[1])
            _new_generation.extend((self.cross_single(_sample)))
        _new_generation.extend(_selected)
        return _new_generation

    def cross_single(self, _sample):
        _chro_1 = _sample[0]
        _chro_2 = _sample[1]
        random_key_number = random.randint(1, len(self.parameter_options))
        random_keys = random.sample(self.parameter_options.keys(), random_key_number)
        for key in random_keys:
            _chro_1.genotype[key], _chro_2.genotype[key] = _chro_2.genotype[key], _chro_1.genotype[key]
        return [_chro_1, _chro_2]

    def mutate(self, _selected):
        for _ in range(0, int(math.ceil(self.pop * len(self.parameter_options) * self.p_mut))):
            _ra_index = random.randint(0, self.pop - 1)
            _selected[_ra_index].mutate()
        return _selected

    def dynamic_p_mutate(self):
        if self.stddev[-1] < 0.2:
            self.p_mut = self.p_mut_high
        else:
            self.p_mut = self.p_mut_low
