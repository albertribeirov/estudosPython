def combine_lists(list1, list2):
	# Generate a new list containing the elements of list2
	# Followed by the elements of list1 in reverse order
	list1.reverse()
	list2.extend(list1)
	return list2


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
