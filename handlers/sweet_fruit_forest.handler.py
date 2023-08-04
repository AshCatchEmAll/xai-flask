import random

def q1_run_code(code):
    # Generating two random floating point numbers in the range [0.1, 1.0)
    float_1 = round(random.uniform(0.1, 1.0), 10)
    float_2 = round(random.uniform(0.1, 1.0), 10)

    # Test cases for converting from floating point exponential form to decimal form
    test_cases = {
        f'[{float_1}]': format(float_1, '.10f'),
        f'[{float_2}]': format(float_2, '.10f')
        # Add more test cases as necessary...
    }

    function_names = ["decimal_form_weight", "decimal_form_height"]

    results = []

    # Iterate over each test case
    for input_float, expected_output in test_cases.items():
        # Parse the input_float from string to actual float
        parsed_input = eval(input_float)[0]

        for function_name in function_names:
            full_code = f"{code}\nresult = {function_name}({parsed_input})"
            
            # Create a dictionary to serve as the local namespace when executing the code
            local_namespace = {}

            try:
                # Execute the user's code with the current test case
                exec(full_code, {}, local_namespace)

                # Get the result produced by the user's code
                result = local_namespace.get('result', None)

                # Check if the result matches the expected output
                if result == expected_output:
                    results.append({
                        'input': input_float,
                        'function': function_name,
                        'output': result,
                        'expected': expected_output,
                        'passed': True
                    })
                else:
                    results.append({
                        'input': input_float,
                        'function': function_name,
                        'output': result,
                        'expected': expected_output,
                        'passed': False
                    })
            except Exception as e:
                results.append({
                    'input': input_float,
                    'function': function_name,
                    'output': str(e),
                    'expected': expected_output,
                    'passed': False
                })

    # Return the results as JSON
    return results



def q2_run_code(code):
    # Generating two random floating point numbers in the range [0.1, 1.0)
    float_1 = round(random.uniform(0.1, 1.0), 10)
    float_2 = round(random.uniform(0.1, 1.0), 10)

    # Test cases for rounding to 3 decimal places
    test_cases = {
        f'[{float_1}]': round(float_1, 3),
        f'[{float_2}]': round(float_2, 3)
        # Add more test cases as necessary...
    }

    function_names = ["round_weight", "round_height"]

    results = []

    # Iterate over each test case
    for input_float, expected_output in test_cases.items():
        # Parse the input_float from string to actual float
        parsed_input = eval(input_float)[0]

        for function_name in function_names:
            full_code = f"{code}\nresult = {function_name}({parsed_input})"
            
            # Create a dictionary to serve as the local namespace when executing the code
            local_namespace = {}

            try:
                # Execute the user's code with the current test case
                exec(full_code, {}, local_namespace)

                # Get the result produced by the user's code
                result = local_namespace.get('result', None)

                # Check if the result matches the expected output
                if result == expected_output:
                    results.append({
                        'input': input_float,
                        'function': function_name,
                        'output': result,
                        'expected': expected_output,
                        'passed': True
                    })
                else:
                    results.append({
                        'input': input_float,
                        'function': function_name,
                        'output': result,
                        'expected': expected_output,
                        'passed': False
                    })
            except Exception as e:
                results.append({
                    'input': input_float,
                    'function': function_name,
                    'output': str(e),
                    'expected': expected_output,
                    'passed': False
                })

    # Return the results as JSON
    return results



def q3_run_code(code):
    # Generating four random floating point numbers in the range [0.1, 1.0)
    float_1 = round(random.uniform(0.1, 1.0), 3)
    float_2 = round(random.uniform(0.1, 1.0), 3)
    float_3 = round(random.uniform(0.1, 1.0), 3)
    float_4 = round(random.uniform(0.1, 1.0), 3)

    # Test cases for calculating the BMI and rounding to 2 decimal places
    test_cases = {
        f'[{float_1}, {float_2}]': round(float_2 / float_1 ** 2, 2),
        f'[{float_3}, {float_4}]': round(float_4 / float_3 ** 2, 2)
        # Add more test cases as necessary...
    }

    function_name = "bmi"

    results = []

    # Iterate over each test case
    for input_floats, expected_output in test_cases.items():
        # Parse the input_float from string to actual float
        parsed_inputs = eval(input_floats)

        full_code = f"{code}\nresult = {function_name}(*{parsed_inputs})"
        
        # Create a dictionary to serve as the local namespace when executing the code
        local_namespace = {}

        try:
            # Execute the user's code with the current test case
            exec(full_code, {}, local_namespace)

            # Get the result produced by the user's code
            result = local_namespace.get('result', None)

            # Check if the result matches the expected output
            if result == expected_output:
                results.append({
                    'input': input_floats,
                    'function': function_name,
                    'output': result,
                    'expected': expected_output,
                    'passed': True
                })
            else:
                results.append({
                    'input': input_floats,
                    'function': function_name,
                    'output': result,
                    'expected': expected_output,
                    'passed': False
                })
        except Exception as e:
            results.append({
                'input': input_floats,
                'function': function_name,
                'output': str(e),
                'expected': expected_output,
                'passed': False
            })

    # Return the results as JSON
    return results
