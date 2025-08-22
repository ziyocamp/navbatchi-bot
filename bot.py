from config import BOT_TOKEN
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler, Filters,
)
from handlers import (
    start,
    send_todays_duty,
)


def main() -> None:
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher

    # add command handler
    dispatcher.add_handler(CommandHandler('start', start))

    # add message handler
    dispatcher.add_handler(MessageHandler(Filters.text("Bugungi navbatchi"), send_todays_duty))

    updater.start_polling()
    updater.idle()

main()
