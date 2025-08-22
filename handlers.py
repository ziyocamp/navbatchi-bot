from datetime import date

from telegram import (
    Update, 
    ReplyKeyboardMarkup, KeyboardButton,
)
from telegram.ext import CallbackContext

from database import (
    add_user,
)


def start(update: Update, context: CallbackContext):
    user = update.effective_user

    add_user(
        user.id,
        user.first_name,
        user.last_name,
        user.username
    )

    update.message.reply_text(
        "salom navbatchi botga xush kelibsiz",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton("Bugungi navbatchi"), 
                    KeyboardButton("Xaftalik navbatchilar ro'yxati"),
                    KeyboardButton("Navbatchilik uchun kunni tanlash"),
                ]
            ],
            resize_keyboard=True
        )
    )


def send_todays_duty(update: Update, context: CallbackContext):
    today = str(date.today())
