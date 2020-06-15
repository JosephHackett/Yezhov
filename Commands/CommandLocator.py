import os
from Commands.XurCommand import XurCommand
from Commands.ErrorCommand import ErrorCommand
from Commands.AdminTeardownCommand import TeardownCommand

class CommandLocator: 

    def __init__(self):
        print("initalizing Command Locator.")

    def locate(self, command, groupMeService):
        parsedCommand = self.__parseCommand(command)

        if (parsedCommand["type"] == "user"):
            if(parsedCommand["args"][0] == "xur"):
                return XurCommand(groupMeService)

        elif(parsedCommand["type"] == "admin" and parsedCommand["sender"] == os.environ["ADMIN"]):
            if(parsedCommand["args"][0] == "teardown"):
                return TeardownCommand(groupMeService)    

        elif(parsedCommand["type"] == "admin" and parsedCommand["sender"] != os.environ["ADMIN"]):
            return ErrorCommand(groupMeService, reason="You aren't an admin.")
        else:
            return ErrorCommand(groupMeService, reason="could not parse.")


    def __parseCommand(self, command):

        # check if this is a standard command
        if (command["text"][0] == "%"):
            args = command["text"][1: len(command["text"])].lower().split(" ")
            sender = command["sender_id"]
            return { "type": "user", "args": args, "sender": sender}

        # check if this is an admin command 
        elif(command["text"][0:3] =="!#!"):
            args = command["text"][3: len(command["text"])].lower().split(" ")
            sender = command["sender_id"]
            return { "type": "admin", "args": args, "sender": sender}
        # else return error 
        else: 
            return {"type": "error"}