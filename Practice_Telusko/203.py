from array import *

arr = array('i', [1, 2, 3, 4, 5])

print(arr)

newarr = array(arr.typecode, [x for x in arr])

print(newarr)