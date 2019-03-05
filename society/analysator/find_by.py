import re
def REGEXP(self, regexp, text):
	return re.findall(regexp, text)