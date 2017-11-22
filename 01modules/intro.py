#!/usr/bin/env python3
# this says which interpreter to use.
# This is for linux in actually. use "chmod +x words.py" command first to mark the file.
# then you can run by "./intro.py http://url..."
# on windows, PyLauncher came to run py scripts. it locates the shebang and correct python interpreter version
# then we can run with "intro.py ..url.."

#  this is comment line by the way

# this is sample py file following pluralsight course in link below:
# https://app.pluralsight.com/library/courses/python-fundamentals/table-of-contents


from urllib.request import urlopen
import sys


# Above is import of a standard library
# batteries included philosophy : python provides many libraries that may be needed


# below is a function definition.
#
# this can be called from REPL (read eval print loop) as :
# >>> import intro
# >>> intro.fetch_words()
# or
# >>> from intro import fetch_words
# >>> fetch_words()
#
# in REPL,
# _  -> prints latest output
# control + D or control + Z -> exit
# import this -> prints zen of python
# PEP 8 - python style guide
# PEP 20 - The zen of python
def fetch_words(url_to_fetch):
    """Fetch a list of words from a URL

    Args:
        url_to_fetch: The url of a utf-8 text doc.

    Returns:
        A List of words from the doc.
    """
    # Above is the docstrings. access to it using help(fetch_words) after importing the module.
    with urlopen(url_to_fetch) as story:
        word_list = []
        for line in story:
            line_words = line.decode('utf-8').split()
            # decoded to string from bytes
            for word in line_words:
                word_list.append(word)
        return word_list


# 2 empty lines between definitions are suggested in PEP
def print_items(items):
    """Print list of items

    Args:
        items: collection of items to print.
    """
    print("""list of the items after a necessary blank line: 
     """)
    # this is how we do multi line string and print
    # string can be started with ' of " but should be consistent later on.
    for item in items:
        print(item)


def main(url_arg):
    """Fetch and print list of items from url

    Args:
        url_arg: url of the collection of items to print.
    """
    words = fetch_words(url_arg)
    print_items(words)


# __name__ is __main__ when called from command line as script.
# __name__ is intro when called as module
# so, below command works only in command line:
# $ python intro.py https://sixty-north.com/c/t.txt
if __name__ == '__main__':
    print(r"<<if __name__ == '__main__':>> is running")
    # r'asda' is for raw string
    # \n \\ \t etc are escape characters. raw string omit them
    url = sys.argv[1]  # arg 0 is module file name
    # for advanced cmd arg passing, use argparse or one of the many 3th party like docopt
    main(url)


######
    ### Summary of modules
    # * python code is in *.py files. They are called modules.
    # * python code is in *.py files. They are called modules.
    # * modules can be executed with : ```python module_name.py```
    # * import into REPL or other modules by: ```import module_name```
    # * function : ```def my_func(arg1):```
    # * ```return``` with optional parameter. No parameter returns `None`
    # * `__name__` is special parameter. it is `__main__` if called as script from cmd,
    #     it is module name (filename without py extension) if called as module.
    # * Whole module code is executed only once, on first import.
    # * `def` keyword is a statement which binds function definition to a name
    # * cmd args is acces by `sys.argv`
    # * script filename : `sys.argv[0]`
    # * docstrings are standalone literal string as the first statement of a function or module.
    # * docstrings are delimited by triple quotes
    # they provide `help()`
    # * module docstring should be placed before any other statement.
    # * comments begin with #and run to the end of the line.
    # * #! is the shebang, placed on the first line and tells the system which interpreter to use.
######