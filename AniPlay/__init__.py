import os
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(os.environ.get("APP_ID", "10471716")),
    api_hash= os.environ.get("API_HASH", "f8a1b21a13af154596e2ff5bed164860"),
    bot_token= os.environ.get("TOKEN", "6916875347:AAEVxR4cO_sIBB6V57ANA92pHKxzw9G3yX0")
)
