from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

import os
import logging

# =========================================
# LOGGING
# =========================================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# =========================================
# TOKEN
# =========================================
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN not found")


# =========================================
# DATA
# =========================================
DATA = {

    "show_images": {
        "title": "UNCUT DESI WEBSERIES",
        "image": "images/demo.jpg"
    },

    "animal": {
        "title": "MEN AND ANIMALS",
        "image": "images/demo2.jpg"
    },

    "model": {
        "title": "MODEL",
        "image": "images/demo4.jpg"
    },

    "onlyfan": {
        "title": "ONLY FANS",
        "image": "images/demo5.jpg"
    },

    "omegal": {
        "title": "OMEGAL LEAKS",
        "image": "images/demo6.jpg"
    },

    "tiktok": {
        "title": "TIK TOK SHORTS",
        "image": "images/demo7.jpg"
    },

    "indian": {
        "title": "INDIAN LESBIAN",
        "image": "images/demo8.jpg"
    },

    "foreign": {
        "title": "FOREIGN LESBIAN",
        "image": "images/demo9.jpg"
    },

    "foreignshe": {
        "title": "FOREIGN SHEMALE",
        "image": "images/demo11.jpg"
    },

    "indianshe": {
        "title": "INDIAN SHEMALE",
        "image": "images/demo10.jpg"
    },

    "gay": {
        "title": "INDIAN & FOREIGN G@Y",
        "image": "images/demo12.jpg"
    },

    "russian": {
        "title": "RUSSIAN TEENS LEAK",
        "image": "images/demo13.jpg"
    },

    "school": {
        "title": "INDIAN SCHOOL GIRL",
        "image": "images/demo14.jpg"
    },

    "college": {
        "title": "COLLEGE GIRLS",
        "image": "images/demo15.jpg"
    },

    "teens": {
        "title": "INDIAN TEENS",
        "image": "images/demo16.jpg"
    },

    "oyo": {
        "title": "OYO HIDDEN CAM",
        "image": "images/demo17.jpg"
    },

    "snapchat": {
        "title": "SNAPCHAT / INSTA LEAKS",
        "image": "images/demo18.jpg"
    },

    "mms": {
        "title": "DAILY DESI MMS",
        "image": "images/demo19.jpg"
    },

    "bhabhi": {
        "title": "INDIAN BHABHI",
        "image": "images/demo20.jpg"
    },

    "room": {
        "title": "MOM ROOM LEAKS",
        "image": "images/demo21.jpg"
    },

    "touch": {
        "title": "INCEST FAMILY TOUCH",
        "image": "images/demo22.jpg"
    },

    "realmom": {
        "title": "REAL MOM - SON",
        "image": "images/demo23.jpg"
    },

    "realbro": {
        "title": "REAL BRO - SIS",
        "image": "images/demo24.jpg"
    },

    "realdad": {
        "title": "REAL DAD - DAUGHTER",
        "image": "images/demo25.jpg"
    }
}


# =========================================
# START COMMAND
# =========================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = []

    for key, value in DATA.items():

        keyboard.append([
            InlineKeyboardButton(
                text=value["title"],
                callback_data=key
            )
        ])

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text="Choose an option:",
        reply_markup=reply_markup
    )


# =========================================
# BUTTON CLICK
# =========================================
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    try:

        data = DATA.get(query.data)

        if not data:

            await query.message.reply_text(
                "Invalid option selected."
            )

            return

        image_path = data["image"]

        # CHECK FILE EXISTS
        if not os.path.isfile(image_path):

            await query.message.reply_text(
                f"Image not found:\n{image_path}"
            )

            return

        caption = f"""
☑️ {data['title']} ☑️

🔴 PREMIUM MEMBERSHIP

✅ RS • 199₹/-

♻ SELLER ID : @iambeeee
"""

        with open(image_path, "rb") as photo:

            await query.message.reply_photo(
                photo=photo,
                caption=caption
            )

    except Exception as e:

        logging.error(f"ERROR: {e}")

        await query.message.reply_text(
            f"Something went wrong:\n{e}"
        )


# =========================================
# MAIN
# =========================================
def main():

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(button_click)
    )

    print("Bot running...")

    app.run_polling(
        drop_pending_updates=True
    )


# =========================================
# START PROGRAM
# =========================================
if __name__ == "__main__":
    main()
