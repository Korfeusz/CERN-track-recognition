import keras
from typing import List, Tuple
from keras.wrappers.scikit_learn import KerasClassifier
import keras
from sklearn.base import BaseEstimator
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
import numpy as np

class KerasDNN(BaseEstimator, KerasClassifier):
    def __init__(
        self,
        input_shape: Tuple[int]=(1,),
        output_shape: Tuple[int]=(1,),
        layers: int=3,
        neurons: int=100,
        activation: str='relu',
        loss_metric: str='binary_crossentropy',
        optimizer: str='adam',
        batch_norm: bool=True,
        dropout: float=0.0,
        metrics: List[str]=['accuracy'],
        last_layer_act: str='softmax',
        kernel_initializer: str='he_normal',
        **kwargs
    ):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.layers = layers
        self.neurons = neurons
        self.activation = activation
        self.loss_metric = loss_metric
        self.optimizer = optimizer
        self.batch_norm = batch_norm
        self.dropout = dropout
        self.kernel_initializer = kernel_initializer
        self.metrics = metrics
        self.last_layer_act = last_layer_act
        self.model = []
        super().__init__(**kwargs)


    def __call__(self, x, y):
        inp = keras.layers.Input(self.input_shape)

        layer = inp
        for i in range(self.layers):
            layer = keras.layers.Dense(self.neurons, activation=self.activation, kernel_initializer=self.kernel_initializer)(layer)
            if self.batch_norm:
                layer = keras.layers.BatchNormalization()(layer)
            if self.dropout > 0:
                layer = keras.layers.core.Dropout(self.dropout)(layer)

        layer = keras.layers.Dense(self.output_shape[-1], activation=self.last_layer_act, kernel_initializer=self.kernel_initializer)(layer)

        model = keras.models.Model(inputs=[inp], outputs=[layer])
        model.compile(
            optimizer=self.optimizer,
            loss=self.loss_metric,
            metrics=self.metrics
        )
        model.fit(x, y, verbose=0, epochs=1)
        self.model = model
        return model

    def predict_proba(self, x, **kwargs):
        return self.model.predict(x)

    def predict(self, x, **kwargs):
        predictions = self.model.predict(x, **kwargs)
        return np.argmax(predictions, axis=1)
    
    def score(self, x, y):
        preds = self.predict_proba(x)
        return roc_auc_score(y, preds)

    def eval(self, x, y):
        scores = self.model.evaluate(x, y)
        print("\n%s: %.2f%%" % (self.model.metrics_names[1], scores[1]*100))
        return scores[1]*100