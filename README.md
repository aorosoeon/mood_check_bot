# mood_check_bot
Chatbot for Telegram, which checks your mood a couple of times per day (by sending a message to you) and in case of difficult emotions gives you a list of coping strategies to replace negative patterns. Also, it is available whenever needed, so you can record your mood anytime and get help from it.

I used:
1. AsyncTelebot and a couple of other classes from pyTelegramBotAPI package for connecting to Telegram API
2. wraps from functools for creating private access mode (the idea is not mine, I used code from stackoverflow user "S.D." (https://stackoverflow.com/questions/55437732/how-to-restrict-the-acess-to-a-few-users-in-pytelegrambotapi/68229442#68229442)
3. aioschedule for creating a timer
4. asyncio for gathering two tasks - bot.infinity_polling and scheduler

Initially, I planned to build synchronous code, but there was a need to combine two continuous tasks. The first one is checking whether users send something to the bot and the second one is running jobs that are scheduled. So, I chose to make this script asynchronous.

I run this program from VM in Google Cloud using "nohup" command for continuous work.
