def f():
	global s
	print s
	s=80
	print s
	return 
	
s = 10
print s
f()
print s
