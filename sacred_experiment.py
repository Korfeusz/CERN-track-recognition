from sacred.observers import MongoObserver
from sacred import Experiment
import genetic_algo as ga
import population
import parameter
ex = Experiment('hello_config')

ex.observers.append(MongoObserver.create())

g_parameter_options = {
'layers' : parameter.IntParameter( (1,5) ),
'neurons': parameter.IntParameter( (1,5) ),
'activation': parameter.SingleChoiceParameter( ['relu'] ),
'loss_metric': parameter.SingleChoiceParameter( ['binary_crossentropy'] ), 
'optimizer': parameter.SingleChoiceParameter( ['adam'] ),
'batch_norm': parameter.SingleChoiceParameter( [True] ),
'dropout': parameter.FloatParameter( (0.0, 0.2) ),
'last_layer_act': parameter.SingleChoiceParameter( ['softmax'] ), 
'kernel_initializer': parameter.SingleChoiceParameter( ['he_normal']),
'feature' : parameter.MultipleChoiceParameter(size=len(learning_data.iloc[:, :-1].columns.values.tolist()),
                                               fixed_size=False,
                                               value=learning_data.iloc[:, :-1].columns.values.tolist())
}

@ex.config
def my_config():
    parameter_options = g_parameter_options
    pop = 20
    iteration = 100


@ex.automain
def my_main(parameter_options, pop, iteration):

    q = population.Population(g_parameter_options, fun_to_maximize, [0.001, 0.1], 0.8, pop)
    for j in range(0, iteration):
        q.generate_generation()
        

    
r = ex.run( config_updates={ 'parameter_options': g_parameter_options } )