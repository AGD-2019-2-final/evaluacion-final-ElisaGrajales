import sys
if __name__ == "__main__":
    for line in sys.stdin:
        col1= line.split('   ')[0]
        col2 = line.split('   ')[2].strip()
        sys.stdout.write("{}\t{}\n".format(col1,col2))
