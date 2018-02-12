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
