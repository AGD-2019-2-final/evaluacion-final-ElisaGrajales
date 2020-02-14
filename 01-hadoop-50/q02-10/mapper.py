import sys
if __name__ == "__main__":
    for line in sys.stdin:
        col1 = line.split(',')[3]
        col2 = line.split(',')[4]
        sys.stdout.write("{}\t{}\n".format(col1,col2))
