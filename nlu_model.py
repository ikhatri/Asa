from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
from termcolor import colored
import argparse


def train_nlu(data, configs, model_dir):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'hacknlu')
    
def run_nlu(message):
    interpreter = Interpreter.load('./models/nlu/default/hacknlu')
    print(interpreter.parse(message))

def get_intent(interpreter, message):
    return interpreter.parse(message)["intent"]["name"]

def test_all():
    print(colored("Running unit tests", "yellow"))
    intents_test_list = [ # phrase , expected intent                        Intent Tested
        ("Hello", "greet"),                                                 # greet
        ("Bye!", "goodbye"),                                                # goodbye
        ("What is the wireless password?", "wifi"),                         # wifi
        ("What can you help me with?", "help"),                             # help
        ("Can you tell me a joke?", "joke"),                                # joke
        ("How do I submit my project?", "project_submission"),              # project_submission
        ("How will my project be judged?", "judging_rubric"),               # judging_rubric
        ("What prizes are there?", "prize_list"),                           # prize_list
        ("What time is dinner?", "event_time"),                             # event_time
        ("Where is the verizon workshop?", "event_location"),               # event_location
        ("What's the schedule for the event?", "schedule")                  # schedule
    ]
    intent_model = Interpreter.load('./models/nlu/default/hacknlu')

    tests_failed = False
    for phrase_intent_pair in intents_test_list:
        resulting_intent = get_intent(intent_model, phrase_intent_pair[0])
        if phrase_intent_pair[1] != resulting_intent:
            print(colored("Expected intent: ", "blue") + phrase_intent_pair[1])
            print(colored("Returned Intent: ", "red") + resulting_intent)
            tests_failed = True

    if not tests_failed:
        print(colored("All intent extraction tests passed!", "green"))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', action='store_true', help='Use -t to train the model')
    parser.add_argument('-u', action='store_true', help='Use -u to run the unit tests')
    parser.add_argument('-m', '--message', type=str, help='The message to pass to the NLU model')
    args=parser.parse_args()
    if(args.t):
        train_nlu('./data/data.json', 'config.yml', './models/nlu')
        test_all()
    elif(args.u):
        test_all()
    else:
        message = args.message
        run_nlu(message)
