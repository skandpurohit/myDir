Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> python3 -v
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    python3 -v
NameError: name 'python3' is not defined
>>> python -v
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    python -v
NameError: name 'python' is not defined
>>> car =  ["mazda" , "honda" , "toyota"]
>>> print(l)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(l)
NameError: name 'l' is not defined
>>> print(len(car))
3
>>> print(car)
['mazda', 'honda', 'toyota']
>>> car =  ["mazda" , "honda" , 'toyota']
>>> print(car)
['mazda', 'honda', 'toyota']
>>> cars =  ['mazda' , "honda" , 'toyota']
>>> print(CARS)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(CARS)
NameError: name 'CARS' is not defined
>>> print(cars)
['mazda', 'honda', 'toyota']
>>> cars.ex
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    cars.ex
AttributeError: 'list' object has no attribute 'ex'
>>> cars.extend(["cadillac","lincoln"])
>>> print(cars)
['mazda', 'honda', 'toyota', 'cadillac', 'lincoln']
>>> ['mazda', 'honda', 'toyota', 'cadillac', 'lincoln']
['mazda', 'honda', 'toyota', 'cadillac', 'lincoln']
>>> 
>>> 
>>> 
>>> cars.count
<built-in method count of list object at 0x030A4418>
>>> cars.count(1)
0
>>> cars.count(2)
0
>>> cars.count(123)
0
>>> cars.count([1])
0
>>> cars.insert(3, "BMW")
>>> print(cars)
['mazda', 'honda', 'toyota', 'BMW', 'cadillac', 'lincoln']
>>> for each_cars in cars:
	print(cars)
	end

	
['mazda', 'honda', 'toyota', 'BMW', 'cadillac', 'lincoln']
Traceback (most recent call last):
  File "<pyshell#28>", line 3, in <module>
    end
NameError: name 'end' is not defined
>>> for each_cars in cars:
	print(cars)

	
['mazda', 'honda', 'toyota', 'BMW', 'cadillac', 'lincoln']
['mazda', 'honda', 'toyota', 'BMW', 'cadillac', 'lincoln']
['mazda', 'honda', 'toyota', 'BMW', 'cadillac', 'lincoln']
['mazda', 'honda', 'toyota', 'BMW', 'cadillac', 'lincoln']
['mazda', 'honda', 'toyota', 'BMW', 'cadillac', 'lincoln']
['mazda', 'honda', 'toyota', 'BMW', 'cadillac', 'lincoln']
>>> for each_cars in cars:
	print(each_cars)

	
mazda
honda
toyota
BMW
cadillac
lincoln
>>> cars.insert(4 ,  '"Audi"')
>>> print(cars)
['mazda', 'honda', 'toyota', 'BMW', '"Audi"', 'cadillac', 'lincoln']
>>> cars.insert(4 ,  'Audi')
>>> print(cars)
['mazda', 'honda', 'toyota', 'BMW', 'Audi', '"Audi"', 'cadillac', 'lincoln']
>>> for each_cars in cars:
	print(each_cars)

	
mazda
honda
toyota
BMW
Audi
"Audi"
cadillac
lincoln
>>> cars.insert(3, "BMW["3 series" , "5 series"]")
SyntaxError: invalid syntax
>>> cars.insert(3, "BMW["series" , "series"]")
SyntaxError: invalid syntax
>>> cars.insert(3, "BMW['5 series' , '3 series']")
>>> print(cars)
['mazda', 'honda', 'toyota', "BMW['5 series' , '3 series']", 'BMW', 'Audi', '"Audi"', 'cadillac', 'lincoln']
>>> cars.insert(3, 'BMW['5 series' , '3 series']')
SyntaxError: invalid syntax
>>> print(cars)
['mazda', 'honda', 'toyota', "BMW['5 series' , '3 series']", 'BMW', 'Audi', '"Audi"', 'cadillac', 'lincoln']
>>> print(cars[4])
BMW
>>> print(cars[4][1])
M
>>> print(cars[4][3][1])
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(cars[4][3][1])
IndexError: string index out of range
>>> cars.re
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    cars.re
AttributeError: 'list' object has no attribute 're'
>>> cars.remove(4)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    cars.remove(4)
ValueError: list.remove(x): x not in list
>>> cars.remove(cars[4])
>>> print(cars)
['mazda', 'honda', 'toyota', "BMW['5 series' , '3 series']", 'Audi', '"Audi"', 'cadillac', 'lincoln']
>>> cars.remove("BMW")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    cars.remove("BMW")
ValueError: list.remove(x): x not in list
>>> cars.remove("Audi")
>>> print(cars)
['mazda', 'honda', 'toyota', "BMW['5 series' , '3 series']", '"Audi"', 'cadillac', 'lincoln']
>>> print(car)
['mazda', 'honda', 'toyota']
>>> car = ["mazda" ,  "toyota" , "honda" , "Audi" ]
>>> print(car)
['mazda', 'toyota', 'honda', 'Audi']
>>> car = ["mazda" ,  "toyota" , ["honda" , ["Civic" , "Accord"]] , "Audi" ]
>>> print(car)
['mazda', 'toyota', ['honda', ['Civic', 'Accord']], 'Audi']
>>> print(car[3][1][2])
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print(car[3][1][2])
IndexError: string index out of range
>>> print(car[3][1][1])
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(car[3][1][1])
IndexError: string index out of range
>>> print(car[2][1][1])
Accord
>>> print(car[2][1])
['Civic', 'Accord']
>>> print(car[2][0])
honda
>>> print(car[2][2])
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print(car[2][2])
IndexError: list index out of range
>>> car = ["mazda" ,  "toyota" , ["honda" , ["Civic" , "Accord"], ["Acura"]] , "Audi" ]
>>> print(car[2][2])
['Acura']
>>> print(car[2][2][0])
Acura
>>> for each_car in car:
	print(each_car)

	
mazda
toyota
['honda', ['Civic', 'Accord'], ['Acura']]
Audi
>>> for each_subcar in each_car in car:
	print(each_subcar)

	
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    for each_subcar in each_car in car:
TypeError: 'bool' object is not iterable
>>> for each_car in car:
	if is
	
SyntaxError: invalid syntax
>>> for each_car in car:
	if isinstance(each_car, list):
		for nested_item in each_car:
			print(nested_item)
			else:
				
SyntaxError: invalid syntax
>>> for each_car in car:
	if isinstance(each_car, list):
		for nested_item in each_car:
			print(nested_item)
	else:
		print(each_car)

		
mazda
toyota
honda
['Civic', 'Accord']
['Acura']
Audi
>>> def function(list):
	for each_car in car:
		if isinstance(each_car, list):
			for nested_item in each_car:
				print(nested_item)
		else:
		print(each_car)
		
SyntaxError: expected an indented block
>>> def function(list):
	for each_car in car:
		if isinstance(each_car, list):
			for nested_item in each_car:
				print(nested_item)
		else:
			print(each_car)

			
>>> function(car)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    function(car)
  File "<pyshell#86>", line 3, in function
    if isinstance(each_car, list):
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> def function(list):
	for each_item in item:
		if isinstance(each_item, list):
			for nested_item in each_item:
				print(nested_item)
		else:
			print(each_item)

			
>>> function(car)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    function(car)
  File "<pyshell#89>", line 2, in function
    for each_item in item:
NameError: name 'item' is not defined
>>> print(car)
['mazda', 'toyota', ['honda', ['Civic', 'Accord'], ['Acura']], 'Audi']
>>> def function(item):
	for each_item in item:
		if isinstance(each_item, list):
			for nested_item in each_item:
				print(nested_item)
		else:
			print(each_item)

			
>>> print(car)
['mazda', 'toyota', ['honda', ['Civic', 'Accord'], ['Acura']], 'Audi']
>>> function(car)
mazda
toyota
honda
['Civic', 'Accord']
['Acura']
Audi
>>> def function(item):
	for each_item in item:
		if isinstance(each_item, list):
			print(each_item)
		else:
			print(each_item)

			
>>> function(car)
mazda
toyota
['honda', ['Civic', 'Accord'], ['Acura']]
Audi
>>> def function(item):
	for each_item in item:
		if isinstance(each_item, list):
			function(each_item)
		else:
			print(each_item)

			
>>> function(car)
mazda
toyota
honda
Civic
Accord
Acura
Audi
>>> 
