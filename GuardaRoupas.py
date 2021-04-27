# Imprime os item do guarda roupa juntamente com suas cores
# Explora o uso de Dictionaries tendo como valor uma List
wardrobe = {"camisa": ["vermelha", "azul", "branca"], "calça jeans": ["azul", "preta"]}
for chave, valor in wardrobe.items():
	for item in valor:
		print("{} {}".format(chave, item))
