# Created by :- @ImmortalsXKing

import httpx
from pyrogram import filters
from REPO import pbot as app

api_key = ""  # Go to @MikuNakanoXBot and do /token and get your api key

@app.on_message(filters.command("generate"))
async def alpha_coder(client, message):
    text = message.text.split("/generate")[1]
    params = {
        "api_key": api_key,
        "prompt": text
    }
    temp = await message.reply_text("**Creating Artificial Image....**")
    async with httpx.AsyncClient() as client:
        response = await client.post("https://miku-api-72b549cb8ae1.herokuapp.com/text2img", json=params, timeout=10.0)
        if response.status_code == 200:
            try:
                response_data = response.json()
                await temp.delete()
                await message.reply_photo(photo=response_data['image'])
            except ValueError:
                await temp.edit("**Error Decoding JSON Report At @MikuNakanoXSupport**")
        else:
            await temp.edit("**Api Is Currently Down.**")
