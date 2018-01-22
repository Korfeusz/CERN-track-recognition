import parameter
from population import Population
from genetic_visualisation import plot_demo
from keras_model import KerasDNN
from typing import Tuple
import numpy as np
from sklearn.model_selection import train_test_split
import evaluate_to_pandas

learning_data = evaluate_to_pandas.read_data()


def fun_to_maximize(genotype):
    x_train, x_test, y_train, y_test = train_test_split(learning_data.iloc[:, :-1],
                                                        learning_data['is_downstream_reconstructible'], test_size=0.4)
    #here we create a model and calc its score
    dnn_model = KerasDNN( (1,), (1,), genotype['layers'], genotype['neurons'],
             genotype['activation'], genotype['loss_metric'], genotype['optimizer'],
             genotype['batch_norm'], genotype['dropout'], ['accuracy'],
             genotype['last_layer_act'], genotype['kernel_initializer'],
            )
    
    print("I am working!")
    
    print("Parameters: {}".format(genotype))
    
    x = x_train[[genotype['feature']]]
    y = y_train
    
    #dnn_model = KerasDNN()
    dnn_model(x, y)
    #dnn_model.fit(x, y )#here we need to put training data

    x_score = x_test[[genotype['feature']]]
    y_score = y_test
    score = dnn_model.eval(x_score, y_score)
    print ("Score: ", score)
    
    return score ##and here- testing data


g_parameter_options = {
    #'input_shape': parameter.IntParameter( (0,10) ), Does not work for now but I don't know if it will be necessery
    #'output_shape': Tuple[ parameter.IntParameter( (0,10) )], Does not work for now but I don't know if it will be necessery
    'layers' : parameter.IntParameter( (1,20) ),
    'neurons': parameter.IntParameter( (1,20) ),
    'activation': parameter.SingleChoiceParameter( ['relu', 'tanh', 'softmax'] ),
    'loss_metric': parameter.SingleChoiceParameter( ['binary_crossentropy'] ), 
    'optimizer': parameter.SingleChoiceParameter( ['adam',  'adamax'] ),
    'batch_norm': parameter.SingleChoiceParameter( [True, False] ), #I wonder if it's better to use IntParameter with (0,1) range repr. boolean?
    'dropout': parameter.FloatParameter( (0.0, 1.0) ),
    #'metrics': parameter.SingleChoiceParameter( ['accuracy'] ), I couldn't make a List of class instances, so for now screw that option
    'last_layer_act': parameter.SingleChoiceParameter( ['softmax'] ), 
    'kernel_initializer': parameter.SingleChoiceParameter( ['he_normal', 'he_uniform'] ),
    'feature': parameter.SingleChoiceParameter(learning_data.iloc[:, :-1].columns.values.tolist())
}
    
pop = 20
iteration = 100
q = Population(g_parameter_options, fun_to_maximize, [0.001, 0.1], 0.8, pop) 

for j in range(0, iteration):
    q.generate_generation()

plot_demo(q)