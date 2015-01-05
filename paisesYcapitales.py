library={}
libraryList=[]
def init():
	print "  "
	print "welcome to Countries and Capitals "
	print "  "
	question=raw_input("Want Insert Other Countries and Capital - Countries -:  ")
	questionlower=question.lower()
	if questionlower == "Countries" or questionlower == "countries" or questionlower == "Countries " or questionlower == "countries ":
		addCountries()
	else:
		print "Enter a valid option:  "
		init()

def menu():
	print"  "
	print "Opciones:  "
	print "Write - paises - if you want to add an item."
	print "Press Capitals if you want to sell an item."
	print "Press All if you want to exit."
	print "Write AllOrdered para ordenado"
	print "Write AllMail para enviar al correo"
	try:
		options=raw_input("Choose an option:  ")
		if options == "countries":
			print "List of Countries"
			i=library.keys()
			for i in library:
				print (i.title())
			menu()
		elif options== "capitals":
			print "List of Capitals"
			e=library.values()
			for e in library.values():
				print (e.title())
			menu()
	except ValueError:
		print "Enter valid option for the Menu:  "
		menu()
def listCoutries():
	for i in libraryList:
		print i
	menu()

def addCountries():
	"""Esta funcion permite agregar datos a las listas y diccionarios"""
	try:
		key = raw_input("Add Countries: ")
		keylow = key.lower()
		libraryList.append(keylow) 
		global value
		value= raw_input("Add Capital: ")
		library[key]=value
		print library
		print libraryList
		again()
	except ValueError:
		print "Enter the data correctly"
		addCountries()
def again():
	"""Esta funcion pregunta si se quieren agregar oto pais"""
	question=raw_input("Do you want to insert another Countries and Capital (y/n) ")
	questionlower=question.lower()
	if questionlower == "y" or questionlower == "yes" or questionlower == "y " or questionlower == "yes ":
		addCountries()
	elif questionlower == "n" or questionlower == "no" or questionlower == "n " or questionlower == "no ":
		menu()
	else:
		print "A valid option and enter (y/n)"
		again()
init()