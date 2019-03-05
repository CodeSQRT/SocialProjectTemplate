from collections import namedtuple

class VkGroup:
	def __init__(self, vk):
		self.vk = {
			"group_wall" : None,
			"group_status" : None,
			"group_photos" : None,
			"group_info" : None,
			"group_members" : None
		}
		methods = {
			"wall.get" : "GroupWall",
			"status.get" : "GroupStatus",
			"photos.getAll" : "GroupPhotos",
			"groups.getById" : "GroupInfo",
			"groups.getMembers" : "GroupMembers",
		}
		for method, value in vk.items():
			self.__dict__['vk'][methods.get(method).lower().replace("group", "group_")] = namedtuple(methods.get(method), value.keys())(*value.values())
		self.vk = namedtuple("GroupObject", self.vk.keys())(*self.vk.values())


	def protest_potential(self):
		for post in self.vk['post']:
			an = Analysator()
			found = an.find_keywords(By.REGEXP, ["привет", "пока"], post.text)