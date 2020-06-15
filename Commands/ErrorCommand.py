from Commands.BaseCommand import BaseCommand

class ErrorCommand(BaseCommand):

    def __init__(self, groupMeService, reason):
        self.groupMeService = groupMeService
        self.reason = reason

    def runCommand(self):
        self.groupMeService.sendMessage("Command could not be executed.\nReason: " + self.reason)