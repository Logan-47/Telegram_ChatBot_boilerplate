from flask import Blueprint, json, request
import telegram
from app.config import TELEGRAM_BOT_TOKEN as TOKEN, URL

api = Blueprint('api', 'api')

bot = telegram.Bot(token=TOKEN)

def _display_help():
    return str('help.md')

def index():
    return 'teledict SuccessFully Deployed'

def respond():
    # Message in jSON transform it to Telegram Object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    # Get Chat ID
    chat_id = update.message.chat.id
    
    # Message ID
    msg_id = update.message.message_id

    text = update.message.text.encode('utf-8').decode()
    print('Got Text:',text)

    response = 'Here is your response'

    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    return 'ok'

def set_webhook():
    hook = bot.setWebhook(f'{URL}{TOKEN}')
    if hook:
        return 'WebHook Setup Ok'
    else:
        return 'WebHook Setup Failed'



