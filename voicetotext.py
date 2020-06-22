# by @laciamemeframe

# by @laciamemeframe

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils

def register(cb):
    cb(TextMod())
class TextMod(loader.Module):
	"""Перевод голосовые сообщения в текст с помощью бота @voice_2_text_bot"""
	strings = {'name': 'voicetotext'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []

	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
        
	async def tcmd(self, message):
		""".t Ответить на голосовое сообщение"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("Ответь на голосовое сообщение")
			return
		try:
			voice = reply.voice
		except:
			await message.edit("Поддерживает только голосовые сообщения!!!")
			return
		chat = '@voice_2_text_bot'
		await message.edit('@voice_2_text_bot <code>обработка...</code>')
		async with message.client.conversation(chat) as conv:
			try:
				response = conv.wait_event(events.NewMessage(incoming=True, from_users=833525928))
				await message.client.send_file(chat, voice)
				response = await response
			except YouBlockedUserError:
				await message.reply('<code>Разблокируй бота</code> @voice_2_text_bot')
				return
			await message.delete()
			await message.client.send_message(message.to_id, response.text)