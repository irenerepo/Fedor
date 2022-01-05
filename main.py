import telebot
import summa
import coren
import factorial
import perimetr

bot = telebot.TeleBot('5053540859:AAFa2EmdbXO1UMmU3mHTxQCDFBqqaUvKxjs')

state = {}

@bot.message_handler(commands=["start"])
def createMainMenu(message):
    main_mackup = telebot.types.ReplyKeyboardMarkup()
    main_mackup.row("Посчитать сумму всех чисел", "Найти корень числа", "Факториал числа", "Периметр и площадь квадрата")
    bot.send_message(message.from_user.id, "Сделайте выбор", reply_markup=main_mackup)

@bot.message_handler(content_types=['text'])
def keyboardActions(message):

    if message.text == "Посчитать сумму всех чисел":
        state["func"] = summa.ssummaa
        bot.send_message(message.from_user.id, "Введите любое число")

    elif message.text == "Найти корень числа":
        state["func"] = coren.coren_chisla
        bot.send_message(message.from_user.id, "Из какого числа будем извлекать корень?")

    elif message.text == "Факториал числа":
        state["func"] = factorial.ffactorial
        bot.send_message(message.from_user.id, "Введите число для которого будем искать факториал")

    elif message.text == "Периметр и площадь квадрата":
        state["func"] = perimetr.perimetr
        bot.send_message(message.from_user.id, "Введите длину стороны квадрата")
    else:
        if state.get("func") and not state.get("isMulti",False):
            try:
                n = float(message.text)
                res = state["func"](n)
                bot.send_message(message.from_user.id, res)
            except:
                bot.send_message(message.from_user.id, "")


bot.polling()



