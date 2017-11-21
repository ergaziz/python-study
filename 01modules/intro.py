# this is comment line.

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
    print("""list of the items after a necessary blank line: 
     """)
    # this is how we do multi line string and print
    # string can be started with ' of " but should be consistent later on.
    for item in items:
        print(item)


def main(url_arg):
    words = fetch_words(url_arg)
    print_items(words)


# __name__ is __main__ when called from command line as script.
# __name__ is intro when called as module
# so, below command works only in command line:
# $ python intro.py https://sixty-north.com/c/t.txt
if __name__ == '__main__':
    print(r"<<if __name__ == '__main__':>> is running")
    # r'asda' is for raw string
    # \n \\ \t etc are escape characters. raw string supresses them
    url = sys.argv[1]
    # for advanced cmd arg passing, use argparse or one of the many 3th party like docopt
    main(url)
