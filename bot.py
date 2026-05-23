from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

import os

# =========================
# TOKEN
# =========================
TOKEN = os.getenv("TOKEN")


# =========================
# DATA
# =========================
DATA = {
    "show_images": {
        "title": "𝐔𝐍𝐂𝐔𝐓 𝐃𝐄𝐒𝐈 𝐖𝐄𝐁𝐒𝐄𝐑𝐈𝐄𝐒",
        "image": r"images\demo.jpg"
    },
    "animal": {
        "title": "𝐌𝐄𝐍 𝐀𝐍𝐃 𝐀𝐍𝐈𝐌𝐀𝐋𝐒",
        "image": r"images\demo2.jpg"
    },
    "model": {
        "title": "𝐌𝐎𝐃𝐄𝐋",
        "image": r"images\demo4.jpg"
    },
    "onlyfan": {
        "title": "𝐎𝐍𝐋𝐘 𝐅𝐀𝐍𝐒",
        "image": r"images\demo5.jpg"
    },
    "omegal": {
        "title": "𝐎𝐌𝐄𝐆𝐀𝐋 𝐋𝐄𝐀𝐊𝐒",
        "image": r"images\demo6.jpg"
    },
    "tiktok": {
        "title": "𝐓𝐈𝐊 𝐓𝐎𝐊 𝐒𝐇𝐎𝐑𝐓𝐒",
        "image": r"images\demo7.jpg"
    },
    "indian": {
        "title": "𝐈𝐍𝐃𝐈𝐀𝐍 𝐋𝐄𝐒𝐁𝐈𝐀𝐍",
        "image": r"images\demo8.jpg"
    },
    "foreign": {
        "title": "𝐅𝐎𝐑𝐄𝐈𝐆𝐍 𝐋𝐄𝐒𝐁𝐈𝐀𝐍",
        "image": r"images\demo9.jpg"
    },
    "foreignshe": {
        "title": "𝐅𝐎𝐑𝐄𝐈𝐆𝐍 𝐒𝐇𝐄𝐌𝐀𝐋𝐄",
        "image": r"images\demo11.jpg"
    },
    "indianshe": {
        "title": "𝐈𝐍𝐃𝐈𝐀𝐍 𝐒𝐇𝐄𝐌𝐀𝐋𝐄",
        "image": r"images\demo10.jpg"
    },
    "gay": {
        "title": "𝐈𝐍𝐃𝐈𝐀𝐍 & 𝐅𝐎𝐑𝐄𝐈𝐆𝐍 𝐆@𝐘",
        "image": r"images\demo12.jpg"
    },
    "russian": {
        "title": "𝐑𝐔𝐒𝐒𝐈𝐀𝐍 𝐓𝐄𝐄𝐍𝐒 𝐋𝐄𝐀𝐊",
        "image": r"images\demo13.jpg"
    },
    "school": {
        "title": "𝐈𝐍𝐃𝐈𝐀𝐍 𝐒𝐂𝐇𝐎𝐎𝐋 𝐆𝐈𝐑𝐋",
        "image": r"images\demo14.jpg"
    },
    "college": {
        "title": "𝐂𝐎𝐋𝐋𝐄𝐆𝐄 𝐆𝐈𝐑𝐋𝐒",
        "image": r"images\demo15.jpg"
    },
    "teens": {
        "title": "𝐈𝐍𝐃𝐈𝐀𝐍 𝐓𝐄𝐄𝐍𝐒",
        "image": r"images\demo16.jpg"
    },
    "oyo": {
        "title": "𝐎𝐘𝐎 𝐇𝐈𝐃𝐃𝐄𝐍 𝐂𝐀𝐌",
        "image": r"images\demo17.jpg"
    },
    "snapchat": {
        "title": "𝐒𝐍𝐀𝐏𝐂𝐇𝐀𝐓/𝐈𝐍𝐒𝐓𝐀 𝐋𝐄𝐀𝐊𝐒",
        "image": r"images\demo18.jpg"
    },
    "mms": {
        "title": "𝐃𝐀𝐈𝐋𝐘 𝐃𝐄𝐒𝐈 𝐌𝐌𝐒",
        "image": r"images\demo19.jpg"
    },
    "bhabhi": {
        "title": "𝐈𝐍𝐃𝐈𝐀𝐍 𝐁𝐇𝐀𝐁𝐇𝐈",
        "image": r"images\demo20.jpg"
    },
    "room": {
        "title": "𝐌𝐎𝐌 𝐑𝐎𝐎𝐌 𝐋𝐄𝐀𝐊𝐒",
        "image": r"images\demo21.jpg"
    },
    "touch": {
        "title": "𝐈𝐍𝐂𝐄𝐒𝐓 𝐅𝐀𝐌𝐈𝐋𝐘 𝐓𝐎𝐔𝐂𝐇",
        "image": r"images\demo22.jpg"
    },
    "realmom": {
        "title": "𝐑𝐄𝐀𝐋 𝐌𝐎𝐌 - 𝐒𝐎𝐍",
        "image": r"images\demo23.jpg"
    },
    "realbro": {
        "title": "𝐑𝐄𝐀𝐋 𝐁𝐑𝐎 - 𝐒𝐈𝐒",
        "image": r"images\demo24.jpg"
    },
    "realdad": {
        "title": "𝐑𝐄𝐀𝐋 𝐃𝐀𝐃 - 𝐃𝐀𝐔𝐆𝐇𝐓𝐄𝐑",
        "image": r"images\demo25.jpg"
    }
}


# =========================
# START COMMAND
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    buttons = []

    for key, value in DATA.items():
        buttons.append([
            InlineKeyboardButton(
                value["title"],
                callback_data=key
            )
        ])

    keyboard = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        "Choose an option:",
        reply_markup=keyboard
    )


# =========================
# BUTTON CLICK
# =========================
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    try:

        data = DATA.get(query.data)

        if not data:
            await query.message.reply_text("Invalid option selected.")
            return

        image_path = data["image"]

        if not os.path.exists(image_path):
            await query.message.reply_text(
                f"Image not found:\n{image_path}"
            )
            return

        caption = f"""
☑️ {data['title']} ☑️

🔴 PREMIUM MEMBERSHIP

✅️ RS • 199₹/-

♻️ SELLER ID :@iambeeee
♻️ SELLER ID :@iambeeee
"""

        with open(image_path, "rb") as photo:

            media = [
                InputMediaPhoto(
                    media=photo,
                    caption=caption
                )
            ]

            await query.message.reply_media_group(media)

    except Exception as e:
        print("ERROR:", e)

        await query.message.reply_text(
            f"Something went wrong:\n{e}"
        )


# =========================
# MAIN
# =========================
def main():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(CallbackQueryHandler(button_click))

    print("Bot running...")

    app.run_polling()


if __name__ == "__main__":
    main()
