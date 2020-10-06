""" This validates input and formats the output of test_name and test_score, or invalid output
    :param test_name, a string with a test name
    :param test_score, optional int between 0-100. default = 0
    :param invalid_message, optional string with message to output if input is invalid. default = 'Invalid test score, try again!'
    :returns the formatted output with test_name and validated test_score. Else returns invalid_message
    """


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):

    # return {test_name: test_score}
    return str(test_name) + ": " + str(test_score)
