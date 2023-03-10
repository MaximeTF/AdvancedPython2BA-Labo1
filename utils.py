import math
from scipy import integrate as itg 

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if (n>=0):
		fact=1
		for i in range(1,n+1):
			fact=fact*i
		return fact
	else:
		raise ValueError("n must be positive")
			
	
	pass

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	delta=b**2-4*a*c
	if (delta==0):
		return (-b/2/a)
	if delta<0:
		return tuple()
	SqRtdelta= math.sqrt(delta)
	return((-b-SqRtdelta)/2/a,(-b+SqRtdelta)/2/a)
	pass

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	return itg.quad(lambda x: eval(function, {'x':x}),lower,upper)[0]

	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 5, 4))
	print(integrate('x ** 2 - 1', -1, 1))
