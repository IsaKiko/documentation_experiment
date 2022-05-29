# from documentation_experiment.greetings import Greeting
from documentation_experiment.constants import HELLO
from documentation_experiment.dataclasses import Greeting

def say_hello(greeting: Greeting) -> str:
    """
    A function that greets you if you say hello.
    :param greeting: The greeting you want to say
    :returns: A greeting... or not
    """
    if greeting.message.lower() == "hello":
        return "Hello back"
    else:
        return HELLO