import sys
if __name__ == "__main__":
    for line in sys.stdin:
        col = line.split(' ')[0]
        sys.stdout.write("{}\t1\n".format(col))
