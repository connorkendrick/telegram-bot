from twx.botapi import TelegramBot, ReplyKeyboardMarkup, ReplyKeyboardHide

"""
Setup the bot
"""

bot = TelegramBot('174835412:AAFcOcKlQgT3ZTKbQu2YyX6XS0aj7udPKvI')
bot.update_bot_info().wait()
print(bot.username)

"""
Send a message to a user
"""

user_id = int('175195250')

result = bot.send_message(user_id, 'test message').wait()
# print(result)

"""
Get updates sent to the bot
"""

# updates = bot.get_updates().wait()
# for update in updates:
    # print(update)
    
"""
Use a custom keyboard
"""
# keyboard = [
    # ['7', '8', '9'],
    # ['4', '5', '6'],
    # ['1', '2', '3'],
         # ['0']
# ]
# reply_markup = ReplyKeyboardMarkup.create(keyboard, False, True, False)

# bot.send_message(user_id, 'please enter a number', reply_markup=reply_markup).wait()

"""
Hide custom keyboard
"""

#bot.send_message(user_id, 'hide keyboard', reply_markup=ReplyKeyboardHide.create()).wait()