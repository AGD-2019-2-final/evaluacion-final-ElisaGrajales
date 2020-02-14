import sys
if __name__ == "__main__":
    for line in sys.stdin:
        col = line.split('   ')[0]
        val1 = line.split('   ')[1]
        val2 = line.split('   ')[2].strip()
        sys.stdout.write("{}\t{}\t{}\n".format(col,val1,val2))
