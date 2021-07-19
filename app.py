import os
api = os.getenv('ADAFRUIT_IO_KEY')
from Adafruit_IO import Client
aio = Client('devonajibu_18' , api)
from telegram.ext import Updater, MessageHandler,Filters

def lighton(bot,update):
  chat_id= bot.message.chat_id
  path='https://thumbs.dreamstime.com/b/cartoon-light-bulb-illustration-got-ideas-60593991.jpg'
  aio.send('bedroom-light', 1)
  data = aio.receive('bedroom-light')
  print(f'Received value: {data.value}')
  bot.message.reply_text('I have turned on the light!!!')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def fanon(bot,update):
  chat_id= bot.message.chat_id
  path='https://png.pngtree.com/png-clipart/20190614/original/pngtree-fan-cartoon-fan-midsummer-summer-png-image_3784724.jpg'
  aio.send('fan', 1)
  data = aio.receive('fan')
  print(f'Received value: {data.value}')
  bot.message.reply_text('I have turned on the fan!!!')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def lightoff(bot,update):
  chat_id= bot.message.chat_id
  aio.send('bedroom-light', 0)
  data = aio.receive('bedroom-light')
  print(f'Received value: {data.value}')
  path='https://image.shutterstock.com/image-photo/stock-vector-turn-off-light-finger-turning-off-light-design-saving-energy-450w-677714989.jpg'
  bot.message.reply_text('I have turned off the light!!!')  
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def fanoff(bot,update):
  chat_id= bot.message.chat_id
  aio.send('fan', 0)
  data = aio.receive('fan')
  print(f'Received value: {data.value}')
  path='https://image.shutterstock.com/image-vector/air-ventilation-off-switch-button-260nw-1584059068.jpg'
  bot.message.reply_text('I have turned off the fan!!!')  
  update.bot.sendPhoto(chat_id=chat_id,photo=path)

def main(bot,update):
  a = bot.message.text
  print(a)
  if a == "light on" or a=="switch on the light" or a== "lights" or a== "turn on light":
   lighton(bot,update) 
  elif a == "fan on" or a=="switch on the fan" or a== "some breeze please" or a== "feeling hot":
   fanon(bot,update) 
  elif a == "light off" or a == "gotta sleep" or a=="lights out" or a== "turn off light" :
    lightoff(bot,update)
  elif a == "fan off" or a == "switch off the fan" or a=="feeling cold" or a== "I'm shivering" :
    fanoff(bot,update)
  else:
     bot.message.reply_text('INVALID INPUT!!!')   


BOT_TOKEN = '1949965624:AAGKIpRbwQx40ZY4CNA8E7XmBXhJ0ndE3G0'
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
