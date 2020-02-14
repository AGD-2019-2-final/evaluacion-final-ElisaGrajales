import sys
if __name__=="__main__":
    for linea in sys.stdin:
        col1=linea.split(',')[0]
        col2=linea.split(',')[1] 
        col2=int(col2)
        sys.stdout.write("{}\t{}\t{}\n".format(col2,col1,col2))
