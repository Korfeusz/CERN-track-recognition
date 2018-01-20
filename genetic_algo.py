import parameter
from population import Population
from genetic_visualisation import plot_demo


def fun_to_maximize(parameters):
    # TODO Here will the optimized algorithm be evaluated against our parameters
    # This is just an example
    if parameters['param1'] == 'option1':
        return 1
    elif parameters['param1'] == 'option2':
        return 0.5
    elif parameters['param1'] == 'option3':
        return 0.1


g_parameter_options = {
    'param1': parameter.SingleChoiceParameter(['option1', 'option2', 'option3']),
    'param2': parameter.FloatParameter((0, 100))
}

pop = 20
iteration = 100
q = Population(g_parameter_options, fun_to_maximize, [0.001, 0.1], 0.8, pop) 

for j in range(0, iteration):
        q.generate_generation()

plot_demo(q)
