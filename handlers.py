from telegram import (
    Update, 
    ReplyKeyboardMarkup, KeyboardButton,
)
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
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
