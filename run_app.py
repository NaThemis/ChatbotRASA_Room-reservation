from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput
import yaml
from rasa_core.utils import EndpointConfig


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/roomnlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput('xoxp-398888386564-411315767895-415531057043-9dc4137b4fd4011ed779eec996e6ad7c', #app verification token
							'xoxb-398888386564-416999414790-pzZLQrkyNvGuNnaBi6lZqxzu', # bot verification token
							'CBEc0ye0bdvVk7MrGj397SH1', # slack verification token
						    )

agent.handle_channels([input_channel], 5004, serve_forever=True)