from telegram.ext import Updater,MessageHandler,Filters

def fanon(bot,update):
  chat_id=bot.message.chat_id
  path='https://1pe0fth3fkc49y78cjoiygdd-wpengine.netdna-ssl.com/wp-content/uploads/2019/05/Ceiling-fans-can-becoming-noisy-if-not-properly-installed.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("the fan is on")
  from Adafruit_IO import Client
  aio = Client('god12', 'aio_jpFh55EyqOUZV5x43qcNTPeelbwX')
  aio.send('fan', 1)
  data = aio.receive('fan')
  print('Received value: {0}'.format(data.value))

def fanoff(bot,update):
  chat_id=bot.message.chat_id
  path='https://n3.sdlcdn.com/imgs/a/v/8/Crompton-Greaves-Amour-3-Blade-SDL965105491-1-dc2a3.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("the fan is off")
  from Adafruit_IO import Client
  aio = Client('god12', 'aio_jpFh55EyqOUZV5x43qcNTPeelbwX')
  aio.send('fan', 0)
  data = aio.receive('fan')
  print('Received value: {0}'.format(data.value))

def lighton(bot,update):
  chat_id=bot.message.chat_id
  path='https://cdn5.vectorstock.com/i/1000x1000/60/94/cartoon-glowing-yellow-light-bulb-vector-18016094.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("the light is on")
  from Adafruit_IO import Client
  aio = Client('god12', 'aio_jpFh55EyqOUZV5x43qcNTPeelbwX')
  aio.send('light', 1)
  data = aio.receive('light')
  print('Received value: {0}'.format(data.value))

def lightoff(bot,update):
  chat_id=bot.message.chat_id
  path='https://upload.wikimedia.org/wikipedia/commons/8/85/Light-bulb-1.jpg'
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
  bot.message.reply_text("light is off")
  from Adafruit_IO import Client
  aio = Client('god12', 'aio_jpFh55EyqOUZV5x43qcNTPeelbwX')
  aio.send('light', 0)
  data = aio.receive('light')
  print('Received value: {0}'.format(data.value))

def rinex(bot,update):
  a=bot.message.text.lower()
  if a=="lighton":
    lighton(bot,update)
  elif a=="lightoff":
    lightoff(bot,update)
  elif a=="fanon":
    fanon(bot,update)
  elif a=="fanoff":
    fanoff(bot,update)
  else:
    bot.message.reply_text("INVALID COMMAND")
   

BOT_TOKEN='1905724069:AAEDkogKc038vaq3lPkJ8CcjrtdeO9lRO88'
u=Updater(BOT_TOKEN,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,rinex))
u.start_polling()
u.idle()
