import requests
import time

TOKEN = "SEU_TOKEN_AQUI"
CHAT_ID = "@ofertaslaripromos"

print("Bot iniciado...")

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    })

while True:
    try:
        send_message("🔥 Bot online e funcionando!")
        print("Mensagem enviada")
    except Exception as e:
        print("Erro:", e)

    time.sleep(3600)
