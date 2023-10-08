from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """<b>🤗 Hello {}

ɪ ᴀᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ ʙᴏᴛ.
Sᴇɴᴅ ᴍᴇ ᴀ ᴅɪʀᴇᴄᴛ ʟɪɴᴋ ᴀɴᴅ I ᴡɪʟʟ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ ᴀs ᴀ ғɪʟᴇ/ᴠɪᴅᴇᴏ.
Usᴇ Hᴇʟᴘ Bᴜᴛᴛᴏɴ Tᴏ Kɴᴏᴡ Hᴏᴡ Tᴏ Usᴇ Mᴇ</b>"""
    HELP_TEXT = """
𒊹︎︎︎ How To Upload File Or Media 

➪ Send Your Link For Upload File Or Media.

𒊹︎︎︎ How to set thumbnail

➪ Send Your Thumbnail Photo And Permanent Added Your Photo.

𒊹︎︎︎ How To Deleting Thumbnail

➪ Send /delthumb To Delete Your Thumbnail.

𒊹︎︎︎ How To Show Thumbnail 

➪ Send /showthumb To View Custom Thumbnail 
 
"""
    ABOUT_TEXT = """
**📛 My Name** : [ᴜʀʟ ᴜᴘʟᴏᴀᴅᴇʀ🚀](http://t.me/url_uploaderV3Bot)

**❤️ Version** : [2.3 🔥](http://t.me/EliteCraft_Studios)

**🤖 Source** : Not Available ❌

**🧿 Language** : [Python 3.10.9](https://www.python.org/)

**📢 Framework** : [Pyrogram 1.4.16](https://docs.pyrogram.org/)

**👨‍💻 Developer** : [IT'S LUFFY](https://t.me/God_Luffy_ATI)

"""


    PROGRESS = """
╭━〔PROGRESS BAR〕━◉
┃╭━━━━━━━━━━━━━━◉
┃┣⪼ 🚀 Sᴘᴇᴇᴅ : {3}/s
┃┣⪼ ⏳️ Dᴏɴᴇ : {1}
┃┣⪼ 🗂️ Tᴏᴛᴀʟ Sɪᴢᴇ : {2}
┃┣⪼ ⏱️ Tɪᴍᴇ : {4}
┃╰━━━━━━━━━━━━━◉
╰━━━━━━━━━━━━━━━◉"""


    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙️ Settings ⚙️', callback_data='OpenSettings')
        ],[
        InlineKeyboardButton('Help 🫂', callback_data='help'),
        InlineKeyboardButton('🧑‍🎓 About🧑‍🎓', callback_data='about')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Back', callback_data='home'),
        InlineKeyboardButton('🧑‍🎓 About 🧑‍🎓', callback_data='about')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Back', callback_data='home'),
        InlineKeyboardButton('🎯 Help', callback_data='help')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔒 Close', callback_data='close')
        ]]
    )
    TEXT = "sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴛᴏ sᴇᴛ ɪᴛ"
    IFLONG_FILE_NAME = " Only 64 characters can be named . "
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>No preminum plans available in this bot </b>  /help for Details"
    FORMAT_SELECTION = "<b>Select Your Format 👇\n\n🎥 Video = Upload As Streamble\n\n📂 File =Upload As File\n\n👮‍♂ Powered By :</b> @EliteCraft_Studios"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "𝘽𝙪𝙡𝙞𝙙𝙞𝙣𝙜 𝙈𝙚𝙩𝙖𝙙𝙖𝙩𝙖.."
    UPLOAD_START = "𝗥𝗲𝗰𝗲𝗶𝘃𝗶𝗻𝗴 𝙈𝙚𝙩𝙖𝙙𝙖𝙩𝙖.."
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 2GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = " OWNER : LUFFY 💕\nFor the List of Telegram Bots"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Dᴏᴡɴʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs.\n\nTʜᴀɴᴋs Fᴏʀ Usɪɴɢ Mᴇ\n\nUᴘʟᴏᴀᴅᴇᴅ ɪɴ {} sᴇᴄᴏɴᴅs"
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    SAVED_CUSTOM_THUMB_NAIL = "Save Your Thumbnail ✔️"
    DEL_ETED_CUSTOM_THUMB_NAIL = "Save Your Thumbnail ✔️."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Delete Your Thumbnail 😏."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Thumbnail 😴"
    NO_VOID_FORMAT_FOUND = "ERROR... <code>{}</code>"
    FILE_NOT_FOUND = "Error, File not Found!!"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /ren with custom thumbnail support"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS for screenshot of that specific time."""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "For the list of Telegram bots. "
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """This Bot full free"""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me 😌😉....</code>"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    CHECK_LINK = "⚡️"

