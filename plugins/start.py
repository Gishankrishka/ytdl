from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('Aʙᴏᴜᴛ 👁‍🗨', callback_data="info_"),
            InlineKeyboardButton('Dᴇᴠᴇʟᴏᴘᴇʀ 👨‍💻', url="https://t.me/+D6BpKtujY844ZTRl")
            ],
            [InlineKeyboardButton('Hᴇʟᴘ ⚙️', callback_data='help_')
            ],
            [InlineKeyboardButton('- Mᴏʀᴇ Tᴏᴏʟ -', callback_data='more_')
            ],
            [InlineKeyboardButton('➕ Aᴅᴅ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕', url='http://t.me/ImPrabashbot?startgroup=true')
            ]]

)

    welcomed = f"ʜɪ <b>{message.from_user.first_name}</b>\n/ʜᴇʟᴘ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
