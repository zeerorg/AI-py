"""
Input/Output composable functions
"""

from helper.func_prog import wrap_output

@wrap_output
def func_print(*args):
    """
    Print a list of values
    """
    print(*args)
    return args

def get_input(input_message: str) -> str:
    """
    Gets string from stdin
    """
    return input(input_message)
