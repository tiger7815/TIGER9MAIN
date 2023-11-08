import os

API_ID = API_ID = 22866842

API_HASH = os.environ.get("API_HASH", "bf45f625b5e5e9867024bd6bf24a2e62")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6718826547:AAHevCnsIaIOw0vPTIzeGi33zGDEkkFXTxE")

PASS_DB = int(os.environ.get("PASS_DB", "7815"))

OWNER = int(os.environ.get("OWNER", 5987970971))

LOG = -1001934203319

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6090912349", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


