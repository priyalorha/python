'''
 Availabilty of a data beyond memory scope, within a nested function

 Techique of attaching a non local variable to a function

 Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.

'''


def outer(val):
    newval=val
    def inner():
        print(newval)

    inner()


outer(504)