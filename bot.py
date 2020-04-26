#Для начяла нужно импортировать фали с помощю апдейтера Updater с библеотеки ###
#Updater соединяе мене з айпишкой телеги#
#Для того чтобы бот реагирувал на команду старт имопортируеться соманд хендлер
#Для отчета добавляем ипорт логинг - встроенний в пайтон
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename="bot.log"
                    )

#Добавляем код на githab


# обработчик 
def greet_user(bot, update):
    #Виводить текст в командрій строци 
    text ='Визов/start'
    print(text)
    
    #отвичяе пользователю
    update.messrge.reply_text(text)


# создаеться переменная с названием юзер текст в которую кладется то что пришло з абдейт юзер текс,сообщение прльзоватиля. и пичятаеться в консоль це принт. 3 команда отпраляе то что нам прислал юзер
def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал {}".format(update.message.chat.first_name, update.message.text)
    
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)

    update.message.reply_text(user_text)



#Тело бота це функция ии можна назвать мейн, запускалка нашого бота 
def main():
    #дальше переменна # Ключик бота 
    mybot = Updater(settings.API_KEY)  
    
    #Добавляем функицию яка передае инфо в наши логи
    logging.info("bot star")

     #Переводим  в переменную для легкость читания
     #реагируе на оосбщение входящи о отсилае на получятелей 
    dp = mybot.dispatcher 
    dp.add_handler(CommandHandler("start", greet_user))
    #данний код реагируе на тексови сообщения и звязаний з функицей ток туми
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # це значить начни ходить на платформу телеграм и провиряй наличие сообщений
    mybot.start_polling()

    #це ознаяе що бот будет работать пока принудительно його не остановиш
    mybot.idle()





#тепер пишельтя опридиленный код який буду при визови роботать
main()