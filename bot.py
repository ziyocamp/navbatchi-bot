from config import BOT_TOKEN
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler, Filters,
    CallbackQueryHandler,
)
from handlers import (
    start,
    send_todays_duty,
    send_available_days,
    select_duty_day,
    send_weekly_duties,
)


def main() -> None:
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler('start', start))

    
    dispatcher.add_handler(MessageHandler(Filters.text("Bugungi navbatchi"), send_todays_duty))
    dispatcher.add_handler(MessageHandler(Filters.text("Navbatchilik uchun kunni tanlash"), send_available_days))
    dispatcher.add_handler(MessageHandler(Filters.text("Xaftalik navbatchilar ro'yxati"),send_weekly_duties))

    
    dispatcher.add_handler(CallbackQueryHandler(select_duty_day, pattern='select_day:'))

    updater.start_polling()
    updater.idle()

main()
