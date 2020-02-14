import sys
if __name__ == '__main__':

    curkey = None
    suma = 0
    x=0
    prom=0

    for line in sys.stdin:

        key, val = line.split("\t")
        val=float(val)
        
        if key == curkey:
            suma = suma + val
            x += 1
            prom = suma / x

        else:
            if curkey is None:
                curkey = key
                suma = val
                x = 1
                prom = suma / x
            else:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma,prom))
                curkey = key
                suma = val
                x = 1
                prom = suma / x

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma,prom))
