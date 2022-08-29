'''
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
	if i%49==0:
		print (i)
'''
import sys
nums_squared_lc = [num**2 for num in range(5)]
print(sys.getsizeof(nums_squared_lc))
print(nums_squared_lc)

nums_squared_gc = (num**2 for num in range(5))
print(sys.getsizeof(nums_squared_gc))
print(nums_squared_gc)
