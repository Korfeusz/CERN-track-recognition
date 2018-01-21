from sacred.observers import MongoObserver
from sacred import Experiment

ex = Experiment('hello_config')

ex.observers.append(MongoObserver.create())

@ex.config
def my_config():
    recipient = "world"
    message = "Hello %s!" % recipient
        
@ex.automain
def my_main(message):
    print(message)