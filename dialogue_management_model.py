from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import rasa_core

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application



logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'room_domain.yml',
					model_path = './models/current/dialogue',
					training_data_file = './data/stories.md'):
					
	agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy()])
	data = agent.load_data(training_data_file)
	agent.train(
				data,
				epochs = 300,
				#batch_size = 50,
				validation_split = 0.2)
				
	agent.persist(model_path)
	return agent
	
def run_room_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/current/nlu')
    print("after interpreter")
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    print("after action_endpoint")
    agent = Agent.load('./models/current/dialogue', interpreter = interpreter, action_endpoint=action_endpoint)
    print("after agent")
    agent = Agent.load('./models/current/dialogue', interpreter = interpreter)
    print("after agent 2")
    rasa_core.run.serve_application(agent ,channel='cmdline')
    return agent
	
if __name__ == '__main__':
    train_dialogue()
    run_room_bot()
