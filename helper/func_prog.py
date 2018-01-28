"""
Helper methods for functional programming
"""

import functools

def compose(*funcs):
    """
    Compose a list of functions into a single function
    """
    def main_func(*fargs, **fkeywords):
        """
        The composed function from list of functions provided
        The function at right runs first, so we need to reverse the list
        """

        def func_out(composed_ans, func):
            """
            Check if value is wrapped to before getting output
            """
            if isinstance(composed_ans, Wrapped):
                return func(*composed_ans.args)
            return func(composed_ans)

        return functools.reduce(func_out,
                                funcs[::-1][1:],
                                funcs[-1](*fargs, **fkeywords))

    return main_func


class Wrapped():
    """
    Wraps the return value so that compose knows what to pass
    It is a helper class for making monads
    """
    def __init__(self, to_wrap):
        self.args = to_wrap


def wrap_output(func):
    """
    HOF for wrapping the function output in `Wrapped`
    """
    def main_func(*fargs, **fkeywords):
        """
        Gets and wraps
        """
        ans = func(*fargs, **fkeywords)
        return Wrapped(ans)

    return main_func
