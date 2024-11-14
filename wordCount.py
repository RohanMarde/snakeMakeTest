import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description = "count the word 'the' in a text file"
    )

    parser.add_argument('--input', default=None, metavar='<str>', help="the input text")

    arg = parser.parse_args()

    inp = arg.input if arg.input else sys.stdin.read()

    count = 0

    for i in inp.split():
        if i == "the":
            count += 1

    print(count)