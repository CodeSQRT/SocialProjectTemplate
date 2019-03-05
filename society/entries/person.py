from collections import namedtuple
class Person:
	def __init__(self, vk):
		self.vk = {
			"user_wall" : None,
			"user_status" : None,
			"user_photos" : None,
			"user_info" : None,
			"user_friends" : None
		}
		methods = {
			"wall.get" : "UserWall",
			"status.get" : "UserStatus",
			"photos.getAll" : "UserPhotos",
			"users.get" : "UserInfo",
			"friends.get" : "UserFriends"
		}
		for method, value in vk.items():
			self.__dict__['vk'][methods.get(method).lower().replace("user", "user_")] = namedtuple(methods.get(method), value.keys())(*value.values())

		self.vk = namedtuple("UserObject", self.vk.keys())(*self.vk.values())

		