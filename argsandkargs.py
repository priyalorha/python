'''


*args is used to send a non-keyworded variable length argument list to the function
**kwargs allows you to pass keyworded variable length of arguments to a function.

'''


def ar(*args,**kargs):
    for i in args:
        print (i)
    for key in kargs:
        print("key={} and value ={}".format(key,kargs[key]),end=" ")

ar('yasoob','python','eggs','test')
ar(name="Priya")