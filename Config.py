import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "JMTHON_ROBOT")
    SUPPORT = os.environ.get("SUPPORT", "JMTHON_SUPPORT")
    CHANNEL = os.environ.get("CHANNEL", "JMTHON")
    START_IMG  =  نظام التشغيل . بيئة . الحصول على ( "START_IMG" ، "https://telegra.ph/file/048ccbb50cb0d9c20b393.jpg" )
    CMD_IMG  =  نظام التشغيل بيئة . الحصول على ( "CMD_IMG" ، "https://telegra.ph/file/048ccbb50cb0d9c20b393.jpg" )
