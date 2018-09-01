import sys

def spork(spoon, fork):
    """
    Return a word that is a mix of the two provided as arguments.
    Note: this function is intended to be silly. And fail some tests, too.
    """
    return spoon[:3] + fork[2:]

if __name__ == '__main__':
    print(spork(*sys.argv[1:3]))
