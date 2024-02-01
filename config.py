import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23849039"))
    API_HASH = os.environ.get("API_HASH", "1673e33ac8001f6c446485b3bfd6cefa")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5953203882:AAHfXj42Z-zwFsfRL0BMdjF4gPWV2mJLUSU")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "559714445")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://raj91r:C3YFhuq32HUtI6mS@cluster0.np8pk.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "bot")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002011714011"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "filee_store_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
