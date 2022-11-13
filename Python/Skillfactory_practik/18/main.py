
import telebot
from config import keys, TOKEN, slang_multi, slang_base, slang_one
from utils import ConvertionException, Converter


bot = telebot.TeleBot(TOKEN)





@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = 'Здраствуй! Я Бот-Конвертер валют и я могу:  \n- Показать список доступных валют через команду /values \
    \n- Вывести конвертацию валюты через команду <имя валюты> <в какую валюту перевести> <количество переводимой валюты>\n \
- Напомнить, что я могу через команду /help'
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать конвертацию, введите команду боту в следующем формате: \n<имя валюты> <в какую валюту перевести> <количество переводимой валюты>\
     \nДробное количество валюты необходимо вводить через точку, пример: 0.35\nЧтобы увидеть список всех доступных валют, введите команду\n/values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException(
                'Не верно введен запрос на конвертацию!\nЧто бы уточнить как правельно вводить запрос, воспользуйтесь командой /help')

        quote, base, amount = message.text.split(' ')

        t_base = Converter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.send_message(message.chat.id, f'\n{e}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Не удалось обработать комманду\n{e}')
    else:
        if float(amount) >= 2:
            text = f' Стоимость {amount} {slang_multi[quote]} в {slang_base[base]} = {t_base}'
        else:
            text = f' Стоимость {amount} {slang_one[quote]} в {slang_base[base]} = {t_base}'

        bot.send_message(message.chat.id, text)

bot.polling()