import telebot

part1 = '8791327298'
part2 = ':AAHKEEWGKE8VL9WYUCrSI09QwVrKzsnoALM'
TOKEN = part1 + part2

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🚀 أهلاً بك! بوت إشارات التداول يعمل بنجاح.")

@bot.message_handler(func=lambda message: True)
def handle_all(message):
    bot.reply_to(message, "✅ تم استلام رسالتك، البوت في الخدمة.")

print("البوت يعمل...")
bot.infinity_polling()
