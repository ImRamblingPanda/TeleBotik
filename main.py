# импортирование всех необходимых библиотек
import telebot as tb
import cfg
import recipe
from telebot import types

# инициализация бота
client = tb.TeleBot(cfg.TOKEN)
# инициализация разметки кнопочного меню и самих кнопок
markup = types.InlineKeyboardMarkup()
item1 = types.InlineKeyboardButton(text='Макаронный тимбаль с фаршем', callback_data='Тимбаль')
item2 = types.InlineKeyboardButton(text='Альотта - мальтийский рыбный суп (Aljotta)',callback_data='Альотта')
item3 = types.InlineKeyboardButton(text='Макаронный тимбаль с творогом',callback_data='Вишенка')
markup.add(item1,item2,item3, row_width= 1)

# обработчик команд
@client.message_handler(commands=['start'])
# функция кнопочного меню
def startup(message):
    client.send_message(message.chat.id, "Привет, напиши \"рецепты\", чтобы узнать рецепты мальтийской кухни :)")
# обработчик сообщений
@client.message_handler(content_types=['text'])
# функция вызова меню
def menu(message):
    if message.text.lower() == "рецепты":
        client.send_message(message.chat.id,'Выбери нужный рецепт и нажми на кнопку', reply_markup=markup)
    else: client.send_message(message.chat.id,'Не понял тебя, попробуй напиши ещё раз')
# обработчик вызовов с кнопок
@client.callback_query_handler(func= lambda call: True)
# функция обработки запроса и отправка ответа пользователю
def answer(call):
    client.answer_callback_query(callback_query_id=call.id)
    match call.data:
        case 'Тимбаль':
            # открытие файла с изображением
            picure = open(f'pics\\{call.data}.jpg', 'rb')
            # отправка изображения сообщением
            client.send_photo(call.message.chat.id, photo=picure, caption=call.data)
            client.send_message(call.message.chat.id, recipe.take_recipe(call.data))
            client.send_message(call.message.chat.id, 'Что-нибудь ещё? Кликай ниже!', reply_markup=markup)
        case 'Альотта':
            # открытие файла с изображением
            picure = open(f'pics\\{call.data}.jpg', 'rb')
            # отправка изображения сообщением
            client.send_photo(call.message.chat.id, photo=picure, caption=call.data)
            # отправка рецепта
            client.send_message(call.message.chat.id, recipe.take_recipe(call.data))
            # отправка сообщения с дублированием меню
            client.send_message(call.message.chat.id, 'Что-нибудь ещё? Кликай ниже!', reply_markup=markup)
        case 'Вишенка':
            # открытие файла с изображением
            picure = open(f'pics\\{call.data}.jpg', 'rb')
            # отправка изображения сообщением
            client.send_photo(call.message.chat.id, photo=picure, caption=call.data)
            # отправка рецепта
            client.send_message(call.message.chat.id, recipe.take_recipe(call.data))
            # отправка сообщения с дублированием меню
            client.send_message(call.message.chat.id, 'Что-нибудь ещё? Кликай ниже!', reply_markup=markup)

# ожидание ответа от сервера telegram
client.polling(non_stop=True)
