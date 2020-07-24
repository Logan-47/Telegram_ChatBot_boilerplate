from app.api import api,index,respond,set_webhook
from app.config import TELEGRAM_BOT_TOKEN as TOKEN


api.add_url_rule(f'/', methods=['GET'], view_func=index) 
api.add_url_rule(f'/setwebhook', methods=['GET','POST'], view_func=set_webhook) 
api.add_url_rule(f'/{TOKEN}', methods=['POST'], view_func=respond) 