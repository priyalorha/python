''' A generator is any fucntion with atleast one yield statement,

 A major difference between return and yield lies in the fact, yield statement
 pauses the function saving all its states and later continues from there on successive calls,
 where as return statement terminates a function entirely'''



def palin(a):
    while a!=0:
        yield a%10
        a//=10
for i in palin(425):
    print(i)