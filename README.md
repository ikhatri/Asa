# Asa
![redpanda](redpanda.png)

A simple slackbot that uses [Rasa NLU](https://github.com/RasaHQ/rasa_nlu) and [Rasa Core](https://github.com/RasaHQ/rasa_core) to respond to common queries that participants might have at a hackathon. Intended to be an easily extensible solution for hackathon organizers to customize for their events.

## Why the name Asa?
Asa was originally created for [HackUMass](https://www.hackumass.com) whose unofficial mascot is the [Red Panda](https://en.wikipedia.org/wiki/Red_panda). Asa is the name of a female Red Panda who currently lives at the [Smithsonian's national zoo](https://nationalzoo.si.edu/animals/red-panda).

## Installation & Local Set Up (Windows)

1. Python (preferably python 3) is required. In order to simplify the dependency process Anaconda is recommended. [Click to download.](https://www.anaconda.com/download/)
    * On windows it is recommended that you select the `Add to PATH` option if you have no other python installations.
2. Ensure that you have the Visual Studio C++ compiler. [Click here to download.](https://www.visualstudio.com/downloads/)
    * In the installer make sure you select the `Desktop development with C++` option and within the `Summary` pane on the right hand side, choose `VC++ 2015.4 v14.00 (v140) toolset for desktop`
3. Install the Rasa stack using pip. The last two commands will require you to run the command prompt as an admin in order to work.
    * `pip install rasa_core`
    * `pip install rasa_nlu[spacy]`
    * `python -m spacy download en_core_web_md`
    * `python -m spacy link en_core_web_md en`

## Installation & Local Set Up (MacOS)

1. Python (preferably python 3) is required. Again Anaconda is recommended. [Click to download.](https://www.anaconda.com/download/)
    * On MacOS you should make sure that you use the Anaconda version of Python as MacOS ships with a default Python 2.7 installation.
2. Ensure that you have Xcode. [Click to download.](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)
3. Install the Rasa stack using pip.
    * `pip install rasa_core`
    * `pip install rasa_nlu[spacy]`
    * `sudo python -m spacy download en_core_web_md`
    * `sudo python -m spacy link en_core_web_md en`

## Notes on using it
You have to create a local file called `api_config.json` with the following contents:
```json
{
    "slack_token": "Your 'Bot User OAuth Access Token' from the OAuth & Permissions tab in slack"
}
```

# Contributing

Cupcake ipsum dolor sit amet icing tiramisu marzipan donut. Sweet croissant sesame snaps sesame snaps oat cake wafer. Danish croissant toffee chocolate cake marshmallow toffee.

## License

This repository is licensed under the [MIT](https://github.com/ikhatri/hackathon-helpbot/blob/master/LICENSE) license.