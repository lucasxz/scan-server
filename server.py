#flask imports
from flask import Flask
from flask import request

import configparser

import json

#flask setup
app = Flask(__name__)

#configparser setup dict setup
config = configparser.ConfigParser()
config.read('config/Profiles.conf')
confDict = {s:dict(config.items(s)) for s in config.sections()}

#config editing helper functions
def update():
  with open('config/Profiles.conf', 'w') as file:
    config.write(file)

def copyToIni(dic, parent):
  for k, v in dic.items():
    if isinstance(v, dict):
      copyToIni(v, k)
    else:
      config[parent][k] = v

@app.route('/')
def test():
  print(confDict)
  update()
  return 'ok';

@app.route('/get-settings', methods=['GET'])
def getSettings():
  return json.dumps(confDict)

@app.route('/set-settings', methods=['POST'])
def setSettings():
  confDict = request.json
  copyToIni(confDict, '')
  update()
  return 'success'


