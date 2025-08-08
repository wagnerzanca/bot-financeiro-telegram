import telebot
import os
from flask import Flask
from threading import Thread

# --- CONFIGURAÇÕES ---
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

if not TELEGRAM_TOKEN:
    print("ERRO: Token do Telegram não encontrado!")
    exit()

bot = telebot.TeleBot(TELEGRAM_TOKEN)
app = Flask('') # Cria o servidor web

# --- SERVIDOR WEB PARA HEALTH CHECK DA RENDER ---
@app.route('/')
def home():
    return "Bot está vivo!"

def run_flask():
  # O host 0.0.0.0 é essencial para a Render conseguir acessar
  # A porta é pega da variável de ambiente PORT que a Render fornece
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)

# --- LÓGICA DO BOT ---
@bot.message_handler(commands=['start', 'ajuda'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Sou o Assistente Financeiro V2. Estou online e pronto para evoluir!")

# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    # Inicia o servidor web em uma thread separada
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    print("Bot V2 iniciado...")
    # Inicia o bot
    bot.infinity_polling()
