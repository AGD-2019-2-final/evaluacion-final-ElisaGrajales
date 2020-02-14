import sys
if __name__ == "__main__":

    for line in sys.stdin:

        col = line.rstrip().split()
        
        for letter in col[1].split(','):
            sys.stdout.write("{}\t{}\t{}\n".format(letter+col[0].zfill(2),letter,col[0]))
