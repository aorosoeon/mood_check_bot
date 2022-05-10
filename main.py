from functools import wraps
from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import KeyboardButton
from telebot.types import Message
import aioschedule as schedule
import asyncio

bot = AsyncTeleBot("API_KEY")

markupYN = ReplyKeyboardMarkup(one_time_keyboard=True)
ynButton1 = KeyboardButton("Yes")
ynButton2 = KeyboardButton("Not now")
markupYN.add(ynButton1, ynButton2)

markupMood = ReplyKeyboardMarkup(one_time_keyboard=False)
mButton1 = KeyboardButton("CUSTOMIZABLE MOOD STATE 1") #example: great mood
mButton2 = KeyboardButton("CUSTOMIZABLE MOOD STATE 2") #example: good
mButton3 = KeyboardButton("CUSTOMIZABLE MOOD STATE 3") #example: neutral, little bit positive
mButton4 = KeyboardButton("CUSTOMIZABLE MOOD STATE 4") #example: neutral, little bit sad
mButton5 = KeyboardButton("CUSTOMIZABLE MOOD STATE 5") #example: sad
mButton6 = KeyboardButton("CUSTOMIZABLE MOOD STATE 6") #example: very bad
markupMood.add(mButton1, mButton2, mButton3, mButton4, mButton5, mButton6)

def is_known_username(username):
	known_usernames = ["CHAT_ID"] #chat id needs to be int, I use string here as a placeholder
	return username in known_usernames

def private_access():
	def deco_restrict(f):
		@wraps(f)
		async def f_restrict(message, *args, **kwargs):
			username1 = message.chat.id
			if is_known_username(username1):
				return await f(message, *args, **kwargs)
			else:
				await bot.send_message(message.chat.id, "Who are you? Keep on walking...")
		return f_restrict
	return deco_restrict

@bot.message_handler(commands=['start'])
@private_access()
async def send_welcome(message: Message):
	await bot.send_message(message.chat.id, "Hi! Let's check your mood. Would you like to?", reply_markup=markupYN)

@bot.message_handler()
@private_access()
async def options(message: Message):
	if message.text == "Yes":
		await bot.send_message(message.chat.id, "How would you rate your mood?", reply_markup=markupMood)
	if message.text == "Not now":
		await bot.send_message(message.chat.id, "Sure, text me when you can")
	if message.text == "CUSTOMIZABLE MOOD STATE 1":
		await bot.send_message(message.chat.id, "CUSTOMIZABLE RESPONSE WITH APPRECIATION OF POSITIVE MOOD")
	if message.text == "CUSTOMIZABLE MOOD STATE 2":
		await bot.send_message(message.chat.id, "CUSTOMIZABLE RESPONSE WITH APPRECIATION OF POSITIVE MOOD")
	if message.text == "CUSTOMIZABLE MOOD STATE 3":
		await bot.send_message(message.chat.id, "CUSTOMIZABLE RESPONSE WITH APPRECIATION OF POSITIVE MOOD")
	if message.text == "CUSTOMIZABLE MOOD STATE 4":
		await bot.send_message(message.chat.id, "CUSTOMIZABLE RESPONSE WITH LIST OF COPING STRATEGIES")
	if message.text == "CUSTOMIZABLE MOOD STATE 5":
		await bot.send_message(message.chat.id, "CUSTOMIZABLE RESPONSE WITH LIST OF COPING STRATEGIES")
	if message.text == "CUSTOMIZABLE MOOD STATE 6":
		await bot.send_message(message.chat.id, "CUSTOMIZABLE RESPONSE WITH LIST OF COPING STRATEGIES")

async def reminder():
	await bot.send_message("CHAT_ID", "How are you?", reply_markup=markupMood)

schedule.every().day.at("FIRST_TIME").do(reminder)
schedule.every().day.at("SECOND_TIME").do(reminder)
schedule.every().day.at("THIRD_TIME").do(reminder)

async def scheduler():
	while True:
		await schedule.run_pending()
		await asyncio.sleep(1)

async def main():
	await asyncio.gather(bot.infinity_polling(), scheduler())

if __name__ == '__main__':
	asyncio.run(main())
