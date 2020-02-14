import sys
if __name__ == "__main__":
    for line in sys.stdin:
        col1 = line.split("   ")[0]
        col3 = line.split("   ")[2]
        sys.stdout.write("{}\t{}".format(col1,col3))
