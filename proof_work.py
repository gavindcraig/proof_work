import numpy
import hashlib
import string
import itertools


class Block:
    """A block object for proof of work game"""
    pattern = '0'
    enc = 'unicode_escape'
    def __init__(self, tail=1):
        self.content = numpy.random.bytes(16).decode(self.enc)
        self.tail = tail * 2
    def guess(self, g):
        # GUESS PROOF OF WORK TO MAKE X TRAILING BYTES = 0
        s = self.content + g
        h = hashlib.md5(s.encode(self.enc)).hexdigest()
        result = h[-self.tail:]
        if result.isnumeric() and int(result) == 0:
            return True


def main():
    b = Block()
    i = 1
    while True:
        for c in itertools.permutations(string.ascii_letters + string.digits,
                                        i):
            if b.guess(''.join(c)):
                print('Proof of work: ' + ''.join(c))
                exit(0)
        i = i + 1


if __name__ == '__main__':
    main()

