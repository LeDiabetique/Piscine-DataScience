import sys

def main(arg):
	if (len(arg) == 2):
		if (int(arg[1]) % 2 == 0):
			print("I'm Even.")
		else:
			print("I'm Odd.")
	return 0

if __name__ == "__main__":
	try:
		assert len(sys.argv) <= 2, "AssertionError: more than one argument is provided"
		if (len(sys.argv) == 2):
			assert sys.argv[1].lstrip('-').isdigit() == True, "AssertionError: argument is not an integer"
	except AssertionError as e:
		print(e)
		sys.exit(1)    
	main(sys.argv)