import telebot
import os
from flask import Flask
from threading import Thread

# --- CONFIGURAÇÕES ---
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

if not TELEGRAM_TOKEN:
    print("ERRO: Token do Telegram não encontrado!")
    exit()

# ---> LINHA DE DIAGNÓSTICO <---
# Vamos imprimir uma parte do token para confirmar qual está sendo usado
try:
    bot_id = TELEGRAM_TOKEN.split(':')[0]
    token_suffix = TELEGRAM_TOKEN[-6:]
    print(f"DEBUG: Token carregado com sucesso. ID do Bot: {bot_id}, Final: ...{token_suffix}")
except Exception as e:
    print(f"DEBUG: Erro ao analisar o token. O token parece estar mal formatado.")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
app = Flask('')

# --- SERVIDOR WEB PARA HEALTH CHECK DA RENDER ---
@app.route('/')
def home():
    return "Bot está vivo!"

def run_flask():
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)

# --- LÓGICA DO BOT ---
@bot.message_handler(commands=['start', 'ajuda'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Sou o Assistente Financeiro V2. Estou online e pronto para evoluir!")

# --- INICIALIZAÇÃO ---
if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    
    print("Bot V2 iniciado...")
    bot.infinity_polling()
