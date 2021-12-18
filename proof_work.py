import numpy
import hashlib
# CREATE A RANDOM STRING WITH X MISSING BYTES

# GUESS PROOF OF WORK TO MAKE X TRAILING BYTES = 0

# CLASS FOR ROUND
class Block:
    """A block object for proof of work game"""
    pattern = '0'
    enc = 'unicode_escape'
    def __init__(self, tail=1):
        self.content = numpy.random.bytes(16).decode(self.enc)
        self.tail = tail * 2
    def guess(self, g):
        s = self.content + g
        h = hashlib.md5(s.encode(self.enc)).hexdigest()
        print(h)
        result = h[-self.tail:]
        if result.isnumeric() and int(result) == 0:
            return True


def main():
    b = Block()
    while True:
        if b.guess(input('Guess: ')):
            print('Correct!')
            break
        print('Incorrect!')


if __name__ == '__main__':
    main()


