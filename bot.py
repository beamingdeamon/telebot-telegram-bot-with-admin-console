import telebot
from dotenv import dotenv_values
from db import get_products , insert_request
from datetime import datetime

config = dotenv_values(".env")

token=config["TELEGRAMTOKEN"]
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет, тебя приветствует компания BITS IT.")
  bot.send_message(message.chat.id,"В данном боте ты можешь посмотреть спектр услуг, которые мы предоставляем и оставить заявку")
  products = get_products()
  index = 1
  index_array = []
  id_array = []
  for product in products:
    bot.send_message(message.chat.id,str(index) + ". " + product[1] + "  Ценна: " + ("от " + str(product[2])  + " тг." if product[2] is not None else "бесплатно"))
    index_array.append(index)
    id_array.append(product[0])
    index += 1
  bot.send_message(message.chat.id,"Чтобы оставить заявку напишите номер продукта который вас заинтересовал.")
  bot.register_next_step_handler(message, get_request, index_array, id_array)
def get_request(message, index_array, id_array):
  i = 0
  current_product_id = None
  for index in index_array:
    if(int(message.text) == index):
      current_product_id = id_array[i]
  if current_product_id != None:
    bot.send_message(message.chat.id,"Можете пожалуйста ввести номер телефона по которому мы могли бы с вами связаться.")
    bot.register_next_step_handler(message, add_request, current_product_id)
  else:
    bot.send_message(message.chat.id,"Извините у нас нету такого продукта")

def add_request(message, product_id):
  bot.send_message(message.chat.id,"Cпасибо большое за выбор продукта, мы обязательно свяжемся с вами в течении 15 минут.")
  insert_request(product_id, message.text, message.from_user.first_name)
  print("NEW REQUEST FROM NUMBER : " + message.text + " , Product id : " + product_id + " , Name : " + message.from_user.first_name + "  | Date : " + datetime.now())
  

bot.infinity_polling(none_stop=True, interval=0)

print("Bot Started")