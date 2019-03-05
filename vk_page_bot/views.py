from vk_page_bot.pagebot import PageBot
from society import Person, VkGroup
import config
import json
bot = PageBot(token=config.token, vk1=config.user_token)


@bot.message_handler(text="подобрать")
def podbor(e):
	""" Подбор """
	# group = bot.vk1.groups.getById(group_ids="fz_96")[0]
	# # print(group)
	# objects = {
	# 	"groups.getById" : group,
	# 	"status.get" : bot.vk1.status.get(group_id=group['id']),
	# 	"photos.getAll" : bot.vk1.photos.getAll(owner_id=group['id'], count=200),
	# 	"groups.getMembers" : bot.vk1.groups.getMembers(group_id=group['id'])
	# }
	# group = Group(vk=objects)
	# print(group.vk)
	# person = Person(vk=objects)


	bot.send_message(text="Трулио", peer_id=e.peer_id)