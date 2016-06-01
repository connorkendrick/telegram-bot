import twx.botapi
import random

API_TOKEN = "184997843:AAHctRG-dO_PDJLRnS4ppor2B8RcgvFHnTw"

class DeathGripsBot:
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
        
            key_words = ["Death Grips", "Death grips", "death grips", "DEATH GRIPS", "DeathGrips", "Deathgrips", "deathgrips", "DEATHGRIPS", "Dg", "dg", "DG"]
        
            for word in key_words:
                if word in bot_update[0].message.text:
                    self.reply(bot_update[0].message.chat.id)
        
        
    def reply(self, chat_id):
        quote_list = ["GOT THE NASTY IN MY TAXI", "YOU NEED A LIFT?", "YUH!", "I GOT SOME SHIT TO SAY JUST FOR THE FUCK OF IT",
            "DEM THANGS dem thangs", "NOIDED", "REAL SHIT", "HOT SHIT", "HAVE A SAD CUM BB", "Don't it feel good to drive a bus?",
            "I'M IN YOUR AREA", "FUCK YOU", "I'm so BLACK QUARTERBACK", "It won't lit", "SOON ALL THAT'S LEFT OF YOU IS YOUR MOST PRIMAL DESIRE",
            "FUCK WHAT YA HEARD", "DON'T GET ME WRONG", "YOU CAN SIT BETWEEN THE BACKSEAT AND MY DICK!", "Jimi Hendrix, of course. Of course.",
            "FUCK WHO'S WATCHING", "When you come out, your shit is gone", "NOW WE GOT ALL THE COCONUTS, BITCH!", "SKIIIINHEAD, SKINHEAD!",
            "IT GOES IT GOES IT GOES IT GOES", "GUILLOTIIIIIIIINE", "I AM THE BEAST I WORSHIP", "TRIPLE SIX, FIVE, FORKED, TOUNGE!",
            "HUSTLE BONES COMIN' OUT MY MOUTH!", "COME UP AND GET ME", "I'VE GOT THE POWERS THAT B!", "GET GET GET GET, GOT GOT GOT GOT",
            "IT's DEATH DEATH DEATH DEATH DEATH"]
        self.api_token.send_message(chat_id, "Did somebody say Death Grips?!" + "\n\n" + random.choice(quote_list)).wait()
        
        
dg_bot = DeathGripsBot(API_TOKEN)
while True: 
    dg_bot.update()