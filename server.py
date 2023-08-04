#Summer 2023
# ╭━━━╮╱╱╱╱╭╮╱╱╭━━━╮╱╭╮╭╮╱╱╱╱╱╱╭━━╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╭╮
# ┃╭━╮┃╱╱╱╱┃┃╱╱┃╭━━╯╱┃┣╯╰╮╱╱╱╱╱┃╭╮┃╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱┃┃
# ┃┃╱╰╋━━┳━╯┣━━┫╰━━┳━╯┣╮╭╋━━┳━╮┃╰╯╰┳━━┳━━┫┃╭┳━━┳━╮╭━╯┃
# ┃┃╱╭┫╭╮┃╭╮┃┃━┫╭━━┫╭╮┣┫┃┃╭╮┃╭╯┃╭━╮┃╭╮┃╭━┫╰╯┫┃━┫╭╮┫╭╮┃
# ┃╰━╯┃╰╯┃╰╯┃┃━┫╰━━┫╰╯┃┃╰┫╰╯┃┃╱┃╰━╯┃╭╮┃╰━┫╭╮┫┃━┫┃┃┃╰╯┃
# ╰━━━┻━━┻━━┻━━┻━━━┻━━┻┻━┻━━┻╯╱╰━━━┻╯╰┻━━┻╯╰┻━━┻╯╰┻━━╯
# #  # # # # # # 

import os
from flask import Flask, request, render_template, jsonify
from routes.turtle_game_routes  import main as turtle_game_blueprint
from routes.sweet_fruit_forest_routes  import fruit_forest as sweet_fruit_forest_blueprint

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')


@app.route('/', methods=['GET'])
def turtle_q3():
	return jsonify({"msg":"Bro"})


if __name__ == '__main__':
	app.register_blueprint(turtle_game_blueprint)
	app.register_blueprint(sweet_fruit_forest_blueprint)
	
	
	
	app.run(host='0.0.0.0', port=3000)
	