import os 
import requests 

#group me service responsible for sending messages to groupme. 
class GroupMeService: 

    def __init__(self): 
        # user token for the indivdial that registers the bot.
        # must be a member of the group in groupId  
        self.userAccessToken = os.environ["ACCESS_TOKEN"]
        # id of the group that this bot should live in. 
        self.groupId = os.environ["GROUP_ID"]
        # the bot Id will be set at the time of registration 
        self.botId = ""
        self.botName = os.environ["BOT_NAME"]
        # the url that Group me should send messages to when a new message is posted in the chat. 
        try:
            self.callbackURL = os.environ["CALLBACK_URL"]
        except KeyError as err:
            print("Warning: there is not a callback url set in the .env file.\nGroupMe will not be able to send messages to this bot.")
            self.callbackURL = ""

    
    def registerBot(self):
        print("registering bot")

        #body of the registration post. 
        payload = {
            "bot": {
                "name": self.botName,
                "group_id": self.groupId,
            }
        }

        # if callback url is set, use it. 
        if(self.callbackURL != ""):
            print("using callback url: ", self.callbackURL)
            payload["bot"]["callback_url"] = self.callbackURL
    
        # post request to register bot
        registration = requests.post("https://api.groupme.com/v3/bots?token=" + os.environ["ACCESS_TOKEN"], json=payload)
        print(registration.json())

        self.botId = registration.json()["response"]["bot"]["bot_id"]

    def sendMessage(self, msgContent):
        payload = {
            "bot_id": self.botId,
            "text": msgContent
        }

        sendMessage = requests.post("https://api.groupme.com/v3/bots/post", json=payload)
        print(sendMessage.json)
    
    def teardown(self):
        # to remove the instance of the bot. 
        requests.post("https://api.groupme.com/v3/bots/destroy?token=" + str(self.userAccessToken) + "&bot_id="+ self.botId)
        
        
