'''for lop with an iterator
terator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.

Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the __iter__() method) returns an iterator from them.

The advantage of using iterators is that they save resources.

'''

nums=[x for x in range(10)]

print(nums)

print(dir(nums.__iter__()))
i_nums=iter(nums)
print(next(i_nums))
print(next(i_nums))


#dictionary
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

for k,v in thisdict.items():
    print(k,v)
