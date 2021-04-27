def format_address(address_string):
	# Declare variables
	lista = []
	rua = ""
	# Separate the address string into parts
	lista = address_string.split()
	# Traverse through the address parts
	for linha in lista:
		# Determine if the address part is the
		# house number or part of the street name
		if linha.isnumeric():
			numero = linha
			lista.pop(0)
		else:
			rua = " ".join(lista)
	# Return the formatted string
	return "house number {} on street named {}".format(numero, rua)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
