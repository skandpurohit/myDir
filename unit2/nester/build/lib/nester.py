"""This function prints the array and sub-arrays"""
def recursiveArray(item):
	"""It takes an argument in form of list"""
	for each_item in item:
		if isinstance(each_item,list):
			recursiveArray(each_item)
		else:
			print(each_item)
			