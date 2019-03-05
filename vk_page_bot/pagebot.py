from collections import namedtuple
import vk as vk_api
import time
import threading
import random
import re
import json
class PageBot :
	"""Библиотека для быстрого создания бота для вконтакте"""
	priveleged_types = {
		"text" : r"\w+"
	}
	decorated = []
	last_update = None
	def __init__(self, token, **kwargs):
		self.vk = vk_api.API(
			vk_api.Session(access_token=token),
			v="5.92",
			lang="ru",
			timeout=10
		)
		for key, arg in kwargs.items():
			self.__dict__[key] = vk_api.API(
				vk_api.Session(access_token=arg),
				v="5.92",
				lang="ru",
				timeout=10
			)
	def message_handler(self, **kwargs):
		def decorate(function):
			def wrapper(e):
				pass
			self.decorated.append(dict(function=function, options=kwargs))
			return wrapper
		return decorate

	def process_new_update(self, update):
		counter = 0
		function = None
		start_time = time.time()
		for executable in self.decorated:
			if function == None :
				if executable['options'].get("priveleged_type") != None :
					if function == None :
						for _type, regexp in self.priveleged_types.items() :
							if len(re.findall(regexp, update["text"])) > 0:
								function = executable['function']
								break

				if len(update['attachments']) != 0 :
					if function == None :
						for attachment in update['attachments'] :
							if attachment['type'] == executable['options'].get('content_type') :
								function = executable['function']
								break
					else :
						break
				for key, option in executable['options'].items() :
					if function == None :
						for key1, option1 in update.items() :
							if key1 == key and option1 == option :
								function = executable['function']
								break
					else :
						break
			else :
				break

		if function != None :
			update['splitted'] = update['text'].split(" ")
			function(namedtuple("Update", update.keys())(*update.values()))
			print("--- %s seconds ---" % (time.time() - start_time))

	def polling(self, interval=1) :
		last_ts = None
		ts = self.vk.messages.getLongPollServer()['ts']
		while True :
			update = self.vk.messages.getLongPollHistory(
				ts=ts, fields="photo,photo_medium_rec,sex,online,screen_name"
				)['messages']['items']
			if (ts != last_ts and len(update) > 0 and update != self.last_update 
				and update[0]['from_id'] != self.vk.users.get()[0]['id']) :
				th = threading.Thread(
					target=lambda:self.process_new_update(update[0])
					)
				th.start()
				last_ts = ts
				self.last_update = update
			ts = self.vk.messages.getLongPollServer()['ts']
			time.sleep(interval)
			
	def send_message(self, peer_id, text) :
		return self.vk.messages.send(
			random_id=random.randint(0, 12000000),
			peer_id=peer_id,
			message=text
		)
