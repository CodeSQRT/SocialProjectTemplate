from flask import Flask, request
from vk_page_bot.views import bot
import json
app = Flask(__name__)
@app.route('/vk', methods=['GET', 'POST', 'DELETE'])
def vkontakte():
	data = json.loads(request.data)
	if "type" not in data.keys():
		return "not vk"
	if data['type'] == "confirmation":
		return "e0df84a3"
	elif data['type'] == "message_new":
		bot.process_new_update(data['object'])
		return 'ok'

app.run(host="0.0.0.0", debug=True, port=8080,
	ssl_context=("/etc/letsencrypt/live/vm477737.had.su/fullchain.pem",
		"/etc/letsencrypt/live/vm477737.had.su/privkey.pem")
	)