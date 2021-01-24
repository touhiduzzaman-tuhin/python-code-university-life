from array import *

li = array('i', [1, 2, 3, 4 ,5])

print(li)

li1 = array(li.typecode, [x*x for x in li])

print(li1)