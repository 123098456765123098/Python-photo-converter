import random
a = ['A','B','C','D','E','F','G','H','a','b','c','d','e',1,2,3,4,5,6,7,8,9,0]
b = random.sample(a,10)
for x in b :
	print(x,end='')
