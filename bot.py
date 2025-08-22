from config import BOT_TOKEN
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler, Filters,
)
from handlers import (
    start,
    send_todays_duty,
    select_duty_day,
)


def main() -> None:
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher

    # add command handler
    dispatcher.add_handler(CommandHandler('start', start))

    # add message handler
    dispatcher.add_handler(MessageHandler(Filters.text("Bugungi navbatchi"), send_todays_duty))
    dispatcher.add_handler(MessageHandler(Filters.text("Navbatchilik uchun kunni tanlash"), select_duty_day))

    updater.start_polling()
    updater.idle()

main()
