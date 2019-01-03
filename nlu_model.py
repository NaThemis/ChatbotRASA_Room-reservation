from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

#import rasa_nlu
#print(rasa_nlu.__version__)

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir, fixed_model_name = 'roomnlu')
	
def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/roomnlu')
	print(interpreter.parse("I want the blue room for the 1 november starting at 16h and during 1 hour !"))


if __name__ == '__main__':
   #commment out the following line to train the model
	train_nlu('./data/data.json', 'config_spacy.json', './models/nlu')
	run_nlu()