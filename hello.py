def main():
	hello()
	name = input("What's your name?")
	name = name.strip().title()
	hello(name)

def hello(name="world"):
	print(f"Hello, {name}")

main()
