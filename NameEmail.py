# Outro exercício com Dictionaries ligando as contas dos usuários aos seus domínios de e-mail
def email_list(domains):
	emails = []
	for chave, valor in domains.items():
		for elemento in valor:
			emails.append("{}@{}".format(elemento, chave))
	return emails


print(email_list(
	{"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
	 "hotmail.com": ["bruce.wayne"]}))
