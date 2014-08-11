#myreduce.py
import operator
def myReduce(function,iterable,initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce non itereable')
    accum_value=initializer
    for x in it:
        accum_value=function(accum_value,x)
    return accum_value

print type(operator.add)
print myReduce(operator.add,range(3,6))
assert(myReduce(operator.mul, range(3,6), 2) == (2*3*4*5))