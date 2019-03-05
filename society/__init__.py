from society.entries.person import Person
from society.entries.group import VkGroup
from society.analysator import Analysator
import society.analysator.find_by as By
class Society:

	#Объекты VkUser
	people = []

	#Объекты VkGroup
	groups = []

	def __init__(self):
		pass


"""

#Добавление групп и людей

общество.вк_группы = []
вк_группы = вконтакте.группы.поиск(текст="Имя города")
для группа в вк_группы {
	общество.вк_группы.добавить()
}

# Процедурный код в использовании класса - Добавление людей в общество
общество.люди = Пусто
общество.вк_группы = [-1, 2, "group321123", "public123"]
для вк_группа в общество.вк_группы {
	для человек в вк_группа {
		общество.люди.добавить(новый Человек(объект_методов_вк_для_человека))
	}
}

"""