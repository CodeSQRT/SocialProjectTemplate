class Analysator:
	def __init__(self, **options):
		self.options = dict(options)

	def find_keywords(self, by, keywords, text):
		regexp = "|".join(keywords)
		return by(regexp, text)