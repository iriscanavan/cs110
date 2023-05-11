# Iris Canavan, Section 3

import copy

def main():
	list_values = [34, 44, 65, 84, 52, 44, 67, 56, 23, 34, 21, 44]
	list_cumulative = [4, 7, 15, 23, 67, 150, 187, 198, 205, 208]
	n = 3
	lowest_num, lowest_index = find_lowest(list_values)
	print("Initial list of values =", list_values)
	print("Minimum Value =", lowest_num, "at index =", lowest_index)
	print("The average =", calc_average(list_values))
	print("Eliminate every 3rd element =",
		drop_every_nth_element(list_values, n))
	print("Eliminated duplicated values =",
		eliminate_duplicates(list_values))
	print("Duplicated list of values 3 times =",
		duplicate_n_times(list_values, n))
	print("-" * 180)
	print("Cumulative values =", list_cumulative)
	print("The difference between indices of cumulative list =",
		incremental(list_cumulative))

def find_lowest(pList):
	lowest_num = pList[0]
	for i in range(len(pList)):
		if pList[i] < lowest_num:
			lowest_num = pList[i]
			lowest_index = i
	return lowest_num, lowest_index

def calc_average(pList):
	return format(sum(pList) / len(pList), '.4f')

def incremental(pList):
	return [pList[i + 1] - pList[i] for i in range(len(pList)-1)]

def drop_every_nth_element(pList, n):
	list_copy = copy.deepcopy(pList)
	del list_copy[n-1::n]
	return list_copy

def eliminate_duplicates(pList):
	result = []
	for i in pList:
		if i not in result:
			result.append(i)
	return result

def duplicate_n_times(pList, n):
	return [pList[i//n] for i in range(len(pList) * n)]

main()
