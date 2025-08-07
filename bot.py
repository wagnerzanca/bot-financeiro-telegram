import telebot
import os

# Pega o token do ambiente, uma prática segura para produção
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

if not TELEGRAM_TOKEN:
    print("ERRO: Token do Telegram não encontrado! Defina a variável de ambiente TELEGRAM_TOKEN.")
    exit()

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'ajuda'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Sou o Assistente Financeiro V2. Estou online e pronto para evoluir!")

print("Bot V2 iniciado...")
bot.infinity_polling() # Usa infinity_polling para mais estabilidade
