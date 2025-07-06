""" Task 23 - Debugging - The Stack Trace - Task"""
"""
Fixes:

1) - SyntaxError: unterminated string literal (detected at line 35)
Correct by adding a "\" escape character.
2) - TypeError: print_values_of() takes 2 positional arguments but 4
were given.
Corrected by encasing the keys in a comma separate key object.
3) - NameError: name 'k' is not defined
Replaced typo 'k' with name of the looping variable 'key'
"""

# Function to print dictionary values given the keys


def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])


# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": 'd\'oh!',
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases, {'lisa', 'bart', 'homer'})

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''
