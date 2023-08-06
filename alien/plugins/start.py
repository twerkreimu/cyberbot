from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["start"]))
async def start(_, message):
    text= "Hey!! I am working bitch!"
    await message.reply_photo(
        caption=text,
        photo="https://i5.walmartimages.com/asr/b87a7dfa-6a8c-4f87-9b38-a56087a2384a.a977ca605954ddd3009994fc145c588c.jpeg")
