""" Task 21 - Programming with Built-in Functions - Task 02"""
import pyjokes
import random
# Had some initial challenges with installing the 3rd party module in the
# python shell, and with the help of
# https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/
# I managed to create a virtual environment 'vern' to install the necessary
# pip modules. Please refer to the above link for installation and activation
# in your IDE if you've not already installed it. It's also too large to
# include in the GitHub upload.

# Reads, clean, appends and randomizes the output. Referred to the
# pynative
# documentation.

jokes = []
for joke in pyjokes.get_jokes():
    lines = joke.strip()
    jokes.append(lines)
print(random.choice(jokes))
