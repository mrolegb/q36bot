from secure import API_KEY
from telegram.ext import Updater, CommandHandler


def greet(bot, update):
    print("Says hi")
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Hi there")


def close(bot, update):
    print("Says bye")
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Good bye")


def respond(update):
    print("Responds")
    update.message.reply_text("I'm sorry Oleg I'm afraid I can't do that.")


def main():
    updater = Updater(API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('hi', greet))
    dp.add_handler(CommandHandler('bye', close))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
