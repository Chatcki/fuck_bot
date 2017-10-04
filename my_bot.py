import requests
from time import sleep

class fuck_bot():
     def __init__(self,token):
         self.token=token
         self.api_url='https://api.telegram.org/bot%s/' % token
     def get_updates(self,offset=None,timeout=30):
        method='getUpdates'
        params={'timeout':timeout,'offset':offset}
        resp=requests.get(self.api_url+method,params)
        result_json=resp.json()['result']
        return result_json
     def get_last_update(self):
        get_result=self.get_updates()
        last_update=None
        if len(get_result)>0:
            last_update=get_result[-1]
        return last_update
     def send_message(self,chat_id,text='fuck you'):
        params={'chat_id':chat_id,'text':text}
        method='sendMessage'
        response=requests.post(self.api_url+method,params)
        return response

my_bot=fuck_bot('475145725:AAF1OrBCUllKhvr_3KZs8fGJWIBzf2C-sFA')
last_update=my_bot.get_last_update()
update_id=last_update['update_id']
while True:
    if update_id==my_bot.get_last_update()['update_id']:
        my_bot.send_message(my_bot.get_last_update()['message']['chat']['id'])
        update_id+=1
