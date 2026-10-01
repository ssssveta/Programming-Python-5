
import csv

def write_vector(f,v):
    a=open(f,"w")
    for x in v:
        a.write(str(x)+" ")
    a.close()

def read_vector(f):
    a=open(f,"r")
    v=list(map(float,a.read().split()))
    a.close()
    return v

def write_results(f,r):
    a=open(f,"w",newline="")
    w=csv.writer(a)
    w.writerow(["Operation","Size","Time"])
    for x in r:
        w.writerow(x)
    a.close()
