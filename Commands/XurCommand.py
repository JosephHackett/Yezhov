import requests
import os
from Commands.BaseCommand import BaseCommand

class XurCommand(BaseCommand):

    def __init__(self, groupMeService):
        self.groupMeService = groupMeService
    
    ### TODO: complete this command. 
    # currently it calls the bungie api to get public vendors and their sale item ids 
    # needs to finish by resolving Xurs inventory and sending it back to group me 
    
    def runCommand(self):
       self. __getActivePublicVendors()
            
    def __getActivePublicVendors(self):
        headers = {'x-api-key': os.environ["BUNGIE_KEY"]}
        publicVendorList = requests.get("https://www.bungie.net/Platform/Destiny2//Vendors/?components=Vendors,VendorSales", headers= headers)
        print(publicVendorList.json())
