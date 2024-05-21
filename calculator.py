def main():
	x = int(input("Value of x is: "))
	print("X squred is: ", square(x))

def square(n):
	return pow(n, 2)

main()