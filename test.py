from telethon.sync import TelegramClient
from telethon import functions, types
from auth_data import user_id

api_id = 8813588
api_hash = "ac086addeaa7ccc74d93c9d785488914"

name = "MyBot"

with TelegramClient(name, api_id, api_hash) as client:
    result = client(functions.channels.InviteToChannelRequest(
        channel='username',
        users=['username']
    ))
    print(result.stringify())