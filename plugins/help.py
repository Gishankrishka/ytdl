from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"ᴄᴜʀʀᴇɴᴛʟʏ ᴏɴʟʏ sᴜᴘᴘᴏʀᴛs ʏᴏᴜᴛᴜʙᴇ sɪɴɢʟᴇ  (ɴᴏ ᴘʟᴀʏʟɪsᴛ) ᴊᴜsᴛ sᴇɴᴅ ʏᴏᴜᴛᴜʙᴇ ᴜʀʟ"
    await message.reply_text(helptxt)
