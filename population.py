from chromosome import Chromosome
import math
import operator
from copy import deepcopy
import random
import numpy as np

class Population:
    def __init__(self, parameter_options, fun_to_maximize, p_mut_range, p_cross, pop):
        self.pop = pop
        self.parameter_options = parameter_options
        self.fun_to_maximize = fun_to_maximize
        self.p_mut_low = p_mut_range[0]
        self.p_mut_high = p_mut_range[1]
        self.p_mut = self.p_mut_low
        self.p_cross = p_cross
        self.agent = [Chromosome(self.parameter_options, self.fun_to_maximize) for _ in range(pop)]
        self.best = []
        self.total_best = -1e3
        self.mean = []
        self.stddev = []
        self.calc_fitness()

    def calc_fitness(self):
        fenotypes = self._calc_fenotypes()
        self._calc_statistics(fenotypes)
        normalized_fenotypes = self._normalize_fenotypes(fenotypes=fenotypes)
        for i, ch in enumerate(self.agent):
            ch.fitness = normalized_fenotypes[i]
        self._sort_agents(fitness=normalized_fenotypes)

    def _calc_fenotypes(self):
        # Map reduce should happen here
        for i in range(self.pop):
            self.agent[i].calc_fenotype()
        return [x.fenotype for x in self.agent]

    def _calc_statistics(self, fenotypes):
        self.best.append(max(fenotypes))
        self.mean.append(sum(fenotypes) / self.pop)
        self.stddev.append(np.std(fenotypes))

    def _sort_agents(self, fitness):
        self.agent.sort(key=operator.attrgetter('fitness'))
        cumsum = np.cumsum(np.sort(fitness))
        for idx, element in enumerate(self.agent):
            element.recursive_sum = cumsum[idx]

    @staticmethod
    def _normalize_fenotypes(fenotypes):
        if min(fenotypes) < 0:
            offset = abs(min(fenotypes))
            fitness = [x + offset for x in fenotypes]
        else:
            fitness = fenotypes
        total_area = sum(fitness)
        return [x / total_area for x in fitness]

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
