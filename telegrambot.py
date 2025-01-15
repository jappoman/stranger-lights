import telepot

def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)

	if content_type == 'text':
		txt=msg['text']
		bot.sendMessage(chat_id, 'Ok, scrivo "%s" con le luci.' % txt)
		out_file = open("/home/pi/wordslist.txt","w")
		out_file.write(txt)
		out_file.close()

bot = telepot.Bot('871506086:AAGiN4Qx0mh8J-wVZlAn_DmrepDACP81Ezg')
bot.message_loop(on_chat_message)

print 'Listening ...'

import time
while 1:
    time.sleep(10)
