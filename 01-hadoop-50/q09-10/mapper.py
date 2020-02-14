import sys
if __name__ == "__main__":
    for line in sys.stdin:
        col = line.split()[0]
        col1 = line.split()[1]
        col2 = line.split()[2]
        col2= col2.zfill(3)
        sys.stdout.write("{}\t{}\t{}\t{}\n".format(col2, col, col1, int(col2)))
