'''
Handler for List question of finding min, max and sum
'''


def q1_run_code(code):
	# Test cases for find_max
	max_test_cases = {
	 '[1, 2, 3, 4, 5]': 5,
	 '[5, 4, 3, 2, 1]': 5,
	 '[5]': 5,
	 '[-1, -2, -3]': -1,
	 # Add more test cases as necessary...
	}

	# Test cases for find_min
	min_test_cases = {
	 '[1, 2, 3, 4, 5]': 1,
	 '[5, 4, 3, 2, 1]': 1,
	 '[5]': 5,
	 '[-1, -2, -3]': -3,
	 # Add more test cases as necessary...
	}

	# Test cases for find_total
	total_test_cases = {
	 '[1, 2, 3, 4, 5]': 15,
	 '[5, 4, 3, 2, 1]': 15,
	 '[5]': 5,
	 '[-1, -2, -3]': -6,
	 # Add more test cases as necessary...
	}

	test_cases = {
	 'find_max': max_test_cases,
	 'find_min': min_test_cases,
	 'find_total': total_test_cases,
	}

	results = []

	# Iterate over each function and its test cases
	for function_name, function_test_cases in test_cases.items():
		for input_list, expected_output in function_test_cases.items():
			try:
				# Construct a string of code to execute, which includes the user's code and
				# a call to the user's function with the current test case
				full_code = f"{code}\nresult = {function_name}({input_list})"

				# Create a dictionary to serve as the local namespace when executing the code
				local_namespace = {}

				# Execute the user's code with the current test case
				exec(full_code, {}, local_namespace)

				# Get the result produced by the user's code
				result = local_namespace.get('result', None)

				# Check if the result matches the expected output
				if result == expected_output:
					results.append({
					 'function': function_name,
					 'input': input_list,
					 'output': result,
					 'expected': expected_output,
					 'passed': True
					})
				else:
					results.append({
					 'function': function_name,
					 'input': input_list,
					 'output': result,
					 'expected': expected_output,
					 'passed': False
					})
			except Exception as e:
				results.append({
				 'function': function_name,
				 'input': input_list,
				 'output': str(e),
				 'expected': expected_output,
				 'passed': False
				})
				return results

	# Return the results as JSON
	return results


'''
Handler for tuple question in turtle game to reverse a tuple
'''


def q2_run_code(code):
	# Test cases for reversing a tuple
	test_cases = {
	 '(1, 2, 3, 4, 5)': (5, 4, 3, 2, 1),
	 '(5, 4, 3, 2, 1)': (1, 2, 3, 4, 5),
	 '(5,)': (5, ),
	 '(1, 2, -3)': (-3, 2, 1),
	 # Add more test cases as necessary...
	}

	results = []

	# Iterate over each test case
	for input_tuple, expected_output in test_cases.items():
		# Construct a string of code to execute, which includes the user's code and
		# a call to the user's function with the current test case
		try:
			full_code = f"{code}\nresult = reverse_tuple({input_tuple})"

			# Create a dictionary to serve as the local namespace when executing the code
			local_namespace = {}

			# Execute the user's code with the current test case
			exec(full_code, {}, local_namespace)

			# Get the result produced by the user's code
			result = local_namespace.get('result', None)

			# Check if the result matches the expected output
			if result == expected_output:
				results.append({
				 'input': input_tuple,
				 'output': result,
				 'expected': expected_output,
				 'passed': True
				})
			else:
				results.append({
				 'input': input_tuple,
				 'output': result,
				 'expected': expected_output,
				 'passed': False
				})
		except Exception as e:
			results.append({
			 'input': input_tuple,
			 'output': str(e),
			 'expected': expected_output,
			 'passed': False
			})
			return results

	# Return the results as JSON
	return results


'''
Handler for deleting keys in dictionary
'''


def q3_run_code(code):
	# Test cases for deleting key-value pairs from a dictionary
	test_cases = {
	 '{"k1": 1, "k2": 2, "k3": 3}': {
	  "k1": 1
	 },
	 '{"k1": "val1", "k2": "val2", "k3": "val3"}': {
	  "k1": "val1",
	 },
	 '{"k1": [1, 2, 3], "k2": [4, 5, 6],"k3": [7, 8, 9]}': {
	  "k1": [1, 2, 3]
	 },
	 # Add more test cases as necessary...
	}

	results = []

	# Iterate over each test case
	for input_dict, expected_output in test_cases.items():
		# Construct a string of code to execute, which includes the user's code and
		# a call to the user's function with the current test case
		try:
			full_code = f"{code}\nresult = delete_keys({input_dict})"

			# Create a dictionary to serve as the local namespace when executing the code
			local_namespace = {}

			# Execute the user's code with the current test case
			exec(full_code, {}, local_namespace)

			# Get the result produced by the user's code
			result = local_namespace.get('result', None)

			# Check if the result matches the expected output
			if result == expected_output:
				results.append({
				 'input': input_dict,
				 'output': result,
				 'expected': expected_output,
				 'passed': True
				})
			else:
				results.append({
				 'input': input_dict,
				 'output': result,
				 'expected': expected_output,
				 'passed': False
				})
		except Exception as e:
			results.append({
			 'input': input_dict,
			 'output': str(e),
			 'expected': expected_output,
			 'passed': False
			})
			return results

	# Return the results as JSON
	return results


'''
Handler for intersection operation on sets
'''


def q4_run_code(code):
	# Test cases for performing intersection operations on sets
	test_cases = {
	 '[{1, 2, 3, 4, 5}, {4, 5, 6, 7, 8}]': {4, 5},
	 '[{1, 2, 3}, {4, 5, 6}]': set(),
	 '[{"apple", "banana", "cherry"}, {"banana", "cherry", "date"}]':
	 {"banana", "cherry"},
	 # Add more test cases as necessary...
	}

	results = []

	# Iterate over each test case
	for input_sets, expected_output in test_cases.items():
		# Construct a string of code to execute, which includes the user's code and
		# a call to the user's function with the current test case
		try:
			# Parse the input_sets from string to actual sets
			parsed_input = eval(input_sets)
			setA, setB = parsed_input[0], parsed_input[1]
			print(setA, setB)
			full_code = f"{code}\nresult = intersect_sets({setA}, {setB})"

			# Create a dictionary to serve as the local namespace when executing the code
			local_namespace = {}

			# Execute the user's code with the current test case
			exec(full_code, {}, local_namespace)

			# Get the result produced by the user's code and convert it to list
			result = local_namespace.get('result', None)

			# make result into a set string

			print(f"Result {result}")
			# Check if the result matches the expected output
			if result == expected_output:
				results.append({
				 'input': str(input_sets),
				 'output': str(result),
				 'expected': str(expected_output),
				 'passed': True
				})
			else:
				results.append({
				 'input': str(input_sets),
				 'output': str(result),
				 'expected': str(expected_output),
				 'passed': False
				})
		except Exception as e:
			results.append({
			 'input': str(input_sets),
			 'output': str(e),
			 'expected': str(expected_output),
			 'passed': False
			})
			return results

	# Return the results as JSON
	return results
