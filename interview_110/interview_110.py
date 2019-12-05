#encoding:utf-8
#author:wangzhicheng
#time:2019/12/4 17:02
#file:interview_110.py

#1-100之和

#1.
num=sum(range(0,101))

i=0
sum_1=0

for i in range(101):
    sum_1+=i
    i+=1

print(num,sum_1)


params_1="name"
def func_1():
    global params_1
    params_1="zhicheng"

def func_2():
    params_1="manman"

func_1()
func_2()
print(params_1)

# os ,datetime ,time ,re,math,sys,json,random,unittest,logging

dict_1={"a":1,"b":2}

dict_1.pop("b")
del dict_1["a"]
dict_1.update({"c":3})
dict_1["d"]=5
print(dict_1)

a=[223,32,233,12,12,12,32]
print(list(set(a)))

a=[223,32,233,12,12,12,32]

b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)