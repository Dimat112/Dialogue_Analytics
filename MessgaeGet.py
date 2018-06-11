import vk
import time
import codecs
from Configuration import *
from tqdm import tqdm
from Stat import main

start = 0

#Создаем сессию
session = vk.Session(access_token=TOKEN)
api = vk.API(session, v = version_api )


#Достаем список сообщений	
def messages_get(my_id, friend_id, reverse = 1):
	messages = api.messages.getHistory(uid=my_id, offset=start, user_id=friend_id, rev=reverse, count=200)
	return messages
count = messages_get(MY_ID, FRIEND_ID, reverse)['count'] #Количество сообщений

print("Общее количество сообщений:", count,"\n")
pbar = tqdm(total=messages_get(MY_ID, FRIEND_ID, reverse)['count']) #Значение progress bar
while count > 0:
	time.sleep(4)
	count -= 200
	start += 201
	pbar.update(200)
	for text in messages_get(MY_ID, FRIEND_ID, reverse)['items']:
		body = text['body']
		with codecs.open("messages_" + Friend_Name + ".txt", "a", "utf-8") as text_file:
			text_file.write(body + "\n")

main()