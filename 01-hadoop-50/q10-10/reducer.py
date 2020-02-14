import sys
if __name__ == '__main__':

    curkey = None
    total = ''
    
    for line in sys.stdin:

        order, key, val = line.split("\t")
        val = val

        if key == curkey:

            total = total+','+val.rstrip()
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, total))

            curkey = key
            total = val.rstrip()
            
    sys.stdout.write("{}\t{}\n".format(curkey, total))
