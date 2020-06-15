import abc

class BaseCommand(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'runCommand') and 
                callable(subclass.runCommand) or 
                NotImplemented)

    @abc.abstractclassmethod
    def runCommand(self):
        raise NotImplementedError