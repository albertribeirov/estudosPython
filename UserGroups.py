# Retorna um Dictionary com os usuários como chaves e uma lista de seus grupos como valor (key-value tipo Map no Java)
def groups_per_user(group_dictionary):
	user_groups = {}
	# Percorre o group_dictionary
	for grupo, users in group_dictionary.items():
		# Percorre os usuários no grupo
		for user in users:
			if user not in user_groups:
				# Caso o usuário não esteja no user_groups,
				# cria uma lista com seu primeiro grupo e adiciona
				# o usuário e sua lista de grupos ao Dictionary
				lista = [grupo]
				user_groups.update({user: lista})
			else:
				# Caso o usuário esteja no user_groups, obtém sua lista de grupos e adiciona
				# um novo grupo à lista
				user_groups.get(user).append(grupo)
	return user_groups


print(groups_per_user({"local": ["admin", "userA"], "public": ["admin", "userB"], "administrator": ["admin"]}))
