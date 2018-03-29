from chromosome import Chromosome
import math
import operator
from copy import deepcopy
import random
import numpy as np
from multiprocessing import Pool
import time


class Population:
    def __init__(self, parameter_options, fun_to_maximize, p_mut_range, p_cross, pop, multiprocess=False, processes=4):
        if pop % 2 == 0:
            self.pop = pop
        else:
            self.pop = pop + 1
        self.parameter_options = parameter_options
        self.fun_to_maximize = fun_to_maximize
        self.p_mut_low = p_mut_range[0]
        self.p_mut_high = p_mut_range[1]
        self.p_mut = self.p_mut_low
        self.p_cross = p_cross
        self.agent = [Chromosome(self.parameter_options, self.fun_to_maximize) for _ in range(self.pop)]
        self.best = []
        self.total_best = -1e3
        self.mean = []
        self.stddev = []
        self.multiprocess = multiprocess
        self.processes = processes
        self.calc_fitness()

    def calc_fitness(self):
        if self.multiprocess:
            fenotypes = self._calc_fenotypes_multiprocess()
        else:
            fenotypes = self._calc_fenotypes()
        self._calc_statistics(fenotypes)
        normalized_fenotypes = self._normalize_fenotypes(fenotypes=fenotypes)
        for i, ch in enumerate(self.agent):
            ch.fitness = normalized_fenotypes[i]
        self._sort_agents(fitness=normalized_fenotypes)

    def _calc_fenotypes(self):
        for i in range(self.pop):
            self.agent[i].calc_fenotype()
        return [x.fenotype for x in self.agent]

    def _calc_fenotypes_multiprocess(self):
        with Pool(self.processes) as p:
            fenotypes = p.map(func=self._calc_fenotype_of_agent, iterable=self.agent)
        for i, c in enumerate(self.agent):
            c.fenotype = fenotypes[i]
        return [x.fenotype for x in self.agent]

    @staticmethod
    def _calc_fenotype_of_agent(agent: Chromosome):
        agent.calc_fenotype()
        return agent.fenotype

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
        if total_area == 0:
            return [1/len(fitness) for _ in range(len(fitness))]
        return [x / total_area for x in fitness]

    def generate_generation(self):
        selected = self.selection()
        selected = self.cross(selected)
        selected = self.mutate(selected)
        self.agent = selected
        self.calc_fitness()
        self.dynamic_p_mutate()
        self.total_best = max(self.best)

    def selection(self):
        fitness = [x.fitness for x in self.agent]
        choices = list(np.random.choice(a=len(self.agent), size=self.pop, p=fitness, replace=True))
        return [deepcopy(self.agent[choice]) for choice in choices]

    def cross(self, selected):
        new_generation = []
        number_to_cross = int(math.ceil(self.pop * self.p_cross / 2))
        for _ in range(number_to_cross):
            sample = random.sample(selected, 2)
            selected.remove(sample[0])
            selected.remove(sample[1])
            new_generation.extend((self.cross_single(sample)))
        new_generation.extend(selected)
        return new_generation

    def cross_single(self, sample):
        chro_1 = sample[0]
        chro_2 = sample[1]
        random_key_number = random.randint(1, len(self.parameter_options))
        random_keys = random.sample(self.parameter_options.keys(), random_key_number)
        for key in random_keys:
            chro_1.genotype[key], chro_2.genotype[key] = chro_2.genotype[key], chro_1.genotype[key]
        return [chro_1, chro_2]

    def mutate(self, selected):
        number_to_mutate = int(math.ceil(self.pop * len(self.parameter_options) * self.p_mut))
        for _ in range(number_to_mutate):
            ra_index = random.randint(0, self.pop - 1)
            selected[ra_index].mutate()
        return selected

    def dynamic_p_mutate(self):
        if self.stddev[-1] < 0.2:
            self.p_mut = self.p_mut_high
        else:
            self.p_mut = self.p_mut_low
