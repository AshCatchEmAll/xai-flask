from flask import Blueprint, request, jsonify
from handlers.turtle_game_handlers import q1_run_code, q2_run_code, q3_run_code, q4_run_code
main = Blueprint('main', __name__)

@main.route('/turtle_game/q1', methods=['POST'])
def tutle_q1():
	user_code = request.json['code']
	results = q1_run_code(user_code)

	return jsonify(results)


@main.route('/turtle_game/q2', methods=['POST'])
def turtle_q2():
	user_code = request.json['code']
	results = q2_run_code(user_code)

	return jsonify(results)


@main.route('/turtle_game/q3', methods=['POST'])
def turtle_q3():
	user_code = request.json['code']
	results = q3_run_code(user_code)

	return jsonify(results)


@main.route('/turtle_game/q4', methods=['POST'])
def turtle_q4():
	user_code = request.json['code']
	results = q4_run_code(user_code)

	return jsonify(results)
