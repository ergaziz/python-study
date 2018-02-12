import sys

# >>> import sys
# >>> sys.getdefaultencoding()
# 'utf-8'

def writeToFile():
    return open("myfile.txt", mode="wt", encoding="utf-8")

# Modes :
# * 'r' open for read, default
# * 'w' writing by truncating
# * 'x' create and fail if exists
# * 'a' open and append
# * 'b' binary mode
# * 't' text mode, default
# * '+' open a fisk file for updating
# * 'U' universal newlines mode. (should not be usd in new code)

# >>> import files
# >>> files.writeToFile()
# >>> f = open("myfile.txt", mode="at", encoding="utf-8")
# >>> f.write('hello file')
# 10
# >>> f.close()

def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line)

if __name__ == '__main__':
    main(sys.argv[1])


def readSeries(path):
    with open(path): # this is identical with try..finally..close structure. we need to close the file!
        return [int(line.strip()) for line in f]


# Summary of files
# Files are opened using the built-in open() function which accepts a file mode to
# control read/write/append behavior and whether the file is to be treated as raw
# binary or encoded text data
# For text data you should specify a text encoding
# Text files deal with string objects and perform universal newline translation and
# string encoding
# Binary files deal with bytes objects with no newline translation or encoding
# When writing files, it's our responsibility to provide newline characters for line
# breaks
# Files should always be closed after use
# Files provide various line-oriented methods for reading, and are also iterators which
# yield line by line
# Files are context managers and the with-statement can be used with context
# managers to ensure that clean up operations, such as closing files, are performed
# The notion of file-like-objects is loosely defined, but very useful in practice
# Exercise EAFP to make the most of them
# Context managers aren't restricted to file-like-objects. We can use tools in the
# contextlib standard library module, such as the closing() wrapper to create our
# own context managers
# help() can be used on instance objects, not just types
# Python supports bitwise operators &, | and left- and right-shifts
