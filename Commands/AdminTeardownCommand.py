from Commands.BaseCommand import BaseCommand

class TeardownCommand(BaseCommand):
    
    def __init__(self, groupMeService):
        self.groupMeService = groupMeService

    def runCommand(self): 
        self.groupMeService.sendMessage("Shutting down.")
        self.groupMeService.teardown()