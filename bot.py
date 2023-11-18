import asyncio
import os
from pyrogram import Client, idle
from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6311317123:AAHcqbM9s6MwjQd-5ToPLyD4AWhv16PNV40")
API_ID = int(os.environ.get("API_ID", "23081466"))
API_HASH = os.environ.get("API_HASH", "dbc665db1489f9d3cfd8de4a52f1ad4b")
STRING = os.environ.get("STRING", "BQFgMfoAPFXBZK6bQ8MP8_cpcR0yUqwF0m_UfSKXgUKh4MKItJ01R6LAod9RDcY_eLOfQ3em7cTP9N2KEBdXq3woEqLDRn9oIBOo6O9MaFw9kNHlWULbWR6qrSPKOsfmUmTBESEem5CyN_3Me51wV8WWvYQhSWFh4f5KzpmR2kYku2qAxZSwO37YX51Wqw3uqJisvyYJypGGrOX5sOz_L_ioFcz_LfvNY-0UzJADIpdFqgiK0sR39Z_ec_G7BL5w8sjAfhKuZHpOiisVmYNJAE6gJbkI-1IU6oJT19JOguMLMaT_IVq9YCNOvw5-X0YakX95PHAM13Ho1UIkU8ptljOpDQUXVQAAAABpJ66YAA")

bot = Client(
    "Renamer",
    bot_token=TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root='plugins')
)

async def start_and_stop_apps():
    apps = [Client2, bot]
    for app in apps:
        await app.start()
    await idle()
    for app in apps:
        await app.stop()

if STRING:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_and_stop_apps())
else:
    bot.run()
