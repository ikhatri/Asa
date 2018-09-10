from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RegexInterpreter
import json

# load your trained agent
agent = Agent.load("./models/dialogue", interpreter="./models/nlu/default/hacknlu")

with open("./api_config.json", 'r') as api_config:
    SLACK_TOKEN = json.load(api_config)["slack_token"]

input_channel = SlackInput(
        slack_token=SLACK_TOKEN,
        # this is the `bot_user_o_auth_access_token`
        slack_channel="@talk_to_asa"
        # the name of your channel to which the bot posts (optional)
)

# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], 5004, serve_forever=True)