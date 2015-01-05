"""This function prints the array and sub-arrays"""
def recursiveArray(item, level):
	"""It takes an argument in form of list"""
	for each_item in item:
		if isinstance(each_item,list):
			recursiveArray(each_item, level+1)
		else:
			for tab in range(level):
				print("\t", end= '')
			print(each_item)
			