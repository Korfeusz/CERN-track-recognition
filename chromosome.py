import random


class Chromosome:
    def __init__(self,  parameter_options,  fun_to_maximize, genotype=None, fitness=-1, recursive_sum=-1):
        self.parameter_options = parameter_options
        if genotype is None:
            genotype = {}
            for key, value in self.parameter_options.items():
                genotype[key] = value.choose_random()
        self.fun_to_maximize = fun_to_maximize
        self.genotype = genotype
        self.fenotype = 0
        self.fitness = fitness
        self.recursive_sum = recursive_sum

    def calc_fenotype(self):
        self.fenotype = self.fun_to_maximize(self.genotype)

    def mutate(self):
        random_gene = random.choice(list(self.genotype.keys()))
        #TODO : musi byc inne
        self.genotype[random_gene] = self.parameter_options[random_gene].choose_random()

    def __str__(self):
        return str(self.genotype)

    __repr__ = __str__