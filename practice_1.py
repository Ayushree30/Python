#Exercise 1: Given two integer numbers return their 
#product. If the product is greater than 1000, then return their sum
a=int(input('Enter the value a:'))
b=int(input('Enter the value of b:'))
if a*b > 1000:
	print(a+b)