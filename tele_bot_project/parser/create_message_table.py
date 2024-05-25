
import asyncpg
import asyncio
from config import *


async def creat_message_data_table():
    conn = await asyncpg.connect(user=user, password=password, database=database, host=host)
    await conn.execute('''
    CREATE TABLE IF NOT EXISTS tele_bot_app_MessageData (
    id serial,
    telegram_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT,
    message TEXT,
    full_date_time TIMESTAMP WITH TIME ZONE
    )
    ''')
    await conn.close()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(creat_message_data_table())