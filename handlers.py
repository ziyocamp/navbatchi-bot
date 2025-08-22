import datetime

from telegram import (
    Update, 
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
)
from telegram.ext import CallbackContext

from database import (
    add_user,
    get_dities_dict,
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


def select_duty_day(update: Update, context: CallbackContext):
    inline_keyboard = []

    duties = get_dities_dict()

    today = datetime.date.today()
    for _ in range(7):
        if str(today) not in duties:
            inline_keyboard.append(
                [
                    InlineKeyboardButton(str(today), callback_data=f"select_day:{str(today)}")
                ]
            )
        today += datetime.timedelta(days=1)

    update.message.reply_text(
        "Navbatchilik kunini tanlang:",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=inline_keyboard
        )
    )


def send_todays_duty(update: Update, context: CallbackContext):
    today = str(datetime.date.today())
