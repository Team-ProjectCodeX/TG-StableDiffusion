# SOURCE https://github.com/Team-ProjectCodeX
# CREATED BY :- @ImmortalsXKing
# PROVIDED BY https://t.me/ProjectCodeX


import httpx
from telegram import ParseMode, Update
from telegram.ext import CommandHandler

# REPO => Your Bots File Name
from REPO import dispatcher

api_key = (
    ""  # Go to @MikuNakanoXBot and do /token and get your api key
)


def generate_command(update: Update, context):
    text = update.message.text.split("/generate")[1].strip()
    params = {"api_key": api_key, "prompt": text}
    temp = update.message.reply_text(
        "**Creating Artificial Image....**", parse_mode=ParseMode.MARKDOWN
    )

    with httpx.Client() as client:
        response = client.post(
            "https://miku-api-72b549cb8ae1.herokuapp.com/text2img",
            json=params,
            timeout=10.0,
        )

        if response.status_code == 200:
            try:
                response_data = response.json()
                temp.delete()
                update.message.reply_photo(photo=response_data["image"])
            except ValueError:
                temp.edit_text(
                    "**Error Decoding JSON Report At @MikuNakanoXSupport**",
                    parse_mode=ParseMode.MARKDOWN,
                )
        else:
            temp.edit_text("**Api Is Currently Down.**", parse_mode=ParseMode.MARKDOWN)


# Register the '/generate' command handler
generate_handler = CommandHandler("generate", generate_command)
dispatcher.add_handler(generate_handler)
