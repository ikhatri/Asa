from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
import argparse


def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'hacknlu')
    
def run_nlu(message):
    interpreter = Interpreter.load('./models/nlu/default/hacknlu')
    print(interpreter.parse(message))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', action='store_true', help='Use -t to train the model')
    parser.add_argument('-m', '--message', type=str, help='The message to pass to the NLU model')
    args=parser.parse_args()
    if(args.t):
        train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
    else:
        message = args.message
        run_nlu(message)
