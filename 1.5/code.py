fst_list = input()
sec_list = input()

def mergeLists(fst_list, sec_list):
	list1 = fst_list[1:]
	list1 = list(list1[0:-1].split(', '))

	list2 = sec_list[1:]
	list2 = list(list2[0:-1].split(', '))


	if (list1 != ['']):
		for index, i in enumerate(list1):
			list1[index] = int(i)
		list1.sort()
	else:
		list1 = []

	if (list2 != ['']):
		for index, i in enumerate(list2):
			list2[index] = int(i)
		list2.sort()
	else:
		list2 = []

	summary_list = list1 + list2
	summary_list.sort()

	return summary_list

print(mergeLists(fst_list, sec_list))