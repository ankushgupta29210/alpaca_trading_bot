import requests

class TelegramAlert:
    def __init__(self, token: str, chat_id: int):
        self.token = token
        self.chat_id = chat_id
        self.api_url = f"https://api.telegram.org/bot{self.token}/sendMessage"

    def send_message(self, message: str):
        payload = {
            "chat_id": self.chat_id,
            "text": message
        }
        try:
            response = requests.post(self.api_url, data=payload)
            result = response.json()
            if result.get("ok"):
                print("✅ Telegram message sent successfully.")
            else:
                print(f"❌ Telegram API error: {result}")
        except Exception as e:
            print(f"❌ Exception sending Telegram message: {e}")
