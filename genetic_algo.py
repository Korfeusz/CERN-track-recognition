import parameter
from population import Population
from keras_model import KerasDNN
import numpy as np
from sklearn.model_selection import train_test_split
import evaluate_to_pandas
from sacred.observers import MongoObserver
from sacred import Experiment
import time

g_info_list = []
g_pop = 20
g_iteration = 200
learning_data = evaluate_to_pandas.read_data()
ex = Experiment('hello_config')
ex.observers.append(MongoObserver.create())


def fun_to_maximize(genotype):
    scores = []
    for i in range(3):
        x_train, x_test, y_train, y_test = train_test_split(learning_data.iloc[:, :-1],
                                                            learning_data['is_downstream_reconstructible'],
                                                            test_size=0.4)
        if genotype['statistical_op'] == 'standardize':
            x_train = evaluate_to_pandas.standardize_data(x_train)
            x_test = evaluate_to_pandas.standardize_data(x_test)
        elif genotype['statistical_op'] == 'normalize':
            x_train = evaluate_to_pandas.normalize_data(x_train)
            x_test = evaluate_to_pandas.normalize_data(x_test)

        input_size = len(genotype["feature"])
        dnn_model = KerasDNN((input_size,), (1,), genotype['layers'], genotype['neurons'],
                             genotype['activation'], genotype['loss_metric'], genotype['optimizer'],
                             genotype['batch_norm'], genotype['dropout'], ['accuracy'],
                             genotype['last_layer_act'], genotype['kernel_initializer'],
                             )

        x = x_train[genotype['feature']]
        y = y_train

        dnn_model(x, y)

        x_score = x_test[genotype['feature']]
        y_score = y_test
        score = dnn_model.eval(x_score, y_score)

        scores.append(score)
    print('scores: {}, mean: {}, parameters: {}'.format(scores, np.mean(scores), genotype))

    info_dict = {'mean': np.mean(scores), 'parameters': genotype}
    g_info_list.append(info_dict)
    return np.mean(scores)


def fun_to_test(genotype):
    x = genotype['x']
    y = genotype['y']
    return -(-20*np.exp(-0.2*np.sqrt(0.5*(x**2 + y**2))) - np.exp(0.5*(np.cos(2*np.pi*x) + np.cos(2*np.pi*y))) + np.e + 20)


g_parameter_options = {
    'x': parameter.FloatParameter((-5.0, 5.0)),
    'y': parameter.FloatParameter((-5.0, 5.0))
}

# g_parameter_options = {
#     'layers': parameter.IntParameter((1, 5)),
#     'neurons': parameter.IntParameter((1, 5)),
#     'activation': parameter.SingleChoiceParameter(['relu']),
#     'loss_metric': parameter.SingleChoiceParameter(['binary_crossentropy']),
#     'optimizer': parameter.SingleChoiceParameter(['adam']),
#     'batch_norm': parameter.SingleChoiceParameter([True]),
#     'dropout': parameter.FloatParameter((0.0, 0.2)),
#     'last_layer_act': parameter.SingleChoiceParameter(['softmax']),
#     'kernel_initializer': parameter.SingleChoiceParameter(['he_normal']),
#     'feature': parameter.MultipleChoiceParameter(size=len(learning_data.iloc[:, :-1].columns.values.tolist()),
#                                                  fixed_size=False,
#                                                  value=learning_data.iloc[:, :-1].columns.values.tolist()),
#     'statistical_op': parameter.SingleChoiceParameter(value=['standardize', 'normalize', 'do_nothing'])
# }


@ex.config
def my_config():
    parameter_options = g_parameter_options
    pop = g_pop
    iteration = g_iteration


@ex.main
def my_main(parameter_options, pop, iteration):
    bst = []
    t0 = time.time()
    for _ in range(20):
        q = Population(parameter_options, fun_to_test, [0.001, 0.1], 0.8, pop)
        print("Population created")
        for j in range(0, iteration):
            # print("Iteration: ", j + 1)
            q.generate_generation()
        bst.append(q.total_best)
    # print('Total best:', q.total_best)
    print('bst: ', np.mean(bst))
    print('time: ', time.time() - t0)
    ex.info['runs_info'] = g_info_list


ex.run(config_updates={'parameter_options': g_parameter_options, 'pop': g_pop, 'iteration': g_iteration})