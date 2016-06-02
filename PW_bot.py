import twx.botapi
import random

API_TOKEN = ""

class ProfessionalWrestlingBot:
    def __init__(self, api_token):
        self.api_token = twx.botapi.TelegramBot(api_token)
        while True:
            init_update = self.api_token.get_updates().wait()
            if init_update:
                self.id = init_update[-1].update_id
                break
        
    def update(self):
        bot_update = self.api_token.get_updates(self.id + 1, 1).wait()
        
        if bot_update:       
            self.id = bot_update[0].update_id
                        
            key_words = ["wwe", "raw", "raws", "smackdown", "smackdowns", "wrestling", "wwf", "tna", "ecw", "awa", "wcw", "wrestlemania", "mania",
                "money in the bank", "mitb", "summerslam", "nxt", "cena", "finisher", "kayfabe", "e&c", "roh", "njpw", "survivor series", "match",
                "main event", "extreme rules", "nwa", "royal rumble", "royalrumble", "rr", "seth rollins", "cm punk", "aj styles","bullet club",
                "nwo", "monday night wars", "mnw", "kenny omega", "hbk", "hhh", "triple h", "haitch", "stone cold", "steve austin"]
                            
            try:
                chat_message = bot_update[0].message.text
                chat_message = chat_message.lower()
            
                for word in key_words:
                    if word in chat_message:
                        self.reply(bot_update[0].message.chat.id)
                        
            except AttributeError:
                pass

        
    def reply(self, chat_id):
        sticker_list = ["BQADAwAD-gADYNISAeHZGGj5bf2lAg", "BQADAwAD_AADYNISATMWgCkDrasIAg", "BQADAwAD_gADYNISAYUv8q3FZOEEAg",
            "BQADAwAEAQACYNISAcMzOP9UK8pZAg", "BQADAwADAgEAAmDSEgEAAdMl_fGDsKkC"]
            
        self.api_token.send_sticker(chat_id, random.choice(sticker_list)).wait()
        
        
pw_bot = ProfessionalWrestlingBot(API_TOKEN)
while True: 
    pw_bot.update()
