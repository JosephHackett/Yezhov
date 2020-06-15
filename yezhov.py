from dotenv import load_dotenv
load_dotenv()

import os
import requests
from flask import Flask
from flask import request
from GroupMe.GroupMeService import GroupMeService
from Commands.CommandLocator import CommandLocator

groupMeService = GroupMeService()
groupMeService.registerBot()
commandLocator = CommandLocator()

app = Flask(__name__)

@app.route("/", methods=['POST'])
def botRoute(): 
    if(request.get_json()["text"][0] == "%" or request.get_json()["text"][0:3] == "!#!"):
        command = commandLocator.locate(request.get_json(), groupMeService)
        command.runCommand()

    return "-", 202

if __name__ == '__main__':
    app.run(port=4200, host="localhost")