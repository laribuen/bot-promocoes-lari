import requests
import time

TOKEN = "COLE_SEU_TOKEN_AQUI"
CHAT_ID = "@ofertaslaripromos"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    })

offers = [
    {
        "title": "Fritadeira Air Fryer 5L",
        "price": 299.90,
        "old_price": 499.90,
        "link": "https://example.com"
    }
]

def calculate_discount(old, new):
    return int((1 - new / old) * 100)

while True:
    for o in offers:
        discount = calculate_discount(o["old_price"], o["price"])

        if discount >= 30:
            msg = f"""
🔥 <b>OFERTA IMPERDÍVEL</b>

📦 {o['title']}
💰 De R$ {o['old_price']} por R$ {o['price']}
📉 Desconto: {discount}%

👉 {o['link']}
"""
            send_message(msg)

    time.sleep(3600)
