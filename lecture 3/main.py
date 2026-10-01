
import random
import time
from matrix_oper import *
from file_oper import *

def make_matrix(n,m):
    a=[]
    for i in range(n):
        r=[]
        for j in range(m):
            r.append(random.random())
        a.append(r)
    return a

def make_vector(n):
    v=[]
    for i in range(n):
        v.append(random.random())
    return v

def get_time(f,*a):
    t=time.perf_counter()
    f(*a)
    return time.perf_counter()-t

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[9,8,7],[6,5,4],[3,2,1]]
v=[1,2,3]
w=[4,5,6]

print("Матрица x матрица:")
print(matrix_multiply(a,b))

print("Матрица x вектор:")
print(matrix_vector_multiply(a,v))

print("След:")
print(matrix_trace(a))

print("Скалярное произведение:")
print(scalar_product(v,w))

print("Гистограмма:")
print(histogram([1,2,3,4,5,6,7,8,9,10],5))

print("Фильтр:")
print(filter_vector([1,2,3,4,5,6],[-1,0,1]))

write_vector("vector.txt",v)

print("Вектор из файла:")
print(read_vector("vector.txt"))

n=[10,25,50,100,150]
r=[]

for x in n:
    a=make_matrix(x,x)
    b=make_matrix(x,x)
    v=make_vector(x)

    t=get_time(matrix_multiply,a,b)
    r.append(["matrix_matrix",x,t])
    print(x,"matrix x matrix:",t)

    t=get_time(matrix_vector_multiply,a,v)
    r.append(["matrix_vector",x,t])
    print(x,"matrix x vector:",t)

    t=get_time(matrix_trace,a)
    r.append(["trace",x,t])
    print(x,"trace:",t)

    t=get_time(scalar_product,v,v)
    r.append(["scalar_product",x,t])
    print(x,"scalar product:",t)

    t=get_time(histogram,v,10)
    r.append(["histogram",x,t])
    print(x,"histogram:",t)

    t=get_time(filter_vector,v,[-1,0,1])
    r.append(["filter",x,t])
    print(x,"filter:",t)

write_results("results.csv",r)

print("Результаты записаны в results.csv")
