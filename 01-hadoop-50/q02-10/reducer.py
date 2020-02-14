import sys

if __name__ == '__main__':
    curkey = None
    total = 0
    for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)
        if total == None:
            total = val
        if key == curkey:
            total = max(val,total)
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\n".format(curkey, total))
            curkey = key
            total = val  
    sys.stdout.write("{}\t{}\n".format(curkey, total))  
