from flask import Blueprint, request, jsonify
from handlers.sweet_fruit_forest_handlers import q1_run_code,q2_run_code,q3_run_code
fruit_forest = Blueprint('fruit_forest', __name__)

@fruit_forest.route('/fruit_forest/q1', methods=['POST'])
def fruit_forest_q1():
	user_code = request.json['code']
	results = q1_run_code(user_code)

	return jsonify(results)



@fruit_forest.route('/fruit_forest/q2', methods=['POST'])
def fruit_forest_q2():
	user_code = request.json['code']
	results = q2_run_code(user_code)

	return jsonify(results)



@fruit_forest.route('/fruit_forest/q3', methods=['POST'])
def fruit_forest_q3():
	user_code = request.json['code']
	results = q3_run_code(user_code)

	return jsonify(results)
