
def matrix_multiply(a,b):
    r=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(b[0])):
            s=0
            for k in range(len(b)):
                s=s+a[i][k]*b[k][j]
            row.append(s)
        r.append(row)
    return r

def matrix_vector_multiply(a,v):
    r=[]
    for i in range(len(a)):
        s=0
        for j in range(len(v)):
            s=s+a[i][j]*v[j]
        r.append(s)
    return r

def matrix_trace(a):
    s=0
    for i in range(len(a)):
        s=s+a[i][i]
    return s

def scalar_product(a,b):
    s=0
    for i in range(len(a)):
        s=s+a[i]*b[i]
    return s

def histogram(v,n):
    x=min(v)
    y=max(v)
    if x==y:
        return [len(v)]+[0]*(n-1)
    h=[0]*n
    d=(y-x)/n
    for a in v:
        k=int((a-x)/d)
        if k==n:
            k=n-1
        h[k]=h[k]+1
    return h

def filter_vector(v,k):
    r=[]
    m=len(k)//2
    for i in range(len(v)):
        s=0
        for j in range(len(k)):
            p=i+j-m
            if p>=0 and p<len(v):
                s=s+v[p]*k[j]
        r.append(s)
    return r
